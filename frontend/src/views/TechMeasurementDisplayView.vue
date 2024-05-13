<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import DisplayRow from '../components/DisplayRow.vue';
import PropValue from '../components/PropValue.vue';
import { useTerritory } from '../composables/territory';


const { getFile, getTechMeasurement } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()
const { getNameByCode } = useTerritory()


function viewItem(item) { 
  router.push(`/file/${item}/create_tech_measurement`)
}

function goBack() {  
  router.back()
}

const file = reactive({})
const techMeasurement = reactive({})
const technicians = reactive({})
const idPath = ref(currentRoute.value.params.id)


onBeforeMount(async () => {
    const id = currentRoute.value.params.id
    const response = await getTechMeasurement(id)
    const fileResponse = await getFile(currentRoute.value.params.id)
    Object.assign(file, fileResponse.file)
    Object.assign(technicians, response.technicians)
    Object.assign(techMeasurement, response.techMeasurement)    
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
  <div>
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
    </display-row>
  </div>
  <br>
  <div class="buttons-container">
    <my-button
      class="primary right"
      label="Agregar Mediciones Técnicas"
      @on-tap="() => viewItem(idPath)"
    />
  </div>
  <div
    v-for="value, index in techMeasurement"
    :key="value"
  >
    <p
      v-if="index==0"
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
    <br>
    <p class="title-techMeasurements">
      Mediciones Técnicas Externas
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
        class="prop"
        label="Descripción"
        :value=" techMeasurement[index].puntoMedicion"
      />
    </display-row>
    <display-row> 
      <prop-value
        class="prop"
        label="Frecuencia Medida"
        :value=" techMeasurement[index].frecMedida"
      />
      <prop-value
        class="prop"
        label="Unidad"
        :value=" techMeasurement[index].unidadFrecMedida"
      />
      <prop-value
        class="prop"
        label="Ancho de Banda"
        :value=" techMeasurement[index].anchoBanda"
      />
      <prop-value
        class="prop"
        label="Unidad"
        :value=" techMeasurement[index].unidadBW"
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
        label="Observaciones"
        :value=" techMeasurement[index].observaciones"
      />
    </display-row>
    <display-row> 
      <prop-value
        class="prop"
        label="E medido (dBuV/m)"
        :value=" techMeasurement[index].eMedido"
      />
      <prop-value
        class="prop"
        label="E testigo (dBuV/m)"
        :value=" techMeasurement[index].eTestigo"
      />
      <prop-value
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
  </div>  
  <div class="buttons-container">
    <my-button
      class="primary right"
      label="Volver"
      @on-tap="goBack()"
    />
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

</style>