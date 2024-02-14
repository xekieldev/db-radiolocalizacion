<script setup>
// import { useLocalStorage } from '../composables/localstorage'
import { useApi } from '../composables/api'
import { onMounted, reactive, ref } from 'vue'
import { RouterLink, useRouter , useRoute} from 'vue-router'
import { useTerritory } from '../composables/territory'
import Mapa from '../components/MapMain.vue'
import DisplayRow from '../components/DisplayRow.vue'
import PropValue from '../components/PropValue.vue'
import Heading from '../components/Heading.vue'



// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getFile, loading, getAllTechnicians } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()
const { getNameByCode } = useTerritory()


const currentPath = ref('')

const redirectToCreate = () => {
  // console.log("currentPath.value: ", router.currentRoute.value.path)

  currentPath.value = router.currentRoute.value.path

  

  // Ahora puedes navegar a la nueva ruta y pasar la ruta actual como un parámetro de consulta
  router.push({ path: '/file/create', query: { from: currentPath.value } })
}





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
// const currentPath = this.$route.fullPath;

onMounted(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const response = await getFile(currentRoute.value.params.id)
    const techResponse = await getAllTechnicians()

    Object.assign(file, response.file)
    Object.assign(station, response.station)
    Object.assign(technicians, response.technicians)
    Object.assign(techniciansValues, techResponse)
console.log(technicians)

    station.provincia = getNameByCode("province", response.station.provincia)
    station.localidad = getNameByCode("city", response.station.localidad)    
})


</script>
<template>
  <div class="tab-container">
    <RouterLink class="tab" :to="'/file/'+ file.id +'/create_tech_measurement'">Agregar Mediciones Técnicas</RouterLink>
    <RouterLink class="tab" :to="'/file/'+ file.id +'/tech_measurement'">Ver Mediciones Técnicas</RouterLink>
    <a class="tab" @click="redirectToCreate" v-if="station.emplazamiento == 'PLANTA TRANSMISORA'">Agregar Estudio</a>
  </div>
  <br>
  <div class="container">
    <heading>Radiolocalización de Estaciones</heading> <br>
    <display-row> 
      <prop-value class="prop double" label="Expediente" :value="file.expediente"/>
      <prop-value class="prop" label="Area" :value="file.area"/>
      <prop-value class="prop" label="Fecha y hora" :value="file.fecha +' '+ file.hora"/>
      
      <!-- <prop-value class="prop" label="Expediente" :value="station.expediente"/>
      <prop-value class="prop" label="Expediente" :value="station.expediente"/>
      <prop-value class="prop" label="Expediente" :value="station.expediente"/> -->
    </display-row>
    <display-row>
      <prop-value class="prop double" label="Identificación" :value="station.identificacion"/>
      <prop-value class="prop" label="Frecuencia" :value="station.frecuencia +' '+ station.unidad"/>
      <prop-value class="prop" label="Clase de Emision" :value="station.claseEmision"/>
      <prop-value class="prop" label="Servicio" :value="station.servicio"/>
    </display-row>
    <display-row>
      <prop-value class="prop double" label="Domicilio" :value="station.domicilio"/>
      <prop-value class="prop double" label="Localidad" :value="station.localidad"/>
      <prop-value class="prop double" label="Provincia" :value="station.provincia"/>
      <prop-value class="prop" label="Latitud" :value="station.latitud"/>
      <prop-value class="prop" label="Longitud" :value="station.longitud"/>
    </display-row>
    <display-row>
      <prop-value class="prop" label="Sistema Irradiante" :value="station.irradiante"/>
      <prop-value class="prop" label="Cantidad" :value="station.cantidad"/>
      <prop-value class="prop" label="Polarización" :value="station.polarizacion"/>
      <prop-value class="prop" label="Altura" :value="station.altura"/>
    </display-row>
    <display-row>
      <prop-value class="prop" label="Vínculo" :value="station.tipoVinculo"/>
      <prop-value class="prop" v-if="station.frecuenciaVinc" label="Frecuencia" :value="station.frecuenciaVinc +' '+ station.unidadVinc"/>
      <prop-value class="prop" v-else label="Frecuencia" value="---"/>
      <prop-value class="prop" v-if="station.irradianteVinc" label="Sistema Irradiante" :value="station.irradianteVinc"/>
      <prop-value class="prop" v-else label="Sistema Irradiante" value="---"/>
      <prop-value class="prop" v-if="station.irradianteVinc" label="Polarización" :value="station.polarizacionVinc"/>
      <prop-value class="prop" v-else label="Polarización" value="---"/>


    </display-row>
    <display-row>
      <prop-value class="prop" label="Observaciones" :value="station.observaciones"/>

    </display-row>
    <mapa class="mapa" v-if="station.latitud" :position="[ station.latitud, station.longitud ]" />

    <display-row>
      <prop-value class="prop technicians" v-for="value, index in technicians" label="Técnico" :value=" technicians[index].apellido + ', ' + technicians[index].nombre"/>

    </display-row>



  </div>

  <RouterLink to="/list">Volver</RouterLink>
  <RouterLink :to="'/file/'+file.id+'/edit'">Editar</RouterLink>
</template>

<style scoped>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  
  /* border: solid; */
}

.status{
    background-color: lightyellow;
}

.tab-container {
  display: flex;
  width: 500px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  margin-left: 46%;
}
.tab {
  flex: 1;
  text-align: center;
  padding: 5px 20px;
  border: 1px solid #ccc;
  border-bottom: none; 
  border-radius: 5px 5px 0 0;
  background-color: #f2f2f2;
  text-decoration: none;
  color: #333;
  position: relative; 
  z-index: 1; 
}

.prop:hover {
  background-color: #e0e0e0;
}

.tab:before {
  content: ''; 
  position: absolute;
  top: 100%; 
  left: 0;
  width: 100%;
  height: 5px; 
  background-color: rgba(0, 0, 0, 0.1); 
  z-index: -1; 
  border-radius: 5px 5px 0 0; 
}

.prop{
  flex-grow: 1;
  border-radius: 10px 0 0;
}
.prop.double{
  flex-grow: 4;
}
.technicians{
  border-bottom: 1px solid #cbcdce;
}
</style>