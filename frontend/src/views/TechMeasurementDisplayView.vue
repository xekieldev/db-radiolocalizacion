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
    console.log(techMeasurement)
    console.log("TechMeasurement: ", response.techMeasurement)
    console.log("file-id: ", file.id)
    console.log("technicians: ", technicians)
    
    
})

function getTechnician(id) {
  console.log("id: ", id, "id_technician1: ",techMeasurement[id].id_technician1,"id_technician2: ", techMeasurement[id].id_technician2)
  const technician1 = technicians[techMeasurement[id].id_technician1-1].nombre + ', ' + technicians[techMeasurement[id].id_technician1-1].apellido
  const technician2 = technicians[techMeasurement[id].id_technician2-1].nombre + ', ' + technicians[techMeasurement[id].id_technician2-1].apellido
  
  // debugger
  return [technician1, technician2]
}
// function getTechnician2(id) {

//   return technicians[techMeasurement[id].id_technician2].nombre + ', ' + technicians[techMeasurement[id].id_technician2].apellido
// }



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
    <p v-if="index==0">Emplazamiento Estación Testigo </p>
    <display-row v-if="index==0"> 
      <prop-value class="prop double" label="Domicilio" :value="techMeasurement[index].domicilioTestigo"/>
      <prop-value class="prop double" label="Localidad" :value="techMeasurement[index].localidadTestigo"/>
      <prop-value class="prop double" label="Provincia" :value="techMeasurement[index].provinciaTestigo"/>
    </display-row>
    <display-row v-if="index==0">
      <prop-value class="prop"  label="Latitud" :value="techMeasurement[index].latitudTestigo"/>
      <prop-value class="prop"  label="Longitud" :value="techMeasurement[index].longitudTestigo"/>
      <prop-value class="prop"  label="Distancia" :value=" techMeasurement[index].distanciaTestigo"/>
      <prop-value class="prop double" label="Azimut geog. con respecto a PTx" :value="techMeasurement[index].azimutTestigo"/>
    </display-row>
<br>
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
      <prop-value class="prop"  label="Distancia" :value=" techMeasurement[index].distancia"/>
      <prop-value class="prop"  label="Azimut" :value=" techMeasurement[index].azimut"/>
    </display-row>
    <display-row > 
      <prop-value class="prop double" label="Domicilio" :value="techMeasurement[index].domicilio"/>
      <prop-value class="prop double" label="Localidad" :value="techMeasurement[index].localidad"/>
      <prop-value class="prop double" label="Provincia" :value="techMeasurement[index].provincia"/>
    </display-row>
    <display-row > 
      <prop-value class="prop"  label="E medido (dBuV/m)" :value=" techMeasurement[index].eMedido"/>
      <prop-value class="prop"  label="E testigo (dBuV/m)" :value=" techMeasurement[index].eTestigo"/>
      <prop-value class="prop"  label="E corregido (dBuV/m)" :value=" techMeasurement[index].eCorregido"/>
      <prop-value class="prop"  label="Incertidumbre (dB)" :value=" techMeasurement[index].incertidumbre"/>
    </display-row>
    <display-row >
      <prop-value class="prop"  label="Resultado Comprobaciones Técnicas" :value=" techMeasurement[index].resultadoComprob"/>

    </display-row>
        <!-- <prop-value class="prop"  label="No esencial 1" :value=" techMeasurement[index].noEsencial1"/>
        <prop-value class="prop"  label="MIC no esencial 1" :value=" techMeasurement[index].micNoEsencial1"/>
        <prop-value class="prop"  label="No esencial 2" :value=" techMeasurement[index].noEsencial2"/>
        <prop-value class="prop"  label="MIC no esencial 2" :value=" techMeasurement[index].micNoEsencial2"/>
        <prop-value class="prop"  label="No esencial 3" :value=" techMeasurement[index].noEsencial3"/>
        <prop-value class="prop"  label="MIC no esencial 3" :value=" techMeasurement[index].micNoEsencial3"/> -->
    <!-- </display-row> -->
    <display-row > 
        <!-- <prop-value class="prop" label="Técnico" :value="technicians[techMeasurement[index].id_technician1].nombre + ', ' + technicians[techMeasurement[index].id_technician1].apellido"/> -->
        <!-- <prop-value class="prop" label="Técnico" :value="technicians[techMeasurement[index].id_technician2].nombre + ', ' + technicians[techMeasurement[index].id_technician2].apellido"/> -->
      <prop-value class="prop"  label="Técnico1" :value="getTechnician(index)[0]"/>
      <prop-value class="prop"  label="Técnico2" :value="getTechnician(index)[1]"/>

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