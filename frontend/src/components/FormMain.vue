<script setup>
import FormRow from './FormRow.vue'
import { ref, watch, onMounted } from 'vue'
import { useTerritory } from '../composables/territory'
import { useLink } from '../composables/link'
import { useArea } from '../composables/area'
import { usePolarization } from '../composables/polarization'
import { useService } from '../composables/service'
import { useTechnician } from '../composables/technician'
import { useUnit } from '../composables/unit'
import { useStationType } from '../composables/stationtype'
import { useRlocFormData } from '../composables/rloc-form-data'
import { useFileValidation } from '../composables/filevalidation'
import { getNode } from '@formkit/core'


const emit = defineEmits(['onSubmit'])
const props = defineProps({
  context: String,
  title: String,
  file: Object,
  station: Object,
  technicians: Object,
  techniciansValues: Array,
})

console.log("station localidad", props.station)
console.log("technician values: ", props.technicians)


function submitHandler(fields) {
  emit('onSubmit', fields)
}

const province = ref(props.station.provincia)
const city = ref(props.station.localidad)
const { provinces, cities, getProvinceCities } = useTerritory()

watch(province, (newValue, oldValue) => {
  console.log("hola")
  props.station.provincia = newValue
  getProvinceCities(newValue)
  if (newValue != oldValue) {
    city.value.value = cities.value[0]
    props.station.localidad = city.value.value
  }
})

const { tipoVinculo } = useLink()
const { area } = useArea()
const { tipoPolarizacion } = usePolarization()
const { servicio } = useService()
const { tecnico } = useTechnician()
const { unidad } = useUnit()
const { emplazamiento } = useStationType()
const store = useRlocFormData()
const { validateFile } = useFileValidation()
const linkType = ref('Radioeléctrico')


</script>

<template>
  <h2>{{ title }}</h2>
  <!-- <h3>{{ file.expediente }}</h3> -->
  <form-kit
    type="form"
    submit-label="Guardar"
    :config="{ validationVisibility: 'submit',
               validation:'required', 
               validationMessages:{ required:'Campo obligatorio', 
                                    validateFile:'Formato incorrecto',
               }
    }"
    @submit="submitHandler"
  >
    <form-row>
      <form-kit
        type="text"
        label="Expediente"
        name="expediente"
        v-model="file.expediente"
        validation="required | validateFile"
        :validation-rules="{ validateFile }"
      />
    </form-row>
    <form-row>
      <form-kit
        type="date"
        label="Fecha"
        name="fecha" 
        v-model="file.fecha"
      />
      <form-kit
        type="time"
        label="Hora"
        name="hora"
        v-model="file.hora"
      />
      <form-kit
        type="select"
        id="area"
        label="CCTE/Área"
        name="area"
        v-model="file.area"
        :options="area"
        placeholder="Área" 
      />
    </form-row>
    <form-row>
    <form-kit
        type="text"
        label="Señal distintiva/Identificación"
        name="identificacion"
        v-model="station.identificacion"
      />
      <form-kit
        type="select"
        label="Servicio"
        name="servicio"
        :options="servicio"
        placeholder="Servicio"
        v-model="station.servicio"
      />
      <form-kit
        type="select"
        label="Tipo de Emplazamiento"
        name="emplazamiento"
        :options="emplazamiento"
        placeholder="Emplazamiento"
        v-model="station.emplazamiento"
      />
    </form-row>
    <form-row>
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="number"
        label="Frecuencia"
        name="frecuencia"
        step="0.000001"
        suffix="MHz"
        v-model="station.frecuencia"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="select"
        label="Unidad"
        name="unidad"
        :options="unidad"
        v-model="station.unidad"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="text"
        label="Clase de Emisión"
        name="claseEmision"
        v-model="station.claseEmision"
      />
    </form-row>
    <form-row>
      <form-kit
        :options="provinces"
        type="select"
        label="Provincia"
        name="provincia"
        v-model="province"
        
      />
      <form-kit
        :options="cities"
        type="select"
        label="Localidad"
        name="localidad"
        v-model="city"
        
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Domicilio"
        name="domicilio"
        v-model="station.domicilio"
      />
      <form-kit
        v-model="store.lat"
        type="number"
        label="Latitud"
        name="lat"
        step="0.000001"
      />
      <form-kit
        v-model="store.lng"
        type="number"
        label="Longitud"
        name="lng"
        step="0.000001"
      />
    </form-row>
    <form-row>
      <form-kit
        type="textarea"
        label="Observaciones"
        name="observacionesDom"
        validation="false"
        v-model="station.observaciones"
      />
    </form-row>

    <form-row>
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="text"
        label="Sistema Irradiante"
        name="irradiante"
        v-model="station.irradiante"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="select"
        label="Polarización"
        name="polarizacion"
        :options="tipoPolarizacion"
        placeholder="Polarización"
        v-model="station.polarizacion"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="text"
        label="Cantidad"
        name="cantidad"
        v-model="station.cantidad"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="text"
        label="Altura Media"
        name="altura"
        help="Altura en metros"
        v-model="station.altura"
      />
    </form-row>
    
    <form-row>
      <form-kit
        v-model="linkType" 
        type="select"
        label="Tipo de Vínculo"
        name="tipoVinculo"
        :options="tipoVinculo"
        placeholder="Vínculo"
      />
      <form-kit
        type="number"
        label="Frecuencia Vínculo"
        name="frecuenciaVinc"
        step="0.00001"
        :disabled="linkType !== 'Radioeléctrico'"
        :validation="linkType === 'Radioeléctrico' && 'required'"
        v-model="station.frecuenciaVinc"
      />
      <form-kit
        type="select"
        label="Unidad"
        name="unidadVinc"
        :options="unidad"
        :disabled="linkType !== 'Radioeléctrico'"
        :validation="linkType === 'Radioeléctrico' && 'required'"
        v-model="station.unidadVinc"
      />
      <form-kit
        type="text"
        label="Sistema Irradiante"
        name="irradianteVinc"
        :disabled="linkType !== 'Radioeléctrico'"
        :validation="linkType === 'Radioeléctrico' && 'required'"
        v-model="station.irradianteVinc"
      />
      <form-kit
        type="select"
        label="Polarización"
        name="polarizacionVinc"
        :options="tipoPolarizacion"
        placeholder="Polarización"
        :disabled="linkType !== 'Radioeléctrico'"
        :validation="linkType === 'Radioeléctrico' && 'required'"
        v-model="station.polarizacionVinc"
      />
    </form-row> 
    <form-row>
      <form-kit
        type="select"
        label="Técnico"
        name="tecnico1"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 1"    
        :value="technician&&technician[0].id"

      />
      <form-kit
        type="select"
        label="Técnico"
        name="tecnico2"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 2" 
        :value="technician&&technician[1].id"

      />
    </form-row>
  </form-kit>
</template>

  
<style scoped>

</style>
  