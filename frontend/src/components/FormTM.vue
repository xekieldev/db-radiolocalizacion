<script setup>
import FormRow from './FormRow.vue'
import { useUnit } from '../composables/unit';
import { useTerritory } from '../composables/territory';
import { ref, watch } from 'vue';
import Heading from './Heading.vue';

import citiesDataRaw from "../../../data/localidades.json"

const citiesData = citiesDataRaw.localidades


const emit = defineEmits(['onSubmit'])
defineProps({
  title: String,
  techniciansValues: Array,
  technicians: Object,
  techMeasurement: Object,
})
function submitHandler(fields) {
  emit('onSubmit', fields)
}

const { unidad } = useUnit()
const province = ref()
const city = ref()
const cityWitness = ref()
const provinceWitness = ref()
const citiesWitness = ref([])
const { provinces, cities, getProvinceCities } = useTerritory()
const witnessStation = ref(false)

watch([province, city, provinceWitness], (newValue, oldValue) => {
  if (newValue[0] !== oldValue[0]) {
    province.value = newValue[0]
    provinceWitness.value = province.value
    getProvinceCities(newValue[0])
    city.value = cities.value[0].value
    citiesWitness.value = citiesData.filter(c => c.provincia.id === newValue[0]).map(c => ({ label: c.nombre, value: c.id , province: c.provincia.id })) 
    cityWitness.value = citiesWitness.value[0].value
  }
  if (newValue[1] !== oldValue[1]) {
    cityWitness.value = newValue[1]
    city.value = newValue[1]
  }
  if (newValue[2] !== oldValue[2]) {
    provinceWitness.value = newValue[2]
    citiesWitness.value = citiesData.filter(c => c.provincia.id === newValue[2]).map(c => ({ label: c.nombre, value: c.id , province: c.provincia.id }))  
  }
})


</script>

