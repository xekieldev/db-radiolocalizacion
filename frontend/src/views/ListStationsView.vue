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

function editItem(item) {  
  router.push(`/file/${item}/edit`)
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
  const data = await listStations(true)
  items.value.push(...data)
  console.log("data else: ", data)
  for (const item in items.value) {
    items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
    items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
    
  }
  console.log(":Items modify ", items)
    
    
})

async function searchStations() {
  const searchString = searchText.value.toLowerCase()
  console.log("Texto a buscar: ", searchText.value)
  const data = await listStations(true)
  // debugger
  const searchResult = data.filter((item) => item.id == searchString || item.identificacion.toLowerCase().includes(searchString) || item.domicilio.toLowerCase().includes(searchString) || item.frecuencia.toString().includes(searchString) || getNameByCode("city", item.localidad).toLowerCase().includes(searchString) || getNameByCode("province", item.provincia).toLowerCase().includes(searchString))
  // items.value.push(...searchResult)
  // Object.assign(items.value, [])
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
          placeholder="Buscar"
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
        <!-- <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">Status</th> -->
        <th>Domicilio</th>
        <th>Localidad (Provincia)</th>
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
      <td>{{ item.frecuencia +" "+item.unidad}}</td> 
      <td>{{ item.domicilio }}</td>
      <td>{{ item.localidad + " (" + item.provincia +")" }} </td>
      <!-- <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">{{ item.status }}</td> -->
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
  flex: 0 0 30%;
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