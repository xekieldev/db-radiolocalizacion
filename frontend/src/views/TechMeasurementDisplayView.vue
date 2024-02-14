<script setup>
import { useApi } from '../composables/api'
import { onMounted, reactive, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';



// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getTechMeasurement } = useApi()
const { currentRoute } = useRouter()


// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado

const techMeasurement = reactive({})
const technicians = reactive({})
const idPath = ref(currentRoute.value.params.id)


onMounted(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono

    const id = currentRoute.value.params.id
       
    const response = await getTechMeasurement(id)
 
    Object.assign(technicians, response.technicians)
    Object.assign(techMeasurement, response.techMeasurement)
    console.log(techMeasurement[0])
    console.log("technicians", response.technicians)
 
})



</script>
<template>
  
  <heading>Mediciones Técnicas Externas</heading>
  <div v-for="value, index in techMeasurement">
  <dl>{{`Medición Técnica ${parseInt(index,10)+1}`}}</dl>
  <dl v-for="[key, value] in Object.entries(value)">
    <dt>{{key}}</dt>
    <!-- <dd v-if="value != null">{{value}}</dd> -->
    <dd>{{ value !== null ? value : '---' }}</dd>

  </dl>

  </div>
  <h3>Técnicos</h3>
  <div v-for="value, index in technicians">
  <dl>{{`Técnico ${parseInt(index,10)+1}`}}</dl>
  <dl v-for="[key, value] in Object.entries(value)">
    <dt>{{key}}</dt>
    <dd>{{ value !== null ? value : '---' }}</dd>

  </dl>

  </div>

  <RouterLink :to="'/file/'+ idPath">Volver</RouterLink>
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