<template>
  <heading> {{ title }} </heading>
  <form-kit
    type="form"
    submit-label="Cargar"
    :config="{ validationVisibility: 'submit',
               validation:'required', 
               validationMessages:{ required:'Campo obligatorio', 
                                    
               }
    }"
    :actions="false"
    @submit="submitHandler"
  >
    <form-row>
      <form-kit
        type="date"
        label="Fecha"
        name="fecha"
        validation="date_after:04-30-2024"
        validation-visibility="live"
        :validation-messages="{
          date_after: 'La fecha debe ser posterior al 01/05/2024.',
        }"
      />
      <form-kit
        type="time"
        label="Hora"
        name="hora"
      />      
      <form-kit
        type="text"
        label="Descripción del Punto de Medición"
        name="puntoMedicion"
      />
    </form-row>
    <form-row>
      <form-kit
        type="number"
        label="Frecuencia Medida"
        name="frecMedida"
        step="0.000001"
        validation="min:0"
        validation-visibility="live"
        :validation-messages="{
          min: 'La frecuencia debe ser mayor que 0.',
        }"
      />
      <form-kit
        type="select"
        label="Unidad"
        name="unidadFrecMedida"
        :options="unidad"
      />
      <form-kit
        type="number"
        label="Ancho de banda"
        name="anchoBanda"
        step="0.000001"
        validation="min:0"
        validation-visibility="live"
        :validation-messages="{
          min: 'El ancho de banda debe ser mayor que 0.',
        }"
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
        v-model="province"
        type="select"
        :options="provinces"
        label="Provincia"
        name="provincia"
      />
      <form-kit
        v-model="city"
        type="select"
        :options="cities"
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
        validation="between:0,-90"
        validation-visibility="live"
        :validation-messages="{
          between: 'Ingrese un valor de latitud entre -90 y 0.',
        }"
      />
      <form-kit
        type="number"
        label="Longitud"
        name="longitud"
        step="0.000001"
        validation="between:0,-180"
        validation-visibility="live"
        :validation-messages="{
          between: 'Ingrese un valor de latitud entre -180 y 0.',
        }"
      />
      <form-kit
        type="number"
        label="Distancia"
        name="distancia"
        help="Distancia en metros"
        validation="min:0"
        validation-visibility="live"
        :validation-messages="{
          min: 'Ingrese un valor positivo para la distancia.',
        }"
      />
      <form-kit
        type="number"
        label="Azimut"
        name="azimut"
        help="Azimut en grados decimales"
        validation="between:0,360"
        validation-visibility="live"
        :validation-messages="{
          between: 'Ingrese un valor de azimut entre 0 y 360.',
        }"
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
    <form-kit
      v-if="techMeasurement && techMeasurement.techMeasurement && techMeasurement.techMeasurement.length == 0"
      v-model="witnessStation"
      type="checkbox"
      label="Agregar Estación Testigo"
      name="witnessStationCheckbox"
    />
    <div v-if="witnessStation === true">
      <form-row v-if="techMeasurement && techMeasurement.techMeasurement && techMeasurement.techMeasurement.length == 0">
        <form-kit
          type="text"
          label="Domicilio estación Testigo"
          name="domicilioTestigo"
        />
        <form-kit
          v-model="provinceWitness"
          type="select"
          :options="provinces"
          label="Provincia"
          name="provinciaTestigo"
        />
        <form-kit
          v-model="cityWitness"
          type="select"
          :options="citiesWitness"
          label="Localidad"
          name="localidadTestigo"
        />
      </form-row>
      <form-row v-if="techMeasurement && techMeasurement.techMeasurement && techMeasurement.techMeasurement.length == 0">
        <form-kit
          type="number"
          label="Latitud"
          name="latitudTestigo"
          step="0.000001"
          validation="between:0,-90"
          validation-visibility="live"
          :validation-messages="{
            between: 'Ingrese un valor de latitud entre -90 y 0.',
          }"
        />
        <form-kit
          type="number"
          label="Longitud"
          name="longitudTestigo"
          step="0.000001"
          validation="between:0,-180"
          validation-visibility="live"
          :validation-messages="{
            between: 'Ingrese un valor de latitud entre -180 y 0.',
          }"
        />
        <form-kit
          type="number"
          label="Distancia"
          name="distanciaTestigo"
          help="Distancia en metros"
          validation="min:0"
          validation-visibility="live"
          :validation-messages="{
            min: 'Ingrese un valor positivo para la distancia.',
          }"
        />
        <form-kit
          type="number"
          label="Azimut"
          name="azimutTestigo"
          help="Azimut geográf. respecto a la PTx en grados decimales"
          validation="between:0,360"
          validation-visibility="live"
          :validation-messages="{
            between: 'Ingrese un valor de azimut entre 0 y 360.',
          }"
        />
      </form-row>
    </div>
    <form-row>
      <form-kit
        type="number"
        label="E medido [dBuV/m]"
        name="eMedido"
        step="0.000001"
        help="Valor de referencia en el punto de medición"
      />
      <form-kit
        v-if="witnessStation === true"
        type="number"
        label="E testigo [dBuV/m]"
        name="eTestigo"
        step="0.000001"
        help="Valor de referencia en el punto de medición"
      />
      <form-kit
        v-if="witnessStation === true"
        type="number"
        label="E corregido [dBuV/m]"
        name="eCorregido"
        step="0.000001"
        help="Valor de referencia en el punto de medición"
      />
      <form-kit
        type="number"
        label="Incertidumbre [dB]"
        name="incertidumbre"
        step="0.000001"
      />
    </form-row>
    <form-row>
      <form-kit
        type="textarea"
        label="Equipamiento utilizado"
        name="equipamiento"
        validation="false"
      />
    </form-row>
    <form-row>
      <form-kit
        type="textarea"
        label="Resultados de las Comprobaciones Técnicas"
        name="resultadoComprob"
        validation="false"
      />
    </form-row>
    <form-row>
      <form-kit
        v-if="technicians && technicians.length>1"
        v-model="technicians[0].id"
        type="select"
        label="Técnico"
        name="id_technician1"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 1"  
      />
      <form-kit
        v-else-if="techniciansValues.length>0"
        type="select"
        label="Técnico"
        name="id_technician1"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 1"
      />
      <form-kit
        v-if="technicians && technicians.length>1"
        v-model="technicians[1].id"
        type="select"
        label="Técnico"
        name="id_technician2"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 2"
      />
      <form-kit
        v-else-if="techniciansValues.length>0"
        type="select"
        label="Técnico"
        name="id_technician2"
        :options="techniciansValues.map((item)=>({label:`${item.apellido}, ${item.nombre}`, value:item.id}))"
        placeholder="Técnico 2"
      />
    </form-row>
    <button
      class="submit-button"
    >
      Guardar
    </button>
  </form-kit>
</template>
 
<style scoped>
.submit-button {
      background-color: white;
      margin: 10px 0 20px;
      padding: 10px 18px;
      border-radius: 20px;
      cursor: pointer;
      border: 1px solid #007BFF;
      font-weight: 600;  
      color: #007BFF;  
      align-self: flex-end;

}
.submit-button:hover {
      background-color: #007BFF;
      color: white;
}

</style>
  