<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive, ref, watch, nextTick } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useTerritory } from '../composables/territory'
import Mapa from '../components/MapMain.vue'
import DisplayRow from '../components/DisplayRow.vue'
import PropValue from '../components/PropValue.vue'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'


const { getFile, getAllTechnicians } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()
const route = useRoute()
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
const printFlag = reactive({isActive: false})

onBeforeMount(async () => {
    const response = await getFile(currentRoute.value.params.id)
    const techResponse = await getAllTechnicians()
    Object.assign(file, response.file)
    Object.assign(station, response.station)
    Object.assign(technicians, response.technicians)
    Object.assign(techniciansValues, techResponse)
    station.provincia = getNameByCode("province", response.station.provincia)
    station.localidad = getNameByCode("city", response.station.localidad)    
})

function print() {
  printFlag.isActive = true
  nextTick(() => {
    // Usa un bucle para verificar el estado del DOM hasta que esté listo
    const checkDomReady = setInterval(() => {
      if (document.querySelector('.print-header')) {
        clearInterval(checkDomReady)
        window.print()        
        printFlag.isActive = false
      }
    }, 200) // Verificar cada 100 ms
  })
}

function viewRelatedStation(item) {
  router.push(`/file/${item}`)
}

watch(
  () => route.params.id,
  async newId => {
    const response = await getFile(newId)
    Object.assign(file, response.file)
    Object.assign(station, response.station)
    Object.assign(technicians, response.technicians)
    station.provincia = getNameByCode("province", response.station.provincia)
    station.localidad = getNameByCode("city", response.station.localidad)

    
  }
)

