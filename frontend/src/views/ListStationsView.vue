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


const { listStations, loading, deleteStation } = useApi()

const router = useRouter()
const { getNameByCode } = useTerritory()
const { search } = useSearch()


const items = ref([])
const searchText = ref('')
const confirm_delete = ref({})



function editItem(file_id, id) {
  if (items.value.find(station => station.id === id).frecuencia != null || items.value.find(station => station.id === id).frecuencia != undefined) {
    
    router.currentRoute.value.query.rloc = 'true'
    router.push({ name: 'editStation', params: { file_id: file_id, id: id }, query: { rloc: 'true'} })

  } else {
    
    router.currentRoute.value.query.rloc = 'false'
    router.push({ name: 'editStation', params: { file_id: file_id, id: id }, query: { rloc: 'false'} })

  }
}


function viewItem(file_id, id) {  
  router.push(`/file/${file_id}/station/${id}`)
}

async function deleteItem(file_id, id) {  
  await deleteStation(file_id, id)
  window.location.reload() 
}

const confirm = (id) => {
  console.log(confirm_delete.value)
  confirm_delete.value[id] = confirm_delete.value[id] === 1 ? 0 : 1
  console.log(confirm_delete.value)
  
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

async function searchStations(searchText) {
  const data = await listStations(false)
  items.value = search(data, searchText, ['identificacion','servicio', 'frecuencia', 'domicilio', 'localidad', 'provincia', 'emplazamiento'])  
}

function viewMap() {  
  router.push(`/station_map`)
}


</script>
<template>
  <heading>Listado de Estaciones</heading>
  <div class="stations-menu">
    <form-search 
      :searchText = "searchText"
      placeholder = "Buscar Estaciones"
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
    <table class="stations-table">
      <tr>
        <th>id</th>
        <th>Identificación</th>
        <th>Servicio</th>
        <th>Frecuencia</th>
        <th>Emplazamiento</th>
        <!-- <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">Status</th> -->
        <th>Domicilio</th>
        <th>Localidad</th>
        <th>Provincia</th>
        <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">
          Status
        </th>
        <!-- <th>Acciones</th> -->
      </tr>
      <tr
        v-for="item in items"
        :key="item"
      >
        <td>
          <my-button
            class="primary center"
            :label="(item.id.toString())"
            @on-tap="() => viewItem(item.file_id, item.id)"
          />
        </td>
        <!-- <td>{{ item.id }}</td> -->
        <td>{{ item.identificacion }}</td> 
        <td>{{ item.servicio }}</td> 
        <td v-if="item.frecuencia">
          {{ item.frecuencia +" "+item.unidad }}
        </td>
        <td v-else>
          ---
        </td>
        <td>{{ item.emplazamiento }}</td>
        <td>{{ item.domicilio }}</td>
        <td>{{ item.localidad }} </td>
        <td>{{ item.provincia }} </td>
        <!-- <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">{{ item.status }}</td> -->
        <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">
          {{ item.status }}
        </td>
        <!-- <td> 
          <div class="action-buttons-container">
            <my-button
              class="primary center"
              label="Editar"
              @on-tap="() => editItem(item.file_id, item.id)"
            />
            <my-button
              v-if="confirm_delete[item.id]!==1"
              class="tertiary center"
              label="Borrar"
              @on-tap="() => confirm(item.id)"
            />
            <my-button
              v-if="confirm_delete[item.id]===1"
              class="tertiary center"
              label="¿Confirmar?"
              @on-tap="() => deleteItem(item.file_id, item.id)"
            />
          </div>
        </td> -->
      </tr>
    </table>
    <div class="status">
        <span><strong>Loading:</strong> {{ loading }}</span>
    </div>
  </div>
  <footer-main class="footer-main"/>
</template>

<style scoped>
.list-container{
  display: flex;
  flex-direction: column;
  /* max-width: 900px; */
  width: 100%;
  justify-content: center;
  /* font-size: 14px; */
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
}

</style>