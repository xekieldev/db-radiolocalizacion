<script setup>
import FormRow from './FormRow.vue'
import Heading from './Heading.vue';
import { useArea } from '../composables/area';
import { useAirport } from '../composables/airport';
import { useType } from '../composables/filetype';
import { useFileValidation } from '../composables/filevalidation'
import { ref, watch, watchEffect } from 'vue';
import { useTerritory } from '../composables/territory'
import { useUnit } from '../composables/unit'
import { userData } from '../composables/loginstatus'
import { useRouter } from 'vue-router'



const userArea = userData.value.area
const emits = defineEmits(['onSubmit', 'update:file.provincia', 'update:file.localidad']);
const { currentRoute } = useRouter()



const props = defineProps({
  context: String,
  title: String,
  file: Object,
  nirMeas: Object,
  technicians: Object,
  techniciansValues: Array,
})

const { area } = useArea()
const{ airport } = useAirport()
const { type } = useType()
const { validateFile } = useFileValidation()
const centrosAllowedTypes = [{ value: 'Tareas Programadas', label: 'Tareas Programadas'}, { value: 'Medición de Radiaciones No Ionizantes (móviles)', label: 'Medición de Radiaciones No Ionizantes (móviles)'}, { value:'Tareas de Oficio', label:'Tareas de Oficio'}]


function submitHandler(fields) {
  // fields.fecha = myDate
  // fields.hora = myTime
  emits('onSubmit', fields)
}

const currentDate = new Date(); 
const fullHours = currentDate.getHours() < 10 ? "0" + currentDate.getHours() : currentDate.getHours()
const fullMinutes = currentDate.getMinutes() < 10 ? "0" + currentDate.getMinutes() : currentDate.getMinutes()
// const fullSeconds = currentDate.getSeconds() < 10 ? "0" + currentDate.getSeconds() : currentDate.getSeconds()
const myTime = fullHours + ":" + fullMinutes// + ":" + fullSeconds

const fullMonth = (currentDate.getMonth()+1)<10 ? "0"+(currentDate.getMonth()+1) : (currentDate.getMonth()+1)
const fullDay = currentDate.getDate()<10 ? "0"+currentDate.getDate() : currentDate.getDate()
const myDate = currentDate.getFullYear() + "-" + fullMonth + "-" + fullDay

const noFrecuency = ref(false)
const { unidad } = useUnit()


const province = ref(props.file.provincia)
const city = ref(props.file.localidad)

const { provinces, cities, getProvinceCities } = useTerritory()

watchEffect(() => {
  if(props.file.provincia) province.value = props.file.provincia
  if(props.file.localidad) city.value = props.file.localidad
})

watch(province, (newValue, oldValue) => {
  emits('update:file.provincia', newValue)
  getProvinceCities(newValue)
  if (newValue !== oldValue) {
    city.value = cities.value[0].value
    emits('update:file.localidad', newValue)
  }
})

function getFileTypeOptions(user_area) {
  if(user_area == 'AGCCTYL') return [...type]  
  if (area.findIndex(item => item.value == user_area) != -1) return [...centrosAllowedTypes]
}

</script>