</script>
<template>
  <div class="buttons-container">
    <my-button
      v-if="!printFlag.isActive"
      class="quinary right"
      label="Imprimir"
      @on-tap="print"
    />
    <my-button
      v-if="!printFlag.isActive"
      class="primary right"
      label="Volver"
      @on-tap="goBack"
    />
  </div>

  <heading v-if="station.frecuencia != null">
    Datos de Radiolocalización
  </heading>
  <heading v-else>
    Datos de Localización
  </heading>

  <div class="buttons-container">
    <div
      v-if="typeof station.related_station_id !== 'undefined' && station.related_station_id !== null && station.related_station_id !== '' && !printFlag.isActive"
      class="related-station-container"
    >
      <my-button
        class="primary"
        :label="(station.id).toString()"
      />
      <img
        src="../../img/flecha-doble.png"
        class="related-arrow"
        title="Estaciones relacionadas"
      >
      <my-button
        class="secondary"
        :label="(station.related_station_id).toString()"
        @on-tap="viewRelatedStation(station.related_station_id)"
      />
    </div>
    <div class="more-buttons">
      <my-button
        v-if="!printFlag.isActive"
        class="secondary right"
        label="Mediciones Técnicas"
        @on-tap="() => viewItem(file.id)"
      />
      <my-button
        v-if="station.emplazamiento == 'PLANTA TRANSMISORA' || station.emplazamiento == 'Planta Transmisora' && !printFlag.isActive"
        class="secondary right"
        label="Agregar Estudio"
        @on-tap="redirectToCreate"
      />      
    </div>
  </div>
  <div class="container">
    <display-row> 
      <prop-value
        class="prop"
        label="id"
        :value="file.id"
      />
      <prop-value
        class="prop double"
        label="Expediente"
        :value="file.expediente"
      />
      <prop-value
        class="prop"
        label="CCTE/Área"
        :value="file.area"
      />
      <prop-value
        class="prop"
        label="Fecha y hora"
        :value="file.fecha +' '+ file.hora"
      />
    </display-row>
    <display-row>
      <prop-value
        class="prop double"
        label="Identificación"
        :value="station.identificacion"
      />
      <prop-value
        v-if="station.frecuencia"
        class="prop"
        label="Frecuencia"
        :value="station.frecuencia +' '+ station.unidad"
      />
      <prop-value
        v-if="station.frecuencia"
        class="prop"
        label="Clase de Emisión"
        :value="station.claseEmision"
      />
      <prop-value
        v-if="station.frecuencia"
        class="prop"
        label="Servicio"
        :value="station.servicio"
      />
      <prop-value
        class="prop"
        label="Emplazamiento"
        :value="station.emplazamiento"
      />
    </display-row>
    <display-row>
      <prop-value
        class="prop double"
        label="Domicilio"
        :value="station.domicilio"
      />
      <prop-value
        class="prop double"
        label="Localidad"
        :value="station.localidad"
      />
      <prop-value
        class="prop double"
        label="Provincia"
        :value="station.provincia"
      />
      <prop-value
        class="prop"
        label="Latitud"
        :value="station.latitud"
      />
      <prop-value
        class="prop"
        label="Longitud"
        :value="station.longitud"
      />
    </display-row>
    <display-row v-if="station.frecuencia">
      <prop-value
        class="prop"
        label="Sistema Irradiante"
        :value="station.irradiante"
      />
      <prop-value
        class="prop"
        label="Cantidad"
        :value="station.cantidad"
      />
      <prop-value
        class="prop"
        label="Polarización"
        :value="station.polarizacion"
      />
      <prop-value
        class="prop"
        label="Altura [m]"
        :value="station.altura"
      />
    </display-row>
    <display-row v-if="station.frecuencia && station.frecuenciaVinc">
      <prop-value
        class="prop"
        label="Vínculo"
        :value="station.tipoVinculo"
      />
      <prop-value
        v-if="station.frecuenciaVinc"
        class="prop"
        label="Frecuencia"
        :value="station.frecuenciaVinc +' '+ station.unidadVinc"
      />
      <prop-value
        v-else
        class="prop"
        label="Frecuencia"
        value="---"
      />
      <prop-value
        v-if="station.irradianteVinc"
        class="prop"
        label="Sistema Irradiante"
        :value="station.irradianteVinc"
      />
      <prop-value
        v-else
        class="prop"
        label="Sistema Irradiante"
        value="---"
      />
      <prop-value
        v-if="station.irradianteVinc"
        class="prop"
        label="Polarización"
        :value="station.polarizacionVinc"
      />
      <prop-value
        v-else
        class="prop"
        label="Polarización"
        value="---"
      />
    </display-row>
    <display-row>
      <prop-value
        v-if="station.observaciones"
        class="prop"
        label="Observaciones"
        :value="station.observaciones"
      />
      <prop-value
        v-else
        class="prop"
        label="Observaciones"
        value="---"
      />
    </display-row>
    <mapa
      v-if="station.latitud"
      class="mapa"
      :position="[ station.latitud, station.longitud ]"
    />
    <display-row>
      <prop-value
        v-for="value, index in technicians"
        :key="value"
        class="prop technicians"
        label="Técnico"
        :value=" technicians[index].apellido + ', ' + technicians[index].nombre"
      />
    </display-row>
    <prop-value
      v-if="!printFlag.isActive"
      class="prop status"
      label="Status"
      :value="file.status"
    />
  </div>
  <div
    v-if="!printFlag.isActive"
    class="buttons-container"
  >
    <my-button
      class="tertiary right"
      label="Editar"
      @on-tap="() => editItem(file.id)"
    />
    <my-button
      class="primary right"
      label="Volver"
      @on-tap="goBack"
    />
  </div>
  <div
    v-if="printFlag.isActive"
    class="print-header"
  >
    <img
      alt="ENACOM logo"
      class="logo"
      src="../../img/Logo.png"
      width="100"
      height="100"
    > 
  </div>
</template>

<style scoped>
.print-header {
  display: flex;
  background: linear-gradient(to right, white 0%, #cacaca 25%, #cacaca 75%, white 100%);
  width: 100%;
  justify-content: space-between;
  align-items: baseline;
  position: absolute;
}
.page {
  position: absolute;
  width: 900px;
  display: flex;
  flex-direction: column;
  margin: 0 auto;
}
.print-preview {
  background: white;
  width: 900px;
  height: 1350px;
}
.general-view {
  margin-top: 100px;
}
.preview-title {
  margin: 30px 10px;
}
.back-preview-button {
  align-self: center;
}
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* text-transform: uppercase; */
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
.related-station-container {
  display: flex;
  gap: 5px;
  margin-right: auto;
}
.related-station-container p {
  padding: 5px 5px;
  flex-direction: row;
}
.more-buttons {
  display: flex;
  flex-direction: row;
  gap: 10px;
}

.related-arrow {
  width: 20px;
}
.text-related-stations {
  font-size: 13px;
  font-weight: 500;
}

</style>