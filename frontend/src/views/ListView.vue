<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { list, loading, deleteFile } = useApi()

const router = useRouter()
const currentRoute = useRouter()

// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const items = reactive([])

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
    console.log("Path", router.currentRoute.value.query.includeDeleted)
    if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
      const data = await list()
      items.push(...data)
      console.log("filtrado", items.filter(check))
      function check(item) {
      console.log(item.area)

      return item.area == "POSADAS"
    }

      // console.log("data: ", data)
    } else {
        const data = await list(true)
        items.push(...data)
        // console.log("data else: ", data)
        console.log("filtrado", items.filter(check))
    }
    function check(item) {
      console.log(item.id)
      
      return item.id == "2"
    }
    
})


</script>
<template>
  <heading>Gestión de Expedientes</heading>
  <div class="list-container">
      <!-- <my-button @on-tap="createItem" class="secondary right" label="Nueva Radiolocalización" /> -->
    <table>
      <tr>
        <th>id</th>
        <th>Expediente</th>
        <th>Área</th>
        <th>Fecha y hora</th>
        <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">Status</th>
        <th>Acciones</th>
      </tr>
      <tr
        v-for="item in items"
        :key="item"
      >
      <!-- <td><RouterLink :to="'file/'+item.id">{{ item.id }}</RouterLink></td> -->
      <td><my-button @on-tap="() => viewItem(item.id)" class="primary center" :label="(item.id.toString())"/></td>
      <td>{{ item.expediente }}</td> 
      <td>{{ item.area }}</td> 
      <td>{{ item.fecha +" "+item.hora}}</td> 
      <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">{{ item.status }}</td>
      <td> 
        <div class="action-buttons-container">
          <my-button @on-tap="() => editItem(item.id)" class="primary center" label="Editar"/>
          <my-button @on-tap="() => deleteItem(item.id)" class="tertiary center" label="Borrar"/>
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
table{
  justify-content: center; 
  margin-top: 5px;
  
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
  
</style>