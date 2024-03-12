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
  </form-kit>
</template>

  
<style scoped>

</style>
  