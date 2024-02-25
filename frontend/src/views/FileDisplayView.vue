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
import MyButton from '../components/MyButton.vue'



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
  // Ahora se puede navegar a la nueva ruta y pasar la ruta actual como un parámetro de consulta
  router.push({ path: '/file/create', query: { from: currentPath.value } })
}

function viewItem(item) {  
  router.push(`/file/${item}/tech_measurement`)
}
function editItem(item) {  
  // router.push(`/file/${item}/edit`)
  router.push({ name: 'editFile', params: { id: item } })

}
function goBack() {  
  // router.push(`/list`)
  router.push({ name: 'list', query: { includeDeleted: 'false' }})

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
console.log(file)

    station.provincia = getNameByCode("province", response.station.provincia)
    station.localidad = getNameByCode("city", response.station.localidad)    
})


</script>
<template>
  <div class="buttons-container">
    <my-button @on-tap="goBack" class="primary right" label="Volver" />
    <!-- <my-button @on-tap="() => editItem(file.id)" label="Editar"/> -->
  </div>

  <heading>Radiolocalización de Estaciones</heading>

  <div class="buttons-container">
    <!-- <RouterLink class="tab" :to="'/file/'+ file.id +'/create_tech_measurement'">Agregar Mediciones Técnicas</RouterLink> -->
    <!-- <RouterLink class="tab" :to="'/file/'+ file.id +'/tech_measurement'">Ver Mediciones Técnicas</RouterLink> -->
    <my-button @on-tap="() => viewItem(file.id)" class="secondary right" label="Mediciones Técnicas"/>
    <my-button @on-tap="redirectToCreate" v-if="station.emplazamiento == ('PLANTA TRANSMISORA' || 'Planta Transmisora')" class="secondary right" label="Agregar Estudio"/>
    <!-- <a class="tab" @click="redirectToCreate" v-if="station.emplazamiento == 'PLANTA TRANSMISORA'">Agregar Estudio</a> -->
  </div>
  <div class="container">
    <display-row> 
      <prop-value class="prop" label="id" :value="file.id"/>
      <prop-value class="prop double" label="Expediente" :value="file.expediente"/>
      <prop-value class="prop" label="CCTE/Área" :value="file.area"/>
      <prop-value class="prop" label="Fecha y hora" :value="file.fecha +' '+ file.hora"/>
    </display-row>
    <display-row>
      <prop-value class="prop double" label="Identificación" :value="station.identificacion"/>
      <prop-value class="prop" label="Frecuencia" :value="station.frecuencia +' '+ station.unidad"/>
      <prop-value class="prop" label="Clase de Emisión" :value="station.claseEmision"/>
      <prop-value class="prop" label="Servicio" :value="station.servicio"/>
      <prop-value class="prop" label="Emplazamiento" :value="station.emplazamiento"/>
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
      <prop-value class="prop" label="Altura [m]" :value="station.altura"/>
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
      <prop-value class="prop" v-if="station.observaciones" label="Observaciones" :value="station.observaciones"/>
      <prop-value class="prop" v-else label="Observaciones" value="---"/>


    </display-row>
    <mapa class="mapa" v-if="station.latitud" :position="[ station.latitud, station.longitud ]" />

    <display-row>
      <prop-value class="prop technicians" v-for="value, index in technicians" label="Técnico" :value=" technicians[index].apellido + ', ' + technicians[index].nombre"/>

    </display-row>
    <!-- <display-row> -->
      <prop-value class="prop status" label="Status" :value="file.status"/>

    <!-- </display-row> -->



  </div>
  <div class="buttons-container">
    <my-button @on-tap="() => editItem(file.id)" class="tertiary right" label="Editar"/>
    <my-button @on-tap="goBack" class="primary right" label="Volver"/>
  </div>

</template>

<style scoped>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.status{
    background-color: lightyellow;
}
.prop:hover {
  background-color: #bdc0c2;
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

.buttons-container {
  display: flex;
  flex-direction: row;
  gap: 10px;
  justify-content: end;
  margin: 5px;
}

.status {
  align-self: flex-start;
}
</style>