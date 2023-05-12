<script setup>
import { useApi } from '../composables/api'
import FormRow from '../components/FormRow.vue'

const submitHandler = async (fields) => {
  console.log(fields)
  const api = useApi()
  const all = await api.list()
  console.log(all)
  api.create(fields)
  
}
const prueba = [{
  value:'opcion1',
  label:'Opcion 1'},
  {
  value:'opcion2',
  label:'Opcion 2'}]
</script>

<template>
  <form-kit type="form" @submit="submitHandler">
    <form-row>
      <form-kit type="date" label="Date" name="fecha" />
      <form-kit type="select" label="Text" name="text" :options="prueba" />

      <form-kit type="text" label="Text2" name="text" />
    </form-row>
    <form-row>
      <form-kit type="date" label="Date" name="fecha" />
      <form-kit type="text" label="Text" name="text" />
      <form-kit type="text" label="Text2" name="text" />
    </form-row>
  </form-kit>
</template>

  
<style>
@media (min-width: 1024px) {
  .form {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
  