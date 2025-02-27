<script setup>
import FormRow from './FormRow.vue'
import { ref, watch, reactive, onBeforeMount } from 'vue'
import { useTerritory } from '../composables/territory'
import { useLink } from '../composables/link'
import { useArea } from '../composables/area'
import { usePolarization } from '../composables/polarization'
import { useService } from '../composables/service'
import { useUnit } from '../composables/unit'
import { useStationType } from '../composables/stationtype'
import { useAntenna } from '../composables/antenna'
import { useRouter, useRoute } from 'vue-router'
import { useApi } from '../composables/api'
import Heading from './Heading.vue'

const router = useRouter()
const { currentRoute } = useRouter()
const route = useRoute()

const { getStation } = useApi()
const emits = defineEmits(['onSubmit', 'update:station.provincia', 'update:station.localidad']);
const props = defineProps({
  context: String,
  title: String,
  file: Object,
  station: Object,
  technicians: Object,
  techniciansValues: Array,
})
const stationPath = reactive({})
const stationId = ref('')

function submitHandler(fields) {
  emits('onSubmit', fields)
}

onBeforeMount( async ()=> {
  try{
    const from = route.query.from
    stationId.value = from ? from.split('/').pop() : null
    const response = await getStation(stationId.value)        
    Object.assign(stationPath , response.station)
  } catch {

    stationId.value = null
  
  }
})

const province = ref(props.station.provincia)
const city = ref(props.station.localidad)
const { provinces, cities, getProvinceCities } = useTerritory()

watch(province, (newValue, oldValue) => {
  emits('update:station.provincia', newValue)
  getProvinceCities(newValue)
  if (newValue !== oldValue) {
    
    city.value = cities.value[0].value
    emits('update:station.localidad', newValue)

  }  
})

const { tipoVinculo } = useLink()
const { area } = useArea()
const { tipoPolarizacion } = usePolarization()
const { servicio } = useService()
const { antenna } = useAntenna()
const { unidad } = useUnit()
const { emplazamiento } = useStationType()


</script>

