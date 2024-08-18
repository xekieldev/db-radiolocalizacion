<script setup>
import FormRow from './FormRow.vue'
import { useArea } from '../composables/area'


const emits = defineEmits(['onSubmit'])
const { area } = useArea()


function submitHandler(fields) {
  emits('onSubmit', fields)
}

const props = defineProps({
  context: String,
  fileNumber: String,
  location: String,
  informe: String,
})

</script>

<template>
  <form-kit
  type="form"
  :actions="false"
  @submit="submitHandler"
  >
    <div class="form-end-file-container">
      <form-row>
        <form-kit
          v-if="context == 'Interferencias en Aeropuertos' && fileNumber != 'A definir' && location == 'AGCCTYL'"
          type="text"
          label="Nota de Fin" 
          name="nota_fin"
          outer-class="field-report"
          inner-class="field--report"
        />
        <form-kit
          v-if="fileNumber !== 'A definir' && (informe === undefined || informe === null || informe === '')"
          type="text"
          label="Informe" 
          name="informe" 
          outer-class="field-report"
        />
        <form-kit
          v-if="fileNumber != 'A definir'"
          type="select"
          :options="area"
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
.form-end-file-container {
  border: 1px solid gray;
  padding: 10px 40px;
  border-radius: 50px;
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
}

.field-area {
  flex: 0 0 200px;
}

</style>
