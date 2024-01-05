<script setup>
// import { useLocalStorage } from '../composables/localstorage'
import { useApi } from '../composables/api'
import { onBeforeMount, reactive } from 'vue'
import { RouterLink } from 'vue-router'


// const ls = useLocalStorage()
// debugger
// const data = ls.list()
// console.log(data)

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { list, getFile, loading } = useApi()

// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const items = reactive([])
// const files = reactive([])

onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const data = await list()
    items.push(...data)
    console.log('items',items)
    // for (let i in items){
    //   console.log(i)
      
    //   const data2 = await getFile(i)
    //   files.push({ ...data2[1]})
    //   console.log("data 2:", data2)
      
    //   console.log("files: ",files)
    // }
})
// onBeforeMount(async () => {
//     // El await acá es necesario para representar que se está
//     // haciendo una llamada a un método asíncrono
//     const data = await getStation(item.id)
//     stations.push(...data)
//     console.log("station: ",data)

// })

</script>
<template>
     <RouterLink to="/file/create">Agregar Radiolocalización</RouterLink>
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
     <td><RouterLink :to="'file/'+item.id+'/edit'">Editar</RouterLink></td> 

    </tr>
    
    <!-- <p>Detalle local storage</p> -->
    <div class="status">
      <span><strong>Loading:</strong> {{ loading }}</span>
      <!-- <br>
      <span><strong>Items:</strong><br> {{ items }}</span>
      <br> -->
    </div>
  </table>
</template>

<style scoped>
.status{
    background-color: lightyellow;
}
table{
  width: 60vw;
}
th, td{
  text-align: center;
  padding: 5px;
}
th{
  font-weight: 700;
  background-color: #0fc0c0;
}
tr:nth-child(odd) {
  background-color: #D6EEEE;
}
</style>