<template>
  <div class="form-main-container">
    <heading v-if="router.currentRoute.value.query.rloc =='true'">
      {{ title }}
    </heading>
    <heading v-else>
      Datos de Localización
    </heading>
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
          v-model="file.expediente"
          type="text"
          label="Expediente"
          name="expediente"
          :disabled="true"
        />
      </form-row>
      <form-row>
        <form-kit
          v-model="station.fecha"
          type="date"
          label="Fecha" 
          name="fecha" 
          validation="required|date_after:04-30-2024"
          validation-visibility="submit"
          :validation-messages="{
            required: 'Este campo es obligatorio.',
            date_after: 'La fecha debe ser posterior al 01/05/2024.',
          }"
        />
        <form-kit
          v-model="station.hora"
          type="time"
          label="Hora"
          name="hora"        
        />
        <form-kit
          v-if="stationId != null || stationId != undefined"
          id="area"
          v-model="stationPath.area"
          type="select"
          label="CCTE/Área"
          name="area"
          :options="area"
          placeholder="Área"
          :disabled="true"
        />
        <form-kit
          v-else
          id="area"
          v-model="station.area"
          type="select"
          label="CCTE/Área"
          name="area"
          :options="area" 
          placeholder="Área"
        />
      </form-row>
      <form-row>
        <form-kit
          v-model="station.identificacion"
          type="text"
          label="Señal distintiva/Identificación"
          name="identificacion"
        />
        <form-kit
          v-model="station.servicio"
          type="select"
          label="Servicio/Sistema"
          name="servicio"
          :options="servicio"
          placeholder="Servicio/Sistema"
        />
        <form-kit
          v-if="stationId != null || stationId != undefined"
          v-model="station.emplazamiento"
          type="select"
          label="Tipo de Emplazamiento"
          name="emplazamiento"
          :options="emplazamiento"
          placeholder="Emplazamiento"
          value="Estudio"
          :disabled="true"
        />
        <form-kit
          v-else
          v-model="station.emplazamiento"
          type="select"
          label="Tipo de Emplazamiento"
          name="emplazamiento"
          :options="emplazamiento"
          placeholder="Emplazamiento"
        />
      </form-row>
      <form-row>
        <form-kit
          v-if="router.currentRoute.value.query.rloc == 'true'"
          v-model="station.frecuencia"
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
        />
        <form-kit
          v-if="router.currentRoute.value.query.rloc == 'true'"
          v-model="station.unidad"
          type="select"
          label="Unidad"
          name="unidad"
          :options="unidad"
        />
        <form-kit
          v-if="router.currentRoute.value.query.rloc =='true'"
          v-model="station.claseEmision"
          type="text"
          label="Clase de Emisión"
          name="claseEmision"
          :validation="[['required'],['matches', /^[A-Z]{1}(\d{1}|[X]{1})[A-Z]{1}([A-Z]{1,2})?$/]]"
          validation-visibility="submit"
          :validation-messages="{
            required: 'Este campo es obligatorio.',
            matches: 'Ingrese una clase de emision válida.',
          }"
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
          v-model="station.domicilio"
          outer-class="field-domicilio"
          type="text"
          label="Domicilio"
          name="domicilio"
        />
        <form-kit
          v-model="station.latitud"
          type="number"
          label="Latitud"
          name="latitud"
          step="0.000001"
          validation="required|between:0,-90"
          validation-visibility="submit"
          :validation-messages="{
            required: 'Este campo es obligatorio.',
            between: 'Ingrese un valor de latitud entre -90 y 0.',
          }"
        />
        <form-kit
          v-model="station.longitud"
          type="number"
          label="Longitud"
          name="longitud"
          step="0.000001"
          validation="required|between:0,-180"
          validation-visibility="submit"
          :validation-messages="{
            required: 'Este campo es obligatorio.',
            between: 'Ingrese un valor de latitud entre -180 y 0.',
          }"
        />
      </form-row>
      <form-row>
        <form-kit
          v-model="station.observaciones"
          type="textarea"
          label="Observaciones"
          name="observaciones"
          validation="false"
        />
      </form-row>
      <form-row>
        <form-kit
          v-if="router.currentRoute.value.query.rloc == 'true'"
          v-model="station.irradiante"
          type="select"
          outer-class="field-irradiante"
          :options="antenna"
          label="Sistema Irradiante"
          name="irradiante"
          placeholder="Sistema irradiante"
        />
        <form-kit
          v-if="router.currentRoute.value.query.rloc == 'true' && station.irradiante !== 'No posee' && station.irradiante !== '---' && station.irradiante !== 'Ver observaciones' && station.irradiante !== 'No se pudo determinar' && station.irradiante !== 'No se observa'"
          v-model="station.polarizacion"
          type="select"
          label="Polarización"
          name="polarizacion"
          :options="tipoPolarizacion"
          placeholder="Polarización"
        />
        <form-kit
          v-if="router.currentRoute.value.query.rloc == 'true' && station.irradiante !== 'No posee' && station.irradiante !== '---' && station.irradiante !== 'Ver observaciones' && station.irradiante !== 'No se pudo determinar' && station.irradiante !== 'No se observa'"
          v-model="station.cantidad"
          type="text"
          label="Cantidad"
          name="cantidad"
        />
        <form-kit
          v-if="router.currentRoute.value.query.rloc == 'true' && station.irradiante !== 'No posee' && station.irradiante !== '---' && station.irradiante !== 'Ver observaciones' && station.irradiante !== 'No se pudo determinar' && station.irradiante !== 'No se observa'"
          v-model="station.altura"
          type="number"
          label="Altura Media"
          step="0.01"
          name="altura"
          validation="min:0"
          help="Altura en metros"
          validation-visibility="live"
          :validation-messages="{
            min: 'Ingrese un valor positivo para la altura.',
          }"
        />
      </form-row>   
      <form-row v-if="router.currentRoute.value.query.rloc == 'true'">
        <form-kit
          v-if="(stationId == null || stationId == undefined) && station.emplazamiento != 'Estudio'"
          v-model="station.tipoVinculo" 
          outer-class="field-emplazamiento"
          type="select"
          label="Tipo de Vínculo"
          name="tipoVinculo"
          :options="tipoVinculo"
          placeholder="Vínculo"
        />
        <form-kit
          v-if="station.tipoVinculo == 'Radioeléctrico'"
          v-model="station.frecuenciaVinc"
          type="number"
          label="Frecuencia Vínculo"
          name="frecuenciaVinc"
          step="0.00001"
          :disabled="(station.tipoVinculo || '').toLowerCase() !== 'radioeléctrico'"
          :validation="((station.tipoVinculo || '').toLowerCase() === 'radioeléctrico' || '') && 'required' && 'min:0'" 
          validation-visibility="live"
          :validation-messages="{
            min: 'La frecuencia debe ser mayor que 0.',
          }"
        />
        <form-kit
          v-if="station.tipoVinculo == 'Radioeléctrico'"
          v-model="station.unidadVinc"
          type="select"
          label="Unidad"
          name="unidadVinc"
          :options="unidad"
          :disabled="(station.tipoVinculo || '').toLowerCase() !== 'radioeléctrico'"
          :validation="((station.tipoVinculo || '').toLowerCase() === 'radioeléctrico' || '') && 'required'"
        />
        <form-kit
          v-if="station.tipoVinculo == 'Radioeléctrico'"
          v-model="station.irradianteVinc"
          type="select"
          label="Sistema Irradiante"
          :options="antenna"
          name="irradianteVinc"
          placeholder="Sistema irradiante"
          :disabled="(station.tipoVinculo || '').toLowerCase() !== 'radioeléctrico'"
          :validation="((station.tipoVinculo || '').toLowerCase() === 'radioeléctrico' || '') && 'required'"
        />
        <form-kit
          v-if="station.tipoVinculo == 'Radioeléctrico'"
          v-model="station.polarizacionVinc"
          type="select"
          label="Polarización"
          name="polarizacionVinc"
          :options="tipoPolarizacion"
          placeholder="Polarización"
          :disabled="(station.tipoVinculo || '').toLowerCase() !== 'radioeléctrico'"
          :validation="((station.tipoVinculo || '').toLowerCase() === 'radioeléctrico' || '') && 'required'"
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
      <form-row>
        <form-kit
          v-if="stationId != null || stationId != undefined"
          v-model="station.related_station_id"
          outer-class="field-related_station"
          type="hidden"
          label="Estación relacionada"
          name="related_station_id"   
          :disabled="true"
          :value="stationId"
        />
      </form-row>      
      <button
        class="submit-button"
      >
        Guardar
      </button>
    </form-kit>
  </div>
</template>

  
<style scoped>

.form-main-container {
  padding: 0 30px;
}
.field-domicilio {
      /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
      flex: 0 0 70%;
}
.field-emplazamiento {
      flex: 0 0 20%;
}
.field-status {
      flex: 0 0 10%;
}
.field-irradiante {
      flex: 0 0 40%;
}
.field-related_station {
      flex: 0 0 15%;
}
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
  