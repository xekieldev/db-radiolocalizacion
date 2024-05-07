<script setup>
import { useLocalStorage } from '../composables/localstorage'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'


const { create, list } = useLocalStorage(1000)

const items = reactive([])


onBeforeMount(async () => {
    const data = await list()
    items.push(...data)
})

async function save(fields) {
  try {
    await create(fields)
    items.splice(0, items.length)
    const data = await list()
    items.push(...data)  
  } catch (error) {
    console.error(error)
  } 
}

</script>

<template>
  <frloc
    title="Datos de Radiolocalización"
    context="Radiolocalizacion" 
    @on-submit="save"
  />
</template>

<style scoped>

</style>