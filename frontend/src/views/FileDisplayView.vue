<script setup>
// import { useLocalStorage } from '../composables/localstorage'
import { useApi } from '../composables/api'
import { onMounted, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'



// const ls = useLocalStorage()
// debugger
// const data = ls.list()
// console.log(data)

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getFile, loading, getTechnicians } = useApi()
const { currentRoute } = useRouter()

// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const file = reactive({})
const station = reactive({})
const technicians = reactive({})
const techniciansValues = reactive({})

onMounted(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
// debugger
    const response = await getFile(currentRoute.value.params.id)
    const techResponse = await getTechnicians()

    Object.assign(file, response.file)
    Object.assign(station, response.station)
    Object.assign(technicians, response.technicians)
    Object.assign(techniciansValues, techResponse)
    console.log("file: ", file)
    console.log("station", station)
    console.log('technicians', technicians)
    

    // file =data
    
})


</script>
<template>
<!-- <dl v-for="([value, name]) in Object.entries(file)">
    <dt>{{name}}</dt>
    <dd>{{value}}</dd>
</dl>
{{ file }} -->

  <h3>Expediente</h3>
  <dl v-for="([key, value]) in Object.entries(file)">
    <dt>{{key}}</dt>
    <dd>{{value}}</dd>
  </dl>
  <h3>Estación</h3>
  <dl v-for="[key, value] in Object.entries(station)">
    <dt>{{key}}</dt>
    <dd>{{value}}</dd>
  </dl>
  <h3>Técnicos</h3>
  <div v-for="value, index in technicians">
  <dl>{{`Técnico ${parseInt(index,10)+1}`}}</dl>
  <dl v-for="[key, value] in Object.entries(value)">
    <dt>{{key}}</dt>
    <dd>{{value}}</dd>
  </dl>

  </div>

  <RouterLink to="/list">Volver</RouterLink>
</template>

<style scoped>
.status{
    background-color: lightyellow;
}
dl {
    padding: 0.2em;
  }
  dt {
    float: left;
    clear: left;
    width: 200px;
    text-align: right;
    font-weight: bold;
    color: green;
    text-transform: capitalize;
  }
  dt::after {
    content: ":";
  }
  dd {
    margin: 0 0 0 210px;
    padding: 0 0 0.1em 0;
  }
</style>