<script setup>
import Fnewtechnician from '../components/FormNewTechnician.vue'
import { onBeforeMount, reactive } from 'vue'
import { useApi } from '../composables/api'
import { useRouter } from 'vue-router'


const { create_technician, list } = useApi()
const router = useRouter()

const items = reactive([])

onBeforeMount(async () => {
    const data = await list()
    items.push(...data)
})

async function save(fields) {
  try {
    await create_technician(fields)
    router.push(`/list_technicians`)
  } catch (error) {
    console.error(error)
  }  
}
</script>

<template>
  <fnewtechnician
    title="Nuevo Técnico"
    context="Técnicos" 
    @on-submit="save"
  />
</template>

<style scoped>


</style>