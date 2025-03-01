<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import { useTerritory } from '../composables/territory'
import { useSearch } from '../composables/search'
import FormSearch from '../components/FormSearch.vue'
import FooterMain from '../components/FooterMain.vue'
import { exportFile, QBtn, QTable, QTd, QTh } from 'quasar'


const { listStations, loading } = useApi()

const router = useRouter()
const { getNameByCode } = useTerritory()
const { search } = useSearch()


const items = ref([])
const textoToSearch = ref('')

function viewItem(file_id, id) {  
  router.push(`/file/${file_id}/station/${id}`)
}

onBeforeMount(async () => {
  if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
    const data = await listStations()
    items.value.push(...data)
    for (const item in items.value) {
      items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
      items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
    }
  } else {
      const data = await listStations(true)
      items.value.push(...data)
      for (const item in items.value) {
        items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
        items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
      }
    }      
})

async function searchStations(textoToSearch) {
  const data = await listStations(false)
  items.value = search(data, textoToSearch, ['identificacion','servicio', 'frecuencia', 'domicilio', 'localidad', 'provincia', 'emplazamiento'])
    for (const item in items.value) {
        items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
        items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
      }
}

function viewMap() {  
  router.push(`/station_map`)
}

const columns = [
  { name: 'id',
    label: 'id', 
    field: 'id', 
    sortable: true, 
    align: 'center'
  },
  { name: 'identificación', label: 'Identificación', field: 'identificacion', sortable: true, align: 'center' },
  { name: 'servicio', label: 'Servicio', field: 'servicio', sortable: true, align: 'center' },
  { name: 'frecuencia', label: 'Frecuencia', field: row => row.frecuencia ? row.frecuencia : '---', sortable: true, align: 'center' },
  { name: 'emplazamiento', label: 'Emplazamiento', field: 'emplazamiento', sortable: true, align: 'center' },
  { name: 'domicilio', label: 'Domicilio', field: 'domicilio', sortable: true, align: 'center' },
  { name: 'localidad', label: 'Localidad', field: 'localidad', sortable: true, align: 'center' },
  { name: 'provincia', label: 'Provincia', field: 'provincia', sortable: true, align: 'center' },
]

</script>
<template>
  <heading>Listado de Estaciones</heading>
  <div class="stations-menu">
    <form-search 
      :text-to-search="textoToSearch"
      placeholder="Buscar Estaciones"
      @on-submit="searchStations"
    />
    <div>
      <my-button
        class="secondary right view-map-button"
        label="Ver Mapa"
        @on-tap="viewMap"
      />
    </div>
  </div>

  <div class="list-container">
    <!-- <my-button @on-tap="createItem" class="secondary right" label="Nueva Radiolocalización" /> -->
    <q-table
      dense
      flat
      wrap-cells
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
      <template v-slot:body-cell-id="props">
          <q-td :props="props">
            <my-button
              class="primary center my-btn"
              :label="props.row.id.toString()"
              @on-tap="() => viewItem(props.row.file_id, props.row.id)"
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

.list-container{
  display: flex;
  flex-direction: column;
  /* max-width: 900px; */
  width: 100%;
  justify-content: center;
  /* font-size: 14px; */
  margin-top: 10px;
  padding: 0 30px;
}
.status{
    background-color: lightyellow;
}
.stations-table{
  justify-content: center; 
  margin-top: 10px;
  font-size: 12px;
}

th, td{
  text-align: center;
  padding: 5px;
}
th{
  font-weight: 700;
  background-color: #cbcdce;
  border-radius: 10px 0 0;
  white-space: nowrap;
}
tr:nth-child(odd) {
  background-color: #ebeded;
  border-radius: 10px 0 0;

}

.action-buttons-container {
  display: flex;
  flex-direction: row;
  gap: 1px;
  margin: 0;
}
.stations-menu {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0 30px;
}
.my-btn {
  height: fit-content;
}

</style>