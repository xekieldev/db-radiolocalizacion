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

function goBack(item) {  
  router.push(`/file/${item}`)
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
console.log("idPath: ", idPath)



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
    console.log("TechMeasurement: ", response.techMeasurement)
    console.log("file-id: ", file.id)
    console.log("technicians: ", technicians)
    
    
})



</script>
<template>
  
  <heading>Mediciones Técnicas Externas</heading>
    <!-- <RouterLink class="tab" :to="'/file/'+ file.id +'/create_tech_measurement'">Agregar Mediciones Técnicas</RouterLink> -->
  <div class="buttons-container" >
    <my-button @on-tap="() => viewItem(idPath)" class="primary right" label="Agregar Mediciones Técnicas"/>
  </div>
 
  <div v-for="value, index in techMeasurement">
  <display-row > 
      <prop-value class="prop"  label="id" :value="techMeasurement[index].id"/>
      <prop-value class="prop"  label="Fecha y hora" :value=" techMeasurement[index].fecha + ' ' + techMeasurement[index].hora"/>
      <prop-value class="prop"  label="Area" :value=" techMeasurement[index].area"/>
    

  </display-row>
  <display-row > 
      <prop-value class="prop"  label="Frecuencia Caracteristica" :value=" techMeasurement[index].frecuenciaCaract"/>
      <prop-value class="prop"  label="Unidad" :value=" techMeasurement[index].unidadFC"/>
      <prop-value class="prop"  label="Distancia" :value=" techMeasurement[index].distancia"/>
      <prop-value class="prop"  label="Azimut" :value=" techMeasurement[index].azimut"/>
      <prop-value class="prop"  label="MIC" :value=" techMeasurement[index].mic"/>
      <prop-value class="prop"  label="Clase de Emision" :value=" techMeasurement[index].claseEmision"/>
      <prop-value class="prop"  label="Ancho de Banda" :value=" techMeasurement[index].anchoBanda"/>
      <prop-value class="prop"  label="Unidad" :value=" techMeasurement[index].unidad"/>
    </display-row>
  <display-row > 
      <prop-value class="prop"  label="No esencial 1" :value=" techMeasurement[index].noEsencial1"/>
      <prop-value class="prop"  label="MIC no esencial 1" :value=" techMeasurement[index].micNoEsencial1"/>
      <prop-value class="prop"  label="No esencial 2" :value=" techMeasurement[index].noEsencial2"/>
      <prop-value class="prop"  label="MIC no esencial 2" :value=" techMeasurement[index].micNoEsencial2"/>
      <prop-value class="prop"  label="No esencial 3" :value=" techMeasurement[index].noEsencial3"/>
      <prop-value class="prop"  label="MIC no esencial 3" :value=" techMeasurement[index].micNoEsencial3"/>
  </display-row>
  <display-row > 
      <prop-value class="prop" v-for="value, index in technicians" label="Técnico" :value=" technicians[index].nombre + ', ' + technicians[index].apellido"/>
  </display-row>

</div>  
<div class="buttons-container">
  <!-- <RouterLink :to="'/file/'+ idPath">Volver</RouterLink> -->
  <my-button @on-tap="goBack(idPath)" class="primary right" label="Volver"/>
</div>
</template>

<style scoped>
.status{
    background-color: lightyellow;
}
.prop {
    flex-grow: 1;
    align-items: center;
  }
.buttons-container {
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: end;
    margin: 5px;
}
</style>