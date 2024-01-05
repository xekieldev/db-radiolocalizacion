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
})
function submitHandler(fields) {
  emit('onSubmit', fields)
}

const province = ref("54")
const city = ref("06021010000")
const { provinces, cities, getProvinceCities } = useTerritory()

watch(province, (newValue, oldValue) => {
  getProvinceCities(newValue)
  if (newValue != oldValue) {
    city.value = cities.value[0]
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
  <h3>{{ file.expediente }}</h3>
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
      />
      <form-kit
        type="time"
        label="Hora"
        name="hora"
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
        @keyup="value = value.toUpperCase()"
      />
      <form-kit
        type="select"
        label="Servicio"
        name="servicio"
        :options="servicio"
        placeholder="Servicio"
      />
      <form-kit
        type="select"
        label="Tipo de Emplazamiento"
        name="emplazamiento"
        :options="emplazamiento"
        placeholder="Emplazamiento"
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
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="select"
        label="Unidad"
        name="unidad"
        :options="unidad"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="text"
        label="Clase de Emisión"
        name="claseEmision"
      />
    </form-row>
    <form-row>
      <form-kit
        v-model="province"
        type="select"
        label="Provincia"
        name="province"
        :options="provinces"
      />
      <form-kit
        v-model="city"
        type="select"
        label="Localidad"
        name="city"
        :options="cities"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Domicilio"
        name="domicilio"
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
      />
    </form-row>

    <form-row>
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="text"
        label="Sistema Irradiante"
        name="irradiante"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="select"
        label="Polarización"
        name="polarizacion"
        :options="tipoPolarizacion"
        placeholder="Polarización"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="text"
        label="Cantidad"
        name="cantidad"
      />
      <form-kit
        v-if="props.context === 'Radiolocalizacion'"
        type="text"
        label="Altura Media"
        name="altura"
        help="Altura en metros"
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
      />
      <form-kit
        type="select"
        label="Unidad"
        name="unidad"
        :options="unidad"
        :disabled="linkType !== 'Radioeléctrico'"
        :validation="linkType === 'Radioeléctrico' && 'required'"
      />
      <form-kit
        type="text"
        label="Sistema Irradiante"
        name="irradianteVinc"
        :disabled="linkType !== 'Radioeléctrico'"
        :validation="linkType === 'Radioeléctrico' && 'required'"
      />
      <form-kit
        type="select"
        label="Polarización"
        name="polarizacionVinc"
        :options="tipoPolarizacion"
        placeholder="Polarización"
        :disabled="linkType !== 'Radioeléctrico'"
        :validation="linkType === 'Radioeléctrico' && 'required'"
      />
    </form-row> 
    <form-row>
      <form-kit
        type="select"
        label="Técnico"
        name="tecnico"
        :options="tecnico"
        placeholder="Técnico 1"
      />
      <form-kit
        type="select"
        label="Técnico"
        name="tecnico"
        :options="tecnico"
        placeholder="Técnico 2"
      />
    </form-row>
  </form-kit>
</template>

  
<style scoped>

</style>
  