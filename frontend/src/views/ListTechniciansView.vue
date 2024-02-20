<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';


// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getAllTechnicians, delete_technician, loading } = useApi()
const router = useRouter()

function createItem() {  
  router.push('/technician/create_technician')
}
function deleteItem() {  
  router.push('/technician/create_technician')
}
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
  <heading>Gestión de Técnicos</heading>
  <div class="technicians-list-container">
     <!-- <RouterLink to="/technician/create_technician">Agregar Nuevo Técnico</RouterLink> -->
     <my-button @on-tap="createItem" class="secondary right" label="Nuevo Técnico" />
  <table>
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
          <my-button @on-tap="confirmar(item.id)" v-if="status[item.id]!=1" class="primary center" label="Borrar"/>
          <my-button @on-tap="del(item.id)" v-if="status[item.id]===1" class="tertiary center" label="¿Confirmar?"/>
      </td>
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
  /* max-width: 900px; */
  width: 100%;
  justify-content: center;
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


.danger {
  color: red;
  font-weight: 700;
  border: 1px solid red;
}
.danger:hover {
  background-color: red;
}

</style>