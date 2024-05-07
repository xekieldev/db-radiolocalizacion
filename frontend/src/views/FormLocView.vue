<script setup>
import { useLocalStorage } from '../composables/localstorage'
import Floc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'
import Mapa from '../components/MapMain.vue'


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
  <floc
    title="Datos de Localización"
    context="Localizacion"
    @on-submit="save"
  />
  <mapa :position="[47.313220, -1.319482]" />
</template>

<style scoped>

</style>