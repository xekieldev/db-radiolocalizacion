<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import { useTerritory } from '../composables/territory'
import FormRow from '../components/FormRow.vue'


const { listStations, loading } = useApi()

const router = useRouter()
const { getNameByCode } = useTerritory()


const items = ref([])
const searchText = ref()


function editItem(item) {
  if (items.value.find(station => station.id === item).frecuencia != null || items.value.find(station => station.id === item).frecuencia != undefined) {
    
    router.currentRoute.value.query.rloc = 'true'
    router.push({ name: 'editFile', params: { id: item }, query: { rloc: 'true'} })

  } else {
    
    router.currentRoute.value.query.rloc = 'false'
    router.push({ name: 'editFile', params: { id: item }, query: { rloc: 'false'} })

  }
}


function viewItem(item) {  
  router.push(`/file/${item}`)
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

async function searchStations() {
  const searchStringTemp = searchText.value ? searchText.value.toLowerCase() : ''
  const searchString = searchStringTemp.split('+')
  const data = await listStations(false)
  const searchResult = data.filter((item) => {
    const id = item.id
    const identificacion = item.identificacion ? item.identificacion.toLowerCase() : ''
    const servicio = item.servicio ? item.servicio.toLowerCase() : ''
    const frecuencia = item.frecuencia !== null && item.frecuencia !== undefined ? item.frecuencia.toString() : ''
    const domicilio = item.domicilio ? item.domicilio.toString().toLowerCase() : ''
    const localidad = getNameByCode("city", item.localidad) ? getNameByCode("city", item.localidad).toLowerCase() : '' 
    const provincia = getNameByCode("province", item.provincia) ? getNameByCode("province", item.provincia).toLowerCase() : '' 
    const emplazamiento = item.emplazamiento ? item.emplazamiento.toLowerCase() : ''
    
    return id == searchString || identificacion.includes(searchString) || servicio.includes(searchString) || frecuencia.includes(searchString) || domicilio.includes(searchString) || localidad.includes(searchString) || provincia.includes(searchString) || emplazamiento.includes(searchString)
    
  })

  items.value = searchResult
  for (const item in items.value) {
    items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
    items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
  }
}

function viewMap() {  

  router.push(`/station_map`)
}


</script>
<template>
  <heading>Listado de Estaciones</heading>
  <div class="bar-menu">
    <div class="view-map-container">
      <my-button
        class="secondary left view-map-button"
        label="Ver Mapa"
        @on-tap="viewMap"
      />
    </div>
    <form-row class="search-bar">
      <form-kit
        v-model="searchText"
        outer-class="field-search"
        type="text"
        name="searchInput"
        placeholder="Buscar estaciones"
      />
      <my-button
        class="secondary buscar-btn"
        label="Buscar"
        @on-tap="() => searchStations()"
      />
    </form-row>
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
        <th>Acciones</th>
      </tr>
      <tr
        v-for="item in items"
        :key="item"
      >
        <!-- <td><RouterLink :to="'file/'+item.id">{{ item.id }}</RouterLink></td> -->
        <td>
          <my-button
            class="primary center"
            :label="(item.id.toString())"
            @on-tap="() => viewItem(item.id)"
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
          {{ item.status2 }}
        </td>
        <td> 
          <div class="action-buttons-container">
            <my-button
              class="primary center"
              label="Editar"
              @on-tap="() => editItem(item.id)"
            />
          <!-- <my-button @on-tap="() => deleteItem(item.id)" class="tertiary center" label="Borrar"/> -->
          </div>
        </td>
      </tr>

      <div class="status">
        <span><strong>Loading:</strong> {{ loading }}</span>
      </div>
    </table>
  </div>
</template>

<style scoped>
.list-container{
  display: flex;
  flex-direction: column;
  /* max-width: 900px; */
  width: 100%;
  justify-content: center;
  font-size: 14px;
}
.status{
    background-color: lightyellow;
}
.stations-table{
  justify-content: center; 
  margin-top: 10px;
  
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
  
.field-search {
  display: flex;
  /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
  /* flex: 0 0 50%; */
  margin: 0;
  
}
.search-bar {
  display: flex;
  justify-content: end;
  align-items: end;
  margin-left: auto;
  
}
.buscar-btn {
  margin: 0 5px;
  bottom: 2px;
  
}
.bar-menu {
  display: flex;
  justify-content: space-between;
  top: 2px;
}

.view-map-container {
  /* margin: auto; */
  left: 0;
  margin-right: auto;
  
}

.view-map-button {
  top: 2px;
}

</style>