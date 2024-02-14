<script setup>
import FormRow from './FormRow.vue'

const emit = defineEmits(['onSubmit'])
const props = defineProps({
  context: String,
  title: String,
})


function submitHandler(fields) {
  emit('onSubmit', fields)
}


</script>

<template>
  <h2>{{ title }}</h2>
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
  </form-kit>
</template>

  
<style scoped>

</style>
  