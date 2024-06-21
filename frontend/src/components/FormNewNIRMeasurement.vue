<script setup>
import FormRow from './FormRow.vue'
import Heading from './Heading.vue';
import { useArea } from '../composables/area';
import { useTerritory } from '../composables/territory'
import { ref, watch } from 'vue';
import { useFileValidation } from '../composables/filevalidation'


const { validateFile } = useFileValidation()
const { area } = useArea()


const emit = defineEmits(['onSubmit'])
defineProps({
  context: String,
  title: String,
  technicians: Object,
  techniciansValues: Array,
})

function submitHandler(fields) {
  emit('onSubmit', fields)
}


// const province = ref(props.station.provincia)
// const city = ref(props.station.localidad)
const province = ref()
const city = ref()
const { provinces, cities, getProvinceCities } = useTerritory()

watch(province, (newValue, oldValue) => {
  province.value = newValue
  getProvinceCities(newValue)
  if (newValue !== oldValue) {
    city.value = cities.value[0].value
  }  
})

</script>

<template>
  <heading>{{ title }}</heading>
  <form-kit
    type="form"
    submit-label="Guardar"
    :config="{ validationVisibility: 'submit',
               validation:'required', 
               validationMessages:{ required:'Campo obligatorio', 
                                    validateFile:'Formato incorrecto',
               }
    }"
    :actions="false"
    @submit="submitHandler"
  >
    <form-row>
      <form-kit
        type="text"
        label="Expediente"
        name="expediente"
        validation="required | validateFile"
        :validation-rules="{ validateFile }"
      />
    </form-row>
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
        type="select"
        :options="area"
        label="CCTE/Área"
        name="area" 
      />

    </form-row>
    <form-row>
      <form-kit
        v-model="province"
        :options="provinces"
        type="select"
        label="Provincia"
        name="provincia"        
      />
      <form-kit
        v-model="city"
        :options="cities"
        type="select"
        label="Localidad"
        name="localidad"  
      />
    </form-row>
    <form-row>
      <form-kit
        type="number"
        label="Cantidad de mediciones"
        name="cantidad" 
      />
      <form-kit
        type="number"
        label="Valor Medido Máximo [%]"
        name="valor_maximo" 
        step="0.000001"
        suffix="%"
        validation="min:0"
        validation-visibility="live"
        :validation-messages="{
          min: 'El valor medido debe ser mayor que 0.',
        }"
      />
    </form-row>
    <form-row>
      <form-kit
        type="textarea"
        label="Observaciones"
        name="observaciones"
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
  