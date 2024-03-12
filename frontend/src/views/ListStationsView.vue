<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, onMounted, reactive, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import { useTerritory } from '../composables/territory'
import FormRow from '../components/FormRow.vue'

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { listStations, getStation, loading, deleteFile } = useApi()

const router = useRouter()
const currentRoute = useRouter()
const { getNameByCode } = useTerritory()

// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const items = ref([])
const searchText = ref()

// function editItem(item) {  
//   router.push(`/file/${item}/edit`)
// }
function editItem(item) {
  console.log("argumento: ", item)
  console.log("item: ", items)
  console.log("station: ", items.value.find(station => station.id === item).frecuencia)
  
  
  if (items.value.find(station => station.id === item).frecuencia != null || items.value.find(station => station.id === item).frecuencia != undefined) {
    
    router.currentRoute.value.query.rloc = 'true'
    router.push({ name: 'editFile', params: { id: item }, query: { rloc: 'true'} })

  } else {
    
    router.currentRoute.value.query.rloc = 'false'
    router.push({ name: 'editFile', params: { id: item }, query: { rloc: 'false'} })

  }
}


function createItem() {  
  router.push('/file/create')
}
function viewItem(item) {  
  router.push(`/file/${item}`)
}

async function deleteItem(item) {  
  console.log("id?", item)
  
  const response = await deleteFile(item)
  window.location.reload()

  
}

onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {

      const data = await listStations()
      items.value.push(...data)
      const stations = items.value
      console.log("stations if: ", items.value)
      for (const item in items.value) {
        items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
        items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
        
      }
      console.log(":Items modify ", items)
    } else {
        const data = await listStations(true)
        items.value.push(...data)
        const stations = items.value
        console.log("stations else: ", items.value)
        
        console.log("data else: ", data)
        for (const item in items.value) {
          items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
          items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
        }
      }
      
})

async function searchStations() {
  const searchStringTemp = searchText.value ? searchText.value.toLowerCase() : ''
  const searchString = searchStringTemp.split('+')
  console.log("Texto a buscar: ", searchString, searchText.value)
  const data = await listStations(false)
  // debugger
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


</script>
<template>
  <heading>Listado de Estaciones</heading>
  <div>
    <form-row class="search-bar">
        <form-kit
          outer-class="field-search"
          type="text"
          name="searchInput"
          placeholder="Buscar estaciones"
          v-model="searchText"
        />
        <my-button @on-tap="() => searchStations()" class="secondary buscar-btn" label="Buscar"/>
        
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
        <th>Localidad (Provincia)</th>
        <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">Status</th>
        <th>Acciones</th>
      </tr>
      <tr
        v-for="item in items"
        :key="item"
      >
      <!-- <td><RouterLink :to="'file/'+item.id">{{ item.id }}</RouterLink></td> -->
      <td><my-button @on-tap="() => viewItem(item.id)" class="primary center" :label="(item.id.toString())"/></td>
      <!-- <td>{{ item.id }}</td> -->
      <td>{{ item.identificacion }}</td> 
      <td>{{ item.servicio }}</td> 
      <td v-if="item.frecuencia">{{ item.frecuencia +" "+item.unidad}}</td>
      <td v-else>---</td>
      <td>{{ item.emplazamiento }}</td>
      <td>{{ item.domicilio }}</td>
      <td>{{ item.localidad + " (" + item.provincia +")" }} </td>
      <!-- <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">{{ item.status }}</td> -->
      <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">{{ item.status2 }}</td>
      <td> 
        <div class="action-buttons-container">
          <my-button @on-tap="() => editItem(item.id)" class="primary center" label="Editar"/>
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
  flex: 0 0 20%;
  margin: 0;
  
}
.search-bar {
  display: flex;
  justify-content: end;
}
.buscar-btn {
  margin: 0 5px;
}
</style>