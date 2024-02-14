<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';


// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getAllTechnicians, delete_technician, loading } = useApi()
const router = useRouter()


// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const items = reactive([])
const status = ref({});
console.log(items)


onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const data = await getAllTechnicians()
    items.push(...data)
    console.log('items',items)
    
})

const confirmar = (id) => {
      status.value[id] = status.value[id] === 1 ? 0 : 1
}


async function del(id) {
    try {
    
    // console.log("id del path: ", id)
    const response = await delete_technician(id)
    status.value[id] = 0
    window.location.reload()


    } catch (error) {

    console.error(error)
    
    }
    
  }


</script>
<template>
  <heading>Técnicos</heading>
  <div class="technicians-list-container">
     <RouterLink to="/technician/create_technician">Agregar Nuevo Técnico</RouterLink>
  <table>
    <tr>
      <th>id</th>
      <th>Nombre</th>
      <th>Apellido</th>
      <th>Acciones</th>
    </tr>
    <tr
      v-for="item in items"
      :key="item"
    >
     <td>{{ item.id }}</td> 
     <td>{{ item.nombre }}</td> 
     <td>{{ item.apellido }}</td> 
     <td><a @click="confirmar(item.id)" v-if="status[item.id]!=1">Borrar</a>
     <a @click="del(item.id)" v-if="status[item.id]===1" class="danger">Confirmar?  </a></td>
    </tr>
    
    <div class="status">
      <span><strong>Loading:</strong> {{ loading }}</span>
    </div>
  </table>
</div>

</template>

<style scoped>
.technicians-list-container {
  display: flex;
  flex-direction: column;
  max-width: 900px;
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
.danger{
  color: red;
  font-weight: 700;
}
</style>