<script setup>
import FormRow from './FormRow.vue'
import { useApi} from '../composables/api'
import { useArea } from '../composables/area'
import { useUnit } from '../composables/unit';
import { useTechnician } from '../composables/technician';
import { onBeforeMount, reactive, ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router'


const { currentRoute } = useRouter()
// const file = reactive ({})

const initialTechnicians = ref([{id: "1"}, { id: "2"}])


const emit = defineEmits(['onSubmit'])
const props = defineProps({
  // context: String,
  title: String,
  techniciansValues: Array,
  technicians: Object,
  file: Object,
})
function submitHandler(fields) {
  emit('onSubmit', fields)
}

// console.log("file.area", file)


const { area } = useArea()
const { unidad } = useUnit()
// const { tecnico} = useTechnician()

</script>

<template>
  <h2>{{ title }}</h2>
  <form-kit
    type="form"
    submit-label="Cargar"
    @submit="submitHandler"
  >
    <form-row>
      <form-kit
        type="text"
        label="Expediente"
        name="expediente"
        :validation="[['required'], ['matches', /^EX-\d{4}-\d{6,10}-\s{2,3}-[A-Z]{3,7}-[A-Z]{3,10}#[A-Z]{2,8}$/,
                                     /^IF-\d{4}-\d{8}-[A-Z]{3}-[A-Z]{5}#[A-Z]{6}$/, /^NO-\d{4}-\d{8}-[A-Z]{3,8}-[A-Z]{3,10}#?[A-Z]{6}?$/, /^[A-Z]{5,20}\s?E?\s?\s\d{1,8}\/\d{4}$/]]"
        validation-visibility="live"
        v-model="file.expediente"
        :disabled="true"
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
        label="CCTE/Área"
        name="area"
        :options="area"
        placeholder="Área"
        v-model="file.area"
        :disabled="true"
      />
    </form-row>

    <form-row>
      <form-kit
        type="text"
        label="Provincia"
        name="provincia"
        validation="required| text"
      />
      <form-kit
        type="text"
        label="Localidad"
        name="localidad"
        validation="required| text"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Domicilio"
        name="domicilio"
        validation="required| text"
      />
      <form-kit
        type="number"
        label="Latitud"
        name="latitud"
        validation="required| number"
        step="0.000001"

      />
      <form-kit
        type="number"
        label="Longitud"
        name="longitud"
        validation="required| number"
        step="0.000001"

      />
    </form-row>
    <form-row>
      <form-kit
        type="number"
        label="Distancia"
        name="distancia"
        help="Distancia en metros"
      />
      <form-kit
        type="number"
        label="Azimut"
        name="azimut"
        help="Azimut en grados decimales"
      />
    </form-row>
    <form-row>
      <form-kit
        type="number"
        label="Frecuencia Característica"
        name="frecuenciaCaract"
        step="0.001"
        validation-visibility="live"
      />
      <form-kit
        type="number"
        label="Intensidad de Campo Radioeléctrico [dBuV/m]"
        name="mic"
        help="Valor de referencia en el punto de medición"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Clase de Emisión"
        name="claseEmision"
      />
      <form-kit
        type="number"
        label="Anchura de banda"
        name="anchoBanda"
      />
      <form-kit
        type="select"
        label="Unidad"
        name="unidad"
        :options="unidad"
      />
    </form-row>
    <form-row>
      <form-kit
        type="number"
        label="No esencial"
        name="noEsencial1"
        step="0.001"
        validation-visibility="live"
      />
      <form-kit
        type="number"
        label="Intensidad de Campo Radioeléctrico [dBuV/m]"
        name="micNoEsencial1"
        help="Valor de referencia en el punto de medición"
      />
    </form-row>   
    <form-row>
      <form-kit
        type="number"
        label="No esencial"
        name="noEsencial2"
        step="0.001"
        validation-visibility="live"
      />
      <form-kit
        type="number"
        label="Intensidad de Campo Radioeléctrico [dBuV/m]"
        name="micNoEsencial2"
        help="Valor de referencia en el punto de medición"
      />
    </form-row> 
    <form-row>
      <form-kit
        type="number"
        label="No esencial"
        name="noEsencial3"
        step="0.001"
        validation-visibility="live"
      />
      <form-kit
        type="number"
        label="Intensidad de Campo Radioeléctrico [dBuV/m]"
        name="micNoEsencial3"
        help="Valor de referencia en el punto de medición"
      />
    </form-row> 

    <form-row>
      <form-kit
        type="textarea"
        label="Resultado de las Comprobaciones Técnicas"
        name="ResultadoComprob"
      />
    </form-row>
    <form-row>
      <form-kit
        type="select"
        label="Técnico"
        name="id_technician1"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 1"
        v-if="technicians && technicians.length > 1"    
        v-model="technicians[0].id"

  
      />
      <form-kit
        type="select"
        label="Técnico"
        name="id_technician1"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 1"
        v-else
        v-model="initialTechnicians[0].id"

      />
      <form-kit
        type="select"
        label="Técnico"
        name="id_technician2"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 2"
        v-if="technicians && technicians.length > 1"    
        v-model="technicians[1].id"
  
      />
      <form-kit
        type="select"
        label="Técnico"
        name="id_technician2"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 2"
        v-else
        v-model="initialTechnicians[1].id"

      />
    </form-row>
  </form-kit>
</template>

  
<style></style>
  