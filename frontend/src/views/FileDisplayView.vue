<script setup>
import { useApi } from '../composables/api'
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useTerritory } from '../composables/territory'
import Mapa from '../components/MapMain.vue'
import DisplayRow from '../components/DisplayRow.vue'
import PropValue from '../components/PropValue.vue'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'


const { getFile, loading, getAllTechnicians } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()
const { getNameByCode } = useTerritory()


const currentPath = ref('')

const redirectToCreate = () => {
  currentPath.value = router.currentRoute.value.path
  if (station.tipoVinculo == 'Radioeléctrico' || station.tipoVinculo == 'RADIOELÉCTRICO') {
    router.push({ path: '/file/create', query: { rloc: 'true', from: currentPath.value } })
  } else {
    router.push({ path: '/file/create', query: { rloc: 'false', from: currentPath.value } })

  }
}

function viewItem(item) {  
  router.push({name: 'tech_measurement', params: { id: item}})
}
function editItem(item) {  

  if (station.frecuencia != null || station.frecuencia != undefined) {
    router.currentRoute.value.query.rloc = 'true'
    router.push({ name: 'editFile', params: { id: item }, query: { rloc: 'true'} })

  } else {
    router.currentRoute.value.query.rloc = 'false'
    router.push({ name: 'editFile', params: { id: item }, query: { rloc: 'false'} })

  }
}
function goBack() {  
  router.back()

}

const file = reactive({})
const station = reactive({})
const technicians = reactive({})
const techniciansValues = reactive({})

onMounted(async () => {
    const response = await getFile(currentRoute.value.params.id)
    const techResponse = await getAllTechnicians()
    Object.assign(file, response.file)
    Object.assign(station, response.station)
    Object.assign(technicians, response.technicians)
    Object.assign(techniciansValues, techResponse)
    station.provincia = getNameByCode("province", response.station.provincia)
    station.localidad = getNameByCode("city", response.station.localidad)    
})


</script>
<template>
  <div class="buttons-container">
    <my-button @on-tap="goBack" class="primary right" label="Volver" />
  </div>

  <heading v-if="station.frecuencia != null">Datos de Radiolocalización</heading>
  <heading v-else>Datos de Localización</heading>

  <div class="buttons-container">
    <my-button @on-tap="() => viewItem(file.id)" class="secondary right" label="Mediciones Técnicas"/>
    <my-button @on-tap="redirectToCreate" v-if="station.emplazamiento == 'PLANTA TRANSMISORA' || station.emplazamiento == 'Planta Transmisora'" class="secondary right" label="Agregar Estudio"/>
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
      <prop-value v-if="station.frecuencia" class="prop" label="Frecuencia" :value="station.frecuencia +' '+ station.unidad"/>
      <prop-value v-if="station.frecuencia" class="prop" label="Clase de Emisión" :value="station.claseEmision"/>
      <prop-value v-if="station.frecuencia" class="prop" label="Servicio" :value="station.servicio"/>
      <prop-value class="prop" label="Emplazamiento" :value="station.emplazamiento"/>
    </display-row>
    <display-row>
      <prop-value class="prop double" label="Domicilio" :value="station.domicilio"/>
      <prop-value class="prop double" label="Localidad" :value="station.localidad"/>
      <prop-value class="prop double" label="Provincia" :value="station.provincia"/>
      <prop-value class="prop" label="Latitud" :value="station.latitud"/>
      <prop-value class="prop" label="Longitud" :value="station.longitud"/>
    </display-row>
    <display-row v-if="station.frecuencia" >
      <prop-value class="prop" label="Sistema Irradiante" :value="station.irradiante"/>
      <prop-value class="prop" label="Cantidad" :value="station.cantidad"/>
      <prop-value class="prop" label="Polarización" :value="station.polarizacion"/>
      <prop-value class="prop" label="Altura [m]" :value="station.altura"/>
    </display-row>
    <display-row v-if="station.frecuencia" >
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
    <prop-value class="prop status" label="Status" :value="file.status"/>
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