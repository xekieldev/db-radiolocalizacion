<script setup>
import { useApi } from '../composables/api'
import { useSearch } from '../composables/search'
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import FormSearch from '../components/FormSearch.vue'
import FooterMain from '../components/FooterMain.vue'


const { getAllTechnicians, delete_technician, loading } = useApi()
const { search } = useSearch()
const router = useRouter()

function createItem() {  
  router.push('/technician/create_technician')
}

const items = ref([])
const status = ref({});
const searchText = ref('')

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

async function searchTechnician(searchText) {
  const data = await getAllTechnicians()    
  items.value = search(data, searchText, ['apellido','nombre', 'area'])    
}

</script>
<template>
  <heading>Gestión de Técnicos</heading>
  <div class="technicians-menu">
    <form-search 
      :searchText = "searchText"
      placeholder = "Buscar Técnicos"
      @on-submit="searchTechnician"
    />
    <my-button
      class="secondary right"
      label="Nuevo Técnico"
      @on-tap="createItem"
    />
  </div>
  <div class="technicians-list-container"> 
    <table class="technicians-table">
      <tr>
        <th>id</th>
        <th>Nombre</th>
        <th>Apellido</th>
        <th>Área/CCTE</th>
        <th>Acciones</th>
      </tr>
      <tr
        v-for="item in items"
        :key="item"
      >
        <td>{{ item.id }}</td> 
        <td>{{ item.nombre }}</td> 
        <td>{{ item.apellido }}</td> 
        <td>{{ item.area }}</td>
        <td>
          <my-button
            v-if="status[item.id]!=1"
            class="primary center"
            label="Borrar"
            @on-tap="confirmar(item.id)"
          />
          <my-button
            v-if="status[item.id]===1"
            class="tertiary center"
            label="¿Confirmar?"
            @on-tap="del(item.id)"
          />
        </td>
      </tr>
    </table>
    <div class="status">
        <span><strong>Loading:</strong> {{ loading }}</span>
    </div>
  </div>
  <footer-main class="footer-main"/>
</template>

<style scoped>
.technicians-list-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  justify-content: center;
  margin-top: 10px;
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
}

</style>