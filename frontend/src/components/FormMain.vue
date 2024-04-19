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
import { useFileValidation } from '../composables/filevalidation'
import { useRoute, useRouter } from 'vue-router'
import { useApi} from '../composables/api'
import Heading from './Heading.vue'



const route = useRoute()
const router = useRouter()
const { currentRoute } = useRouter()

const { getFile } = useApi()

const emit = defineEmits(['onSubmit'])
const props = defineProps({
  context: String,
  title: String,
  file: Object,
  station: Object,
  technicians: Object,
  techniciansValues: Array,
})

const filePath = reactive({})
const fileId = ref('')

console.log("path ahroa:", router.currentRoute.value.name)


function submitHandler(fields) {
  emit('onSubmit', fields)
}


onBeforeMount( async ()=> {
  try{
    fileId.value = currentRoute.value.query.from.slice(6,)
    console.log("fileId: ", fileId)
    const response = await getFile(fileId.value)  
    Object.assign(filePath , response.file)

    console.log("filePath: ", filePath)
  } catch {
  fileId.value = null
  }
})

console.log("Edition query: ", router.currentRoute.value.query.rloc, "Edition name: ", router.currentRoute.value.name )

const province = ref(props.station.provincia)
const city = ref(props.station.localidad)
const { provinces, cities, getProvinceCities } = useTerritory()

watch(province, (newValue, oldValue) => {
  props.station.provincia = newValue
  
  getProvinceCities(newValue)
  if (newValue !== oldValue) {
    // console.log(cities && cities.value && cities.value.length && cities.value[0].value)
    
    city.value = cities.value[0].value
    props.station.localidad = city.value.value
  }
  console.log('ready')
  
})

const { tipoVinculo } = useLink()
const { area } = useArea()
const { tipoPolarizacion } = usePolarization()
const { servicio } = useService()
const { unidad } = useUnit()
const { emplazamiento } = useStationType()
const { validateFile } = useFileValidation()
const linkType = ref('Radioeléctrico')


</script>

