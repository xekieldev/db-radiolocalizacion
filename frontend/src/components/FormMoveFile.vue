<script setup>
import FormRow from './FormRow.vue'
import { useArea } from '../composables/area'
import { useExternalArea } from '../composables/externalareas'
import { userData } from '../composables/loginstatus'
import { useFileValidation } from '../composables/filevalidation'


const emits = defineEmits(['onSubmit'])
const { area } = useArea()
const { externalArea } = useExternalArea()
const centrosAllowedAreas = [{ value: 'AGCCTYL', label: 'AGCCTYL'}, { value: 'Guarda Temporal', label: 'Guarda Temporal'}]
// const areasExternas = [{value:'ACRA#ENACOM', label:'ACRA#ENACOM'},{value: 'DNSA#ENACOM', label: 'DNSA#ENACOM'}]
const userArea = userData.value.area
const { validateFile } = useFileValidation()

function submitHandler(fields) {
  emits('onSubmit', fields)
}

const props = defineProps({
  context: String,
  fileType: String,
  fileNumber: String,
  location: String,
  informe: String,
})

function getAreasOptions(user_area) {
  if(user_area == 'AGCCTYL') return [...externalArea, ...area]  
  if (area.findIndex(item => item.value == user_area) != -1) return [...centrosAllowedAreas]
}

</script>

<template>
  <form-kit
    type="form"
    :actions="false"
    @submit="submitHandler"
  >
    <div class="form-actions-file-container">
      <form-row>
        <form-kit
          v-if="context == 'Interferencias en Aeropuertos' && fileNumber != 'A definir' && location == 'AGCCTYL'"
          type="text"
          label="Nota de Fin" 
          name="nota_fin"
          outer-class="field-report"
          inner-class="field--report"
          validation="required | validateFile"
          :validation-rules="{ validateFile }"
        />
        <form-kit
          v-if="context == 'Medición de Radiaciones No Ionizantes' && fileNumber != 'A definir' && location == 'AGCCTYL'"
          type="text"
          label="Nota de Fin" 
          name="nota_fin"
          outer-class="field-report"
          inner-class="field--report"
          validation="required | validateFile"
          :validation-rules="{ validateFile }"
        />
        <form-kit
          v-if="fileNumber !== 'A definir' && (informe === undefined || informe === null || informe === '') && fileType !=='Descargo'"
          type="text"
          label="Informe" 
          name="informe" 
          outer-class="field-report"
          validation="required | validateFile"
          :validation-rules="{ validateFile }"
        />
        <form-kit
          v-if="fileNumber != 'A definir'"
          type="select"
          :options="getAreasOptions(userArea)"
          label="Área destino"
          name="area_destino"
          placeholder="Área"
          outer-class="field-area"
        />  
        <form-kit
          v-if="fileNumber == 'A definir'"
          type="text"
          label="Expediente" 
          name="expediente" 
          outer-class="field-report"
          validation="required | validateFile"
          :validation-rules="{ validateFile }"
        />
        <button
          v-if="fileNumber != 'A definir'"
          class="submit-button"
        >
          Pase
        </button>
        <button
          v-else
          class="submit-button"
        >
          Asignar
        </button>
      </form-row>
    </div>
  </form-kit>
</template>

<style scoped>
.form-actions-file-container {
  border: 1px solid gray;
  padding: 10px 40px;
  border-radius: 50px;
  margin-top: 5px;
  margin-bottom: 5px;
  width: 100%;
  box-sizing: border-box;
}

.submit-button {
  background-color: white;
  margin: 10px 0 16px;
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
  margin-right: auto;
}

.field-area {
  width: 250px;
}
.field-report {
  width: 350px;
} 


</style>