<template>
  <heading>{{ title }}</heading>
  <form-kit
    type="form"
    submit-label="Guardar"
    :actions="false"
    @submit="submitHandler"
  >
    <form-row>
      <form-kit
        v-if="currentRoute.name !== 'editFile'"
        v-model="file.fecha"
        type="hidden"
        label="Fecha"
        name="fecha"
        :value="myDate"
      />
      <form-kit
        v-else
        v-model="file.fecha"
        type="date"
        label="Fecha"
        name="fecha"
        outer-class="shorter-field"
      />
      <form-kit
        v-if="currentRoute.name !== 'editFile'"
        v-model="file.hora"
        type="hidden"
        label="Hora"
        name="hora"
        :value="myTime"
      />
      <form-kit
        v-else
        v-model="file.hora"
        type="time"
        label="Hora"
        name="hora"
        outer-class="shorter-field"
      />
      <form-kit
        v-model="file.expediente"
        type="text"
        label="Expediente"
        name="expediente"
        validation="required | validateFile"
        :validation-rules="{ validateFile }"
      />
      <form-kit
        v-model="file.tipo"
        type="select"
        label="Tipo de Trámite"
        name="tipo"
        :options="getFileTypeOptions(userArea)"
        placeholder="Seleccione"
      />
      <form-kit
        v-model="file.prioridad"
        value="Normal"
        type="select"
        label="Prioridad"
        name="prioridad" 
        :options="[
          'Urgente',
          'Normal',
        ]"
        outer-class="short-field"
      />
    </form-row>
    <form-row v-if="file.tipo != 'Interferencias en Aeropuertos'">
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
      <form-kit
        v-model="file.area_asignada"
        type="select"
        label="CCTE/Área asignada"
        name="area_asignada"
        :options="area"
        placeholder="Área"
      />
    </form-row>
    
    <div v-if="file.tipo && file.tipo != 'Medición de Radiaciones No Ionizantes (móviles)'">
      <form-row v-if="file.tipo == 'Interferencias en Aeropuertos'">
        <form-kit
          v-if="file.tipo && file.tipo == 'Interferencias en Aeropuertos'"
          v-model="file.aeropuerto"
          type="select"
          label="Aeropuerto/Aeródromo"
          name="aeropuerto"
          :options="airport"
        />
        <form-kit
          v-model="file.nota_inicio"
          type="text"
          label="Nota/Expediente de Inicio"
          name="nota_inicio"
        />
        <form-kit
          v-model="file.area_asignada"
          type="select"
          label="CCTE/Área asignada"
          name="area_asignada"
          :options="area"
          placeholder="Área"
        />
      </form-row>
      <form-row v-if="file.tipo && !(file.tipo == 'Descargo' || file.tipo == 'Interferencias en Aeropuertos') ">
        <form-kit
          v-model="file.domicilio"
          type="text"
          label="Domicilio"
          name="domicilio"        
        />
        <form-kit
          v-model="file.latitud"
          type="number"
          label="Latitud"
          name="latitud"
          step="0.000001"
          outer-class="short-field"
        />
        <form-kit
          v-model="file.longitud"
          type="number"
          label="longitud"
          name="longitud"
          step="0.000001"
          outer-class="short-field"
        />
      </form-row>
      <form-row v-if="file.tipo != 'Descargo'">
        <form-kit
          v-model="file.usuario"
          type="text"
          label="Usuario"
          name="usuario"
        />
        <div class="checkbox-container">
          <form-kit
            v-model="noFrecuency"
            type="checkbox"
            label="Sin dato de frecuencia"
            outer-class="frecuency-checkbox"
          />
        </div>
        <form-kit
          v-if="noFrecuency == false"
          v-model="file.frecuencia"
          type="number"
          label="Frecuencia"
          name="frecuencia"
          step="0.000001"
          suffix="MHz"
          validation="min:0"
          validation-visibility="live"
          :validation-messages="{
            min: 'La frecuencia debe ser mayor que 0.',
          }"
          outer-class="short-field"
        />
        <form-kit 
          v-if="noFrecuency == false"
          v-model="file.unidad"
          type="select"
          label="Unidad"
          name="unidad"
          value="MHz"
          :options="unidad"
          outer-class="short-field"
        />
      </form-row>
      <form-row>
        <form-kit
          v-model="file.motivo"
          type="textarea"
          label="Motivo"
          name="motivo"
          validation="false"
        />
      </form-row>
    </div>
    
    <div
      v-if="file.tipo && file.tipo === 'Medición de Radiaciones No Ionizantes (móviles)'"
      class="NIR-file"
    >
      <form-row>
        <form-kit
          v-model="file.fecha"
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
          v-model="file.hora"
          type="time"
          label="Hora"
          name="hora" 
        />
        <form-kit
          v-model="nirMeas.cantidad"
          type="number"
          label="Cantidad de mediciones"
          name="cantidad" 
        />
        <form-kit
          v-model="nirMeas.valor_maximo"
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
          v-model="nirMeas.observaciones"
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
    </div>
    
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

.short-field {
      /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
      flex: 0 0 20%;
}
.shorter-field {
      /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
      flex: 0 0 10%;
}
.checkbox-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 0 0 16%;
  
}
.frecuency-checkbox {
  align-self: center;
  margin-bottom: 0;
}

</style>
  