<template>
  <heading v-if="router.currentRoute.value.query.rloc =='true'">{{ title }}</heading>
  <heading v-else> Datos de Localización</heading>
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
    :actions="false"
  >
    <form-row>
      <form-kit
        type="text"
        label="Expediente"
        name="expediente"
        v-model="filePath.expediente"
        validation="required | validateFile"
        :validation-rules="{ validateFile }"
        v-if="fileId != null || fileId != undefined"
        :disabled="true"

      />
      <form-kit
        type="text"
        label="Expediente"
        name="expediente"
        v-model="file.expediente"
        validation="required | validateFile"
        :validation-rules="{ validateFile }"
        v-else
      />
      <!-- <form-kit
        outer-class="field-status"
        type="text"
        label="Status"
        name="status"
        v-model="file.status"
        value="Available"
        :disabled="true"
      /> -->
    </form-row>
    <form-row>
      <!-- <form-kit
        type="date"
        label="Fecha"
        name="fecha" 
        v-model="filePath.fecha"
        v-if="fileId != null || fileId != undefined"
        :disabled="true"
      /> -->
      <form-kit
        type="date"
        label="Fecha"
        name="fecha" 
        v-model="file.fecha"
        
      />
      <!-- <form-kit
        type="time"
        label="Hora"
        name="hora"
        v-model="filePath.hora"
        v-if="fileId != null || fileId != undefined"
        :disabled="true"
      /> -->
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
        v-model="filePath.area"
        :options="area"
        placeholder="Área"
        v-if="fileId != null || fileId != undefined"
        :disabled="true"
      />
      <form-kit
        type="select"
        id="area"
        label="CCTE/Área"
        name="area"
        v-model="file.area"
        :options="area"
        placeholder="Área" 
        v-else
      />
    </form-row>
    <form-row>
      <!-- <form-kit
        outer-class="field-status"
        type="text"
        label="Status"
        name="status2"
        v-model="station.status2"
        value="Available"
        :disabled="true"
      /> -->
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
        v-if="fileId != null || fileId != undefined"
        value="Estudio"
        :disabled="true"

      />
      <form-kit
        type="select"
        label="Tipo de Emplazamiento"
        name="emplazamiento"
        :options="emplazamiento"
        placeholder="Emplazamiento"
        v-model="station.emplazamiento"
        v-else

      />
    </form-row>
    <form-row>
      <form-kit
        v-if="router.currentRoute.value.query.rloc == 'true'"
        type="number"
        label="Frecuencia"
        name="frecuencia"
        step="0.000001"
        suffix="MHz"
        v-model="station.frecuencia"
      />
      <form-kit
        v-if="router.currentRoute.value.query.rloc == 'true'"
        type="select"
        label="Unidad"
        name="unidad"
        :options="unidad"
        v-model="station.unidad"
      />
      <form-kit
        v-if="router.currentRoute.value.query.rloc =='true'"
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
        outer-class="field-domicilio"
        type="text"
        label="Domicilio"
        name="domicilio"
        v-model="station.domicilio"
      />
      <form-kit
        v-model="station.latitud"
        type="number"
        label="Latitud"
        name="latitud"
        step="0.000001"
      />
      <form-kit
        v-model="station.longitud"
        type="number"
        label="Longitud"
        name="longitud"
        step="0.000001"
      />
    </form-row>
    <form-row>
      <form-kit
        type="textarea"
        label="Observaciones"
        name="observaciones"
        validation="false"
        v-model="station.observaciones"
      />
    </form-row>

    <form-row>
      <form-kit
        v-if="router.currentRoute.value.query.rloc == 'true'"
        type="text"
        label="Sistema Irradiante"
        name="irradiante"
        v-model="station.irradiante"
      />
      <form-kit
        v-if="router.currentRoute.value.query.rloc == 'true'"
        type="select"
        label="Polarización"
        name="polarizacion"
        :options="tipoPolarizacion"
        placeholder="Polarización"
        v-model="station.polarizacion"
      />
      <form-kit
        v-if="router.currentRoute.value.query.rloc == 'true'"
        type="text"
        label="Cantidad"
        name="cantidad"
        v-model="station.cantidad"
      />
      <form-kit
        v-if="router.currentRoute.value.query.rloc == 'true'"
        type="text"
        label="Altura Media"
        name="altura"
        help="Altura en metros"
        v-model="station.altura"
      />
    </form-row>
    
    <form-row v-if="router.currentRoute.value.query.rloc == 'true'">
      <form-kit
        outer-class="field-emplazamiento"
        v-model="station.tipoVinculo" 
        type="select"
        label="Tipo de Vínculo"
        name="tipoVinculo"
        :options="tipoVinculo"
        placeholder="Vínculo"
        v-if="(fileId == null || fileId == undefined) && station.emplazamiento != 'Estudio'"
      />
      <form-kit
        v-if="station.tipoVinculo == 'Radioeléctrico'"
        type="number"
        label="Frecuencia Vínculo"
        name="frecuenciaVinc"
        step="0.00001"
        :disabled="(station.tipoVinculo || '').toLowerCase() !== 'radioeléctrico'"
        :validation="((station.tipoVinculo || '').toLowerCase() === 'radioeléctrico' || '') && 'required'"
        v-model="station.frecuenciaVinc"
      />
      <form-kit
        v-if="station.tipoVinculo == 'Radioeléctrico'"
        type="select"
        label="Unidad"
        name="unidadVinc"
        :options="unidad"
        :disabled="(station.tipoVinculo || '').toLowerCase() !== 'radioeléctrico'"
        :validation="((station.tipoVinculo || '').toLowerCase() === 'radioeléctrico' || '') && 'required'"
        v-model="station.unidadVinc"
      />
      <form-kit
        v-if="station.tipoVinculo == 'Radioeléctrico'"
        type="text"
        label="Sistema Irradiante"
        name="irradianteVinc"
        :disabled="(station.tipoVinculo || '').toLowerCase() !== 'radioeléctrico'"
        :validation="((station.tipoVinculo || '').toLowerCase() === 'radioeléctrico' || '') && 'required'"
        v-model="station.irradianteVinc"
      />
      <form-kit
        v-if="station.tipoVinculo == 'Radioeléctrico'"
        type="select"
        label="Polarización"
        name="polarizacionVinc"
        :options="tipoPolarizacion"
        placeholder="Polarización"
        :disabled="(station.tipoVinculo || '').toLowerCase() !== 'radioeléctrico'"
        :validation="((station.tipoVinculo || '').toLowerCase() === 'radioeléctrico' || '') && 'required'"
        v-model="station.polarizacionVinc"
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
        v-else-if="techniciansValues.length > 0"
        

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
        v-else-if="techniciansValues.length > 0"
        

      />
    </form-row>
    <button class="submit-button" slot="submit">Guardar</button>
  </form-kit>
</template>

  
<style scoped>
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
  