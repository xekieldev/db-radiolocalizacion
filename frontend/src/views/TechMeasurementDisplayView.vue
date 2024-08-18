<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive, ref, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'
import DisplayRow from '../components/DisplayRow.vue'
import PropValue from '../components/PropValue.vue'
import { useTerritory } from '../composables/territory'


const { getTechMeasurement, getStation, delete_tech_measurement, getFile } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()
const { getNameByCode } = useTerritory()

const file = reactive({})
const station = reactive({})
const techMeasurement = reactive({})
const technicians = reactive({})
const idPath = ref(currentRoute.value.params.id)
let previewStatus = ref(false)


onBeforeMount(async () => {
  const id = currentRoute.value.params.id
  const file_id = currentRoute.value.params.file_id
  const stationResponse = await getStation(currentRoute.value.params.id)
  Object.assign(station, stationResponse.station)
  const file_response = await getFile(station.file_id)   
  Object.assign(file, file_response.file) 
    
  if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
    const response = await getTechMeasurement(file_id, id)
    Object.assign(techMeasurement, response.techMeasurement)
    Object.assign(technicians, response.technicians)

  } else {
      const response = await getTechMeasurement(file_id, id, true)
      Object.assign(techMeasurement, response.techMeasurement)
      Object.assign(technicians, response.technicians)
  }    
})

function viewItem(file_id, id) { 
  router.push(`/file/${file_id}/station/${id}/create_tech_measurement`)
}

function goBack() {  
  router.back()
}

function getTechnician(id) {
  for (const key in technicians) {
    if (technicians[key].id === id) {
      return technicians[key].nombre + ', ' + technicians[key].apellido
    }
  }
  return ''
}

async function del_tech_measurement(id, id_tech_measurement) {
    try { 
      await delete_tech_measurement(id, id_tech_measurement)
      window.location.reload() 

    } catch (error) {
    console.error(error)
    } 
  }

  function print() {  
  previewStatus.value = true
  if(previewStatus.value){
    nextTick(() => {
      window.print()
      previewStatus.value = false
    })
  }
}

</script>

<template>
  <div class="buttons-container">
    <my-button
      v-if="!previewStatus"
      class="quinary right"
      label="Imprimir"
      @on-tap="print"
    />
    <my-button
      v-if="!previewStatus"
      class="primary right"
      label="Agregar punto de medición"
      @on-tap="() => viewItem(station.file_id, idPath)"
    />
  </div>
  <heading>Comprobaciones Técnicas Externas</heading>
  <div class="reference-group">
    <display-row> 
      <prop-value
        class="prop"
        label="id"
        :value="station.id"
      />
      <prop-value
        class="prop double"
        label="Expediente"
        :value="file.expediente"
      />
      <prop-value
        class="prop"
        label="CCTE/Área"
        :value="station.area"
      />
    </display-row>
    <display-row>
      <prop-value
        class="prop"
        label="Identificación"
        :value="station.identificacion"
      />
      <prop-value
        v-if="station.frecuencia === null || station.frecuencia === undefined"
        class="prop"
        label="Frecuencia"
        value="---"
      />
      <prop-value
        v-else
        class="prop"
        label="Frecuencia"
        :value="station.frecuencia +' '+ station.unidad"
      />
    </display-row>
  </div>
  <br>
  <div
    v-for="value, index in techMeasurement"
    :key="value"
  >
    <div
      v-if="index==0 && techMeasurement && techMeasurement[0].domicilioTestigo != null"
      class="testigo-group"
    >
      <p
        class="title-testigo"
      >
        Emplazamiento Estación Testigo
      </p>
      <display-row v-if="index==0"> 
        <prop-value
          class="prop double"
          label="Domicilio"
          :value="techMeasurement[index].domicilioTestigo"
        />
        <prop-value
          class="prop double"
          label="Localidad"
          :value="getNameByCode('city', techMeasurement[index].localidadTestigo)"
        />
        <prop-value
          class="prop double"
          label="Provincia"
          :value="getNameByCode('province', techMeasurement[index].provinciaTestigo)"
        />
      </display-row>
      <display-row v-if="index==0">
        <prop-value
          class="prop"
          label="Latitud"
          :value="techMeasurement[index].latitudTestigo"
        />
        <prop-value
          class="prop"
          label="Longitud"
          :value="techMeasurement[index].longitudTestigo"
        />
        <prop-value
          class="prop"
          label="Distancia [m]"
          :value=" techMeasurement[index].distanciaTestigo"
        />
        <prop-value
          class="prop double"
          label="Azimut geog. con respecto a PTx [°]"
          :value="techMeasurement[index].azimutTestigo"
        />
      </display-row>
    </div>
    <br>
    <div class="measurement-point-group">
      <p class="title-techMeasurements">
        Punto de medición técnica
      </p>
      <display-row> 
        <prop-value
          class="prop"
          label="id"
          :value="techMeasurement[index].id"
        />
        <prop-value
          class="prop"
          label="Fecha y hora"
          :value=" techMeasurement[index].fecha + ' ' + techMeasurement[index].hora"
        />
        <prop-value
          class="prop double"
          label="Descripción"
          :value=" techMeasurement[index].puntoMedicion"
        />
      </display-row>
      <display-row> 
        <prop-value
          class="prop double"
          label="Domicilio"
          :value="techMeasurement[index].domicilio"
        />
        <prop-value
          class="prop double"
          label="Localidad"
          :value="getNameByCode('city', techMeasurement[index].localidad)"
        />
        <prop-value
          class="prop double"
          label="Provincia"
          :value="getNameByCode('province', techMeasurement[index].provincia)"
        />
      </display-row>
      <display-row> 
        <prop-value
          class="prop"
          label="Latitud"
          :value="techMeasurement[index].latitud"
        />
        <prop-value
          class="prop"
          label="Longitud"
          :value="techMeasurement[index].longitud"
        />
        <prop-value
          class="prop"
          label="Distancia [m]"
          :value=" techMeasurement[index].distancia"
        />
        <prop-value
          class="prop"
          label="Azimut [°]"
          :value=" techMeasurement[index].azimut"
        />
      </display-row>
      <display-row>
        <prop-value
          class="prop"
          label="Observaciones"
          :value=" techMeasurement[index].observaciones"
        />
      </display-row>
      <display-row> 
        <prop-value
          class="prop"
          label="Frecuencia Medida"
          :value=" techMeasurement[index].frecMedida +' '+ techMeasurement[index].unidadFrecMedida"
        />
        <prop-value
          class="prop"
          label="Ancho de Banda"
          :value=" techMeasurement[index].anchoBanda +' '+ techMeasurement[index].unidadBW"
        />
      </display-row>
      <display-row> 
        <prop-value
          class="prop"
          label="E medido (dBuV/m)"
          :value=" techMeasurement[index].eMedido"
        />
        <prop-value
          v-if="techMeasurement && techMeasurement[0].domicilioTestigo != null"
          class="prop"
          label="E testigo (dBuV/m)"
          :value=" techMeasurement[index].eTestigo"
        />
        <prop-value
          v-if="techMeasurement && techMeasurement[0].domicilioTestigo != null"
          class="prop"
          label="E corregido (dBuV/m)"
          :value=" techMeasurement[index].eCorregido"
        />
        <prop-value
          class="prop"
          label="Incertidumbre (dB)"
          :value=" techMeasurement[index].incertidumbre"
        />
      </display-row>
      <display-row>
        <prop-value
          class="prop"
          label="Equipamiento utilizado"
          :value=" techMeasurement[index].equipamiento"
        />
      </display-row>
      <display-row>
        <prop-value
          class="prop"
          label="Resultado de las Comprobaciones Técnicas"
          :value=" techMeasurement[index].resultadoComprob"
        />
      </display-row>
      <display-row> 
        <prop-value
          class="prop"
          label="Técnico 1"
          :value="getTechnician(techMeasurement[index].id_technician1)"
        />
        <prop-value
          class="prop"
          label="Técnico 2"
          :value="getTechnician(techMeasurement[index].id_technician2)"
        />
      </display-row>
      <display-row class="status-container">
        <prop-value
          v-if="!previewStatus"
          class="prop status"
          label="Status"
          :value=" techMeasurement[index].status"
        />
      </display-row>
      <div class="buttons-container delete-btn">
        <my-button
          v-if="!previewStatus"
          class="tertiary right"
          label="Borrar"
          @on-tap="() => del_tech_measurement(idPath, techMeasurement[index].id)"
        />
      </div>
    </div>
  </div>  
  <div class="buttons-container">
    <my-button
      v-if="!previewStatus"
      class="primary right"
      label="Volver"
      @on-tap="goBack()"
    />
  </div>
  <div
    v-if="previewStatus"
    class="preview-header"
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
.status{
    background-color: lightyellow;
}
.prop {
    flex-grow: 1;
    align-items: center;
}
.prop.double{
  flex-grow: 4;
}
.buttons-container {
    display: flex;
    flex-direction: row;
    gap: 10px;
    justify-content: end;
    margin: 5px;
    padding-bottom: 5px;
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
.reference-group {
  padding-bottom: 10px;;
  border-bottom: solid 1px lightblue;
  /* text-transform: uppercase; */
}
.testigo-group {
  padding-bottom: 10px;;
  border-bottom: solid 1px lightblue;
  /* text-transform: uppercase; */
}
.status {
  flex: 0 0 15%;
}
.status-container {
  justify-content: left;
}
.delete-btn {
  border-bottom: 1px solid lightblue;
}
.preview-header {
  display: flex;
  position: absolute;
  background: linear-gradient(to right, white 0%, #cacaca 25%, #cacaca 75%, white 100%);
  width: 100%;
  justify-content: space-between;
  align-items: baseline;
}
.back-preview-button {
  align-self: center;
}

</style>