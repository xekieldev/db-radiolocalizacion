<script setup>
import { useApi } from '../composables/api'
import { onMounted, reactive, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import DisplayRow from '../components/DisplayRow.vue';
import PropValue from '../components/PropValue.vue';



// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getFile, getTechMeasurement } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()



function viewItem(item) { 
  console.log("Aca!! ", item)
  router.push(`/file/${item}/create_tech_measurement`)
}

// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const file = reactive({})

const techMeasurement = reactive({})
const technicians = reactive({})
const idPath = ref(currentRoute.value.params.id)


onMounted(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const id = currentRoute.value.params.id
    const response = await getTechMeasurement(id)
    const fileResponse = await getFile(currentRoute.value.params.id)
    Object.assign(file, fileResponse.file)
    Object.assign(technicians, response.technicians)
    Object.assign(techMeasurement, response.techMeasurement)
    console.log(techMeasurement)
    console.log("technicians", response.technicians)
    console.log("file-id: ", file.id)
    
})



</script>
<template>
  
  <heading>Mediciones Técnicas Externas</heading>
    <!-- <RouterLink class="tab" :to="'/file/'+ file.id +'/create_tech_measurement'">Agregar Mediciones Técnicas</RouterLink> -->
    <my-button @on-tap="() => viewItem(file.id)" class="primary right" label="Agregar Mediciones Técnicas"/>

  <!-- <div v-for="value, index in techMeasurement">
  <dl>{{`Medición Técnica ${parseInt(index,10)+1}`}}</dl>
  <dl v-for="[key, value] in Object.entries(value)">
    <dt>{{key}}</dt>
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

  </div> -->

  <!-- <display-row v-if="techMeasurement[0].id"> 
    <prop-value class="prop" label="id Expediente" :value="file.id"/>
    <prop-value class="prop double" label="Expediente" :value="file.expediente"/>
    <prop-value class="prop" label="Area" :value="file.area"/>
    <prop-value class="prop" label="Fecha y hora" :value="file.fecha +' '+ file.hora"/>
  </display-row> -->
  <div v-for="value, index in techMeasurement">
  <display-row > 
      <prop-value class="prop technicians"  label="id" :value="techMeasurement[index].id"/>
      <prop-value class="prop technicians"  label="Fecha y hora" :value=" techMeasurement[index].fecha + ' ' + techMeasurement[index].hora"/>
      <prop-value class="prop technicians"  label="Area" :value=" techMeasurement[index].area"/>
      <!-- <prop-value class="prop technicians"  label="Localidad" :value=" techMeasurement[index].localidad"/>
      <prop-value class="prop technicians"  label="Domicilio" :value=" techMeasurement[index].domicilio"/>
      <prop-value class="prop technicians"  label="Latitud" :value=" techMeasurement[index].latitud"/>
      <prop-value class="prop technicians"  label="Longitud" :value=" techMeasurement[index].longitud"/> -->

  </display-row>
  <display-row > 
    <prop-value class="prop technicians"  label="Frecuencia Caracteristica" :value=" techMeasurement[index].frecuenciaCaract"/>
      <prop-value class="prop technicians"  label="Distancia" :value=" techMeasurement[index].distancia"/>
      <prop-value class="prop technicians"  label="Azimut" :value=" techMeasurement[index].azimut"/>
      <prop-value class="prop technicians"  label="MIC" :value=" techMeasurement[index].mic"/>
      <prop-value class="prop technicians"  label="Clase de Emision" :value=" techMeasurement[index].claseEmision"/>
      <prop-value class="prop technicians"  label="Ancho de Banda" :value=" techMeasurement[index].anchoBanda"/>
      <prop-value class="prop technicians"  label="Unidad" :value=" techMeasurement[index].unidad"/>
    </display-row>
  <display-row > 
      <prop-value class="prop technicians"  label="No esencial 1" :value=" techMeasurement[index].noEsencial1"/>
      <prop-value class="prop technicians"  label="MIC no esencial 1" :value=" techMeasurement[index].micNoEsencial1"/>
      <prop-value class="prop technicians"  label="No esencial 2" :value=" techMeasurement[index].noEsencial2"/>
      <prop-value class="prop technicians"  label="MIC no esencial 2" :value=" techMeasurement[index].micNoEsencial2"/>
      <prop-value class="prop technicians"  label="No esencial 3" :value=" techMeasurement[index].noEsencial3"/>
      <prop-value class="prop technicians"  label="MIC no esencial 3" :value=" techMeasurement[index].micNoEsencial3"/>
  </display-row>
  <display-row > 
      <prop-value class="prop technicians" v-for="value, index in technicians" label="Técnico" :value=" technicians[index].nombre + ', ' + technicians[index].apellido"/>
  </display-row>

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

  .prop {
    flex-grow: 1;
    align-items: center;
  }
</style>