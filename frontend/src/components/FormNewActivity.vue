<script setup>
import FormRow from './FormRow.vue'
import { ref } from 'vue'

const emits = defineEmits(['onSubmit'])
const activityDate = ref('')
const activityText = ref('')

function submitHandler(fields) {
  emits('onSubmit', fields)
  activityDate.value = ''
  activityText.value = ''
}

</script>

<template>
  <form-kit
    type="form"
    :actions="false"
    @submit="submitHandler"
  >
    <div class="activities-container">
      <h2 class="activity-title">
        Actividades
      </h2>
      <div class="new-activity">
        <form-row>
          <form-kit
            v-model="activityDate"
            type="date"
            label="Fecha" 
            name="fecha" 
            validation="date_after:04-30-2024"
            validation-visibility="live"
            :validation-messages="{
              date_after: 'La fecha debe ser posterior al 01/05/2024.',
            }"
            outer-class="field-date"
          />
          <form-kit
            v-model="activityText"
            type="text"
            label="Detalle" 
            name="detalle" 
            help="Detalle de las tareas o actividades durante la ejecución del expediente. Máximo 500 caracteres."
          />
          <button
            class="submit-button"
          >
            Agregar
          </button>
        </form-row>
      </div>
    </div>
  </form-kit>
</template>

<style scoped>
.activities-container {
  display: flex;
  flex-direction: column;
  border-top: solid 1px gray;

  
}
.activity-title {
  font-size: 20px;
  padding: 10px;
  align-self: center;
  font-weight: 500;
}

.field-date {
  flex: 0 0 20%;
}
.submit-button {
      background-color: white;
      margin: 8px 0 16px;
      padding: 10px 18px;
      border-radius: 20px;
      cursor: pointer;
      border: 1px solid #007BFF;
      font-weight: 600;  
      color: #007BFF;  
      align-self: center

}
.submit-button:hover {
      background-color: #007BFF;
      color: white;
}
</style>
