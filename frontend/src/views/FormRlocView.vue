<script setup>
import { useLocalStorage } from '../composables/localstorage'
import Fest from '../components/Form.vue'

const save = async (fields) => {
  const ls = useLocalStorage()
  ls.create(fields)
}

</script>

<template>
  <fest
    @on-submit="save"
    title="Planilla de Radiolocalización" 
    context="Radiolocalizacion"/>
</template>

<style scoped>

</style>