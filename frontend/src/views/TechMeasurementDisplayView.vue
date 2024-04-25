<script setup>
import { useApi } from '../composables/api'
import { onMounted, reactive, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import DisplayRow from '../components/DisplayRow.vue';
import PropValue from '../components/PropValue.vue';
import { useTerritory } from '../composables/territory';



// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getFile, getTechMeasurement } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()
const { getNameByCode } = useTerritory()



function viewItem(item) { 
  console.log("Aca!! ", item)
  router.push(`/file/${item}/create_tech_measurement`)
}

function goBack(item) {  
  // router.push(`/file/${item}`)
  // router.go(-1)
  router.back()
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
    // console.log(techMeasurement)
    // console.log("TechMeasurement: ", response.techMeasurement)
    // console.log("file-id: ", file.id)
    console.log("technicians: ", technicians)
    
    techMeasurement[0].provinciaTestigo = getNameByCode("province", response.techMeasurement[0].provinciaTestigo)
    techMeasurement[0].localidadTestigo = getNameByCode("city", response.techMeasurement[0].localidadTestigo)
    console.log("Valor Testigo",techMeasurement[0])
    
})

function getTechnician(id) {
  for (const key in technicians) {
    if (technicians[key].id === id) {
      return technicians[key].nombre + ', ' + technicians[key].apellido
    }
  }
  return ''
}



</script>
<template>
  
  <heading>Mediciones Técnicas Externas</heading>
    <!-- <RouterLink class="tab" :to="'/file/'+ file.id +'/create_tech_measurement'">Agregar Mediciones Técnicas</RouterLink> -->
  
  <div>
    <display-row> 
        <prop-value class="prop" label="id" :value="file.id"/>
        <prop-value class="prop double" label="Expediente" :value="file.expediente"/>
        <prop-value class="prop" label="CCTE/Área" :value="file.area"/>
        <!-- <prop-value class="prop" label="Fecha y hora" :value="file.fecha +' '+ file.hora"/> -->
      </display-row>
  </div>
<br>
<div class="buttons-container" >
    <my-button @on-tap="() => viewItem(idPath)" class="primary right" label="Agregar Mediciones Técnicas"/>
  </div>
  <div v-for="value, index in techMeasurement">
    <p v-if="index==0" class="title-testigo">Emplazamiento Estación Testigo </p>
    <display-row v-if="index==0"> 
      <prop-value class="prop double" label="Domicilio" :value="techMeasurement[index].domicilioTestigo"/>
      <prop-value class="prop double" label="Localidad" :value="techMeasurement[index].localidadTestigo"/>
      <prop-value class="prop double" label="Provincia" :value="techMeasurement[index].provinciaTestigo"/>
    </display-row>
    <display-row v-if="index==0">
      <prop-value class="prop"  label="Latitud" :value="techMeasurement[index].latitudTestigo"/>
      <prop-value class="prop"  label="Longitud" :value="techMeasurement[index].longitudTestigo"/>
      <prop-value class="prop"  label="Distancia [m]" :value=" techMeasurement[index].distanciaTestigo"/>
      <prop-value class="prop double" label="Azimut geog. con respecto a PTx [°]" :value="techMeasurement[index].azimutTestigo"/>
    </display-row>
<br>
<p class="title-techMeasurements">Mediciones Técnicas Externas</p>

    <display-row > 
      <prop-value class="prop"  label="id" :value="techMeasurement[index].id"/>
      <prop-value class="prop"  label="Fecha y hora" :value=" techMeasurement[index].fecha + ' ' + techMeasurement[index].hora"/>
      <prop-value class="prop"  label="Descripción" :value=" techMeasurement[index].puntoMedicion"/>
    </display-row>
    <display-row > 
      <prop-value class="prop"  label="Frecuencia Medida" :value=" techMeasurement[index].frecMedida"/>
      <prop-value class="prop"  label="Unidad" :value=" techMeasurement[index].unidadFrecMedida"/>
      <prop-value class="prop"  label="Ancho de Banda" :value=" techMeasurement[index].anchoBanda"/>
      <prop-value class="prop"  label="Unidad" :value=" techMeasurement[index].unidadBW"/>
    </display-row>
    <display-row > 
      <prop-value class="prop"  label="Latitud" :value="techMeasurement[index].latitud"/>
      <prop-value class="prop"  label="Longitud" :value="techMeasurement[index].longitud"/>
      <prop-value class="prop"  label="Distancia [m]" :value=" techMeasurement[index].distancia"/>
      <prop-value class="prop"  label="Azimut [°]" :value=" techMeasurement[index].azimut"/>
    </display-row>
    <display-row > 
      <prop-value class="prop double" label="Domicilio" :value="techMeasurement[index].domicilio"/>
      <prop-value class="prop double" label="Localidad" :value="getNameByCode('city', techMeasurement[index].localidad)"/>
      <prop-value class="prop double" label="Provincia" :value="getNameByCode('province', techMeasurement[index].provincia)"/>
    </display-row>
    <display-row > 
      <prop-value class="prop"  label="E medido (dBuV/m)" :value=" techMeasurement[index].eMedido"/>
      <prop-value class="prop"  label="E testigo (dBuV/m)" :value=" techMeasurement[index].eTestigo"/>
      <prop-value class="prop"  label="E corregido (dBuV/m)" :value=" techMeasurement[index].eCorregido"/>
      <prop-value class="prop"  label="Incertidumbre (dB)" :value=" techMeasurement[index].incertidumbre"/>
    </display-row>
    <display-row >
      <prop-value class="prop"  label="Resultado de las Comprobaciones Técnicas" :value=" techMeasurement[index].resultadoComprob"/>

    </display-row>

    <display-row> 
      
        <prop-value class="prop" label="Técnico 1" :value="getTechnician(techMeasurement[index].id_technician1)"/>
        <prop-value class="prop" label="Técnico 2" :value="getTechnician(techMeasurement[index].id_technician2)"/>

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
.title-testigo {
  font-weight: 700;
  margin-bottom: 10px;
}
.title-techMeasurements {
  font-weight: 700;
  margin-bottom: 10px;
}
.field-technicians {
  display: inline-flex;
  width: 50%; 
}
/* .tecnico1 {
  margin-right: 2.5px;
}
.tecnico2 {
  margin-left: 2.5px;
} */
</style>