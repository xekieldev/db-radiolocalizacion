<script setup>
import FormRow from './FormRow.vue'
import { useApi} from '../composables/api'
import { useArea } from '../composables/area'
import { useUnit } from '../composables/unit';
import { useTechnician } from '../composables/technician';
import { onBeforeMount, reactive, ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router'
import Heading from './Heading.vue';


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
  <!-- <h2>{{ title }}</h2> -->
  <heading> {{ title }} </heading>
  <form-kit
    type="form"
    submit-label="Cargar"
    @submit="submitHandler"
  >
    <form-row>
      <!-- <form-kit
        type="text"
        label="Expediente"
        name="expediente"
        :validation="[['required'], ['matches', /^EX-\d{4}-\d{6,10}-\s{2,3}-[A-Z]{3,7}-[A-Z]{3,10}#[A-Z]{2,8}$/,
                                     /^IF-\d{4}-\d{8}-[A-Z]{3}-[A-Z]{5}#[A-Z]{6}$/, /^NO-\d{4}-\d{8}-[A-Z]{3,8}-[A-Z]{3,10}#?[A-Z]{6}?$/, /^[A-Z]{5,20}\s?E?\s?\s\d{1,8}\/\d{4}$/]]"
        validation-visibility="live"
        v-model="file.expediente"
        :disabled="true"
      /> -->
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
        type="text"
        label="Punto de Medición"
        name="puntoMedicion"
      />
    </form-row>

    <form-row>

      <form-kit
        type="number"
        label="Frecuencia Medida"
        name="frecMedida"
        step="0.001"
      />
      <form-kit
        type="select"
        label="Unidad"
        name="unidadFrecMedida"
        :options="unidad"
      />
      <form-kit
        type="number"
        label="Anchura de banda"
        name="anchoBanda"
      />
      <form-kit
        type="select"
        label="Unidad"
        name="unidadBW"
        :options="unidad"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Domicilio"
        name="domicilio"
      />
      <form-kit
        type="text"
        label="Provincia"
        name="provincia"
      />
      <form-kit
        type="text"
        label="Localidad"
        name="localidad"
      />
    </form-row>
    <form-row>
      <form-kit
        type="number"
        label="Latitud"
        name="latitud"
        step="0.000001"
      />
      <form-kit
        type="number"
        label="Longitud"
        name="longitud"
        step="0.000001"
      />
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
        type="textarea"
        label="Descripción/Observaciones"
        name="observaciones"
        validation="false"
      />
    </form-row>
    <div style="border: 1px solid gray; padding: 10px; border-radius: 5px; margin: 10px 0 10px 0">
    <form-row>
      <form-kit
        type="text"
        label="Domicilio estación Testigo"
        name="domicilioTestigo"
      />
      <form-kit
        type="text"
        label="Provincia"
        name="provinciaTestigo"
      />
      <form-kit
        type="text"
        label="Localidad"
        name="localidadTestigo"
      />
    </form-row>
    <form-row>
      <form-kit
        type="number"
        label="Latitud"
        name="latitudTestigo"
        step="0.000001"
      />
      <form-kit
        type="number"
        label="Longitud"
        name="longitudTestigo"
        step="0.000001"
      />
      <form-kit
        type="number"
        label="Distancia"
        name="distanciaTestigo"
        help="Distancia en metros"
      />
      <form-kit
        type="number"
        label="Azimut"
        name="azimutTestigo"
        help="Azimut geográf. respecto a la PTx en grados decimales"
      />
    



    </form-row>
  </div>

    <form-row>
      <form-kit
        type="number"
        label="E medido [dBuV/m]"
        name="eMedido"
        help="Valor de referencia en el punto de medición"
      />
      <form-kit
        type="number"
        label="E testigo [dBuV/m]"
        name="eTestigo"
        help="Valor de referencia en el punto de medición"
      />
      <form-kit
        type="number"
        label="E corregido [dBuV/m]"
        name="eCorregido"
        help="Valor de referencia en el punto de medición"
      />
      <form-kit
        type="number"
        label="Incertidumbre [dB]"
        name="incertidumbre"
      />
    </form-row>
    <form-row>
      <form-kit
        type="textarea"
        label="Descripción/Observaciones"
        name="resultadoComprob"
        validation="false"
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
  