<script setup>
import { useApi } from '../composables/api'
import { useSearch } from '../composables/search'
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import FormSearch from '../components/FormSearch.vue'
import FooterMain from '../components/FooterMain.vue'
import { exportFile, QBtn, QTable, QTd, QTh } from 'quasar'


const { getAllTechnicians, delete_technician, loading } = useApi()
const { search } = useSearch()
const router = useRouter()

function createItem() {  
  router.push('/technician/create_technician')
}

const items = ref([])
const status = ref({})
const textToSearch = ref('')

onBeforeMount(async () => {
  const data = await getAllTechnicians()
  items.value.push(...data)
})

const confirmar = (id) => {
  status.value[id] = status.value[id] === 1 ? 0 : 1
}

async function del(id) {
  try { 
    await delete_technician(id)
    status.value[id] = 0
    window.location.reload()
  } catch (error) {
  console.error(error) 
  }  
}

async function searchTechnician(textToSearch) {
  const data = await getAllTechnicians()    
  items.value = search(data, textToSearch, ['apellido','nombre', 'area'])    
}

const columns = [
  { name: 'id',
    label: 'id', 
    field: 'id', 
    sortable: true, 
    align: 'center'
  },
  { name: 'nombre', label: 'Nombre', field: 'nombre', sortable: true, align: 'center' },
  { name: 'apellido', label: 'Apellido', field: 'apellido', sortable: true, align: 'center' },
  { name: 'area', label: 'Área/CCTE', field: 'area', sortable: true, align: 'center' },
  { name: 'acciones', label: 'Acciones', field: 'acciones', align: 'center' },
]

</script>
<template>
  <heading>Gestión de Técnicos</heading>
  <div class="technicians-menu">
    <form-search 
      :text-to-search="textToSearch"
      placeholder="Buscar Técnicos"
      @on-submit="searchTechnician"
    />
    <div>
      <my-button
        class="secondary right"
        label="Nuevo Técnico"
        @on-tap="createItem"
      />
    </div>
  </div>
  <div class="technicians-list-container"> 
    <q-table
      dense
      flat
      :rows="items"
      :columns="columns"
      row-key="id"
      :pagination="{ rowsPerPage: 15 }"
      separator="vertical"
      table-class="zebra"
      table-header-style="height: 45px;"
    >
  
    <template v-slot:header-cell="props">
      <q-th :props="props">
        {{ props.col.label }}
      </q-th>
    </template>
   
    <!-- Acciones personalizadas en la última columna -->
    <template v-slot:body-cell-acciones="props">
      <q-td :props="props">
        <my-button
            v-if="status[props.row.id]!=1"
            class="tertiary center"
            label="Borrar"
            @on-tap="confirmar(props.row.id)"
          />
          <my-button
            v-if="status[props.row.id]===1"
            class="tertiary center"
            label="¿Confirmar?"
            @on-tap="del(props.row.id)"
          />
      </q-td>
    </template>
  </q-table>
    <div class="status">
      <span><strong>Loading:</strong> {{ loading }}</span>
    </div>
  </div>
  <footer-main class="footer-main" />
</template>

<style scoped>

:deep(div.zebra table tr:nth-child(even))
{background-color: #ebeded;}

.technicians-list-container {
  font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu,
    Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  font-size: 15px;
  display: flex;
  flex-direction: column;
  width: 100%;
  justify-content: center;
  margin-top: 10px;
  padding: 0 30px;
}
.technicians-table {
  font-size: 12px;
}
.status{
    background-color: lightyellow;
}
th, td{
  text-align: center;
  padding: 5px;
}
th{
  font-weight: 700;
  /* font-size: 15px; */
  background-color: #cbcdce;
  border-radius: 10px 0 0;

}
tr:nth-child(odd) {
  background-color: #ebeded;
  border-radius: 10px 0 0;

}
.danger {
  color: red;
  font-weight: 700;
  border: 1px solid red;
}
.danger:hover {
  background-color: red;
}
.technicians-menu {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0 30px;
}

</style>