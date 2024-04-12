<script setup>
import FormRow from './FormRow.vue'
import Heading from './Heading.vue';
import { useArea } from '../composables/area';

const emit = defineEmits(['onSubmit'])
const props = defineProps({
  context: String,
  title: String,
})
const { area } = useArea()



function submitHandler(fields) {
  emit('onSubmit', fields)
}


</script>

<template>
  <heading>{{ title }}</heading>
  <form-kit
    type="form"
    submit-label="Guardar"
    @submit="submitHandler"
    :actions="false"
  >
    <form-row>
      <form-kit
        type="text"
        label="Nombre"
        name="nombre"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Apellido"
        name="apellido" 
      />
    </form-row>
    <form-row>
      <form-kit
        type="select"
        :options="area"
        label="CCTE/Área"
        name="area" 
      />
    </form-row>
    <button class="submit-technician-button" slot="submit">Guardar</button>
  </form-kit>
</template>

  
<style scoped>

.submit-technician-button {
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

</style>
  