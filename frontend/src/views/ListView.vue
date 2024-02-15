<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { list, loading } = useApi()

const router = useRouter()

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

onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const data = await list()
    items.push(...data)

})


</script>
<template>
  <heading>Listado de estaciones</heading>
  <div class="list-container">
      <my-button @on-tap="createItem" label="Agregar Radiolocalización" />
    <table>
      <tr>
        <th>id</th>
        <th>Expediente</th>
        <th>Área</th>
        <th>Fecha y hora</th>
        <th>Acciones</th>
      </tr>
      <tr
        v-for="item in items"
        :key="item"
      >
      <td><RouterLink :to="'file/'+item.id">{{ item.id }}</RouterLink></td> 
      <td>{{ item.expediente }}</td> 
      <td>{{ item.area }}</td> 
      <td>{{ item.fecha +" "+item.hora}}</td> 
      <td><my-button @on-tap="() => editItem(item.id)" label="Editar"/></td> 

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
table{
  justify-content: center; 
  
}
th, td{
  text-align: center;
  padding: 5px;
}
th{
  font-weight: 700;
  background-color: #cbcdce;
}
tr:nth-child(odd) {
  background-color: #ebeded;
}
/* a{
  color: rgb(0, 123, 255);
  text-decoration: none;
  font-weight: 500; 
} */
</style>