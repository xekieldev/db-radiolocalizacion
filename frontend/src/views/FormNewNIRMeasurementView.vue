<script setup>
import FormNewNIR from '../components/FormNewNIRMeasurement.vue'
import { onBeforeMount, reactive } from 'vue'
import { useApi } from '../composables/api'
import { useRouter } from 'vue-router'


const { create_non_ionizing_radiation, getAllTechnicians } = useApi()
const router = useRouter()
const file = reactive({})
const station = reactive([])
const technicians = reactive([])
const techniciansValues = reactive([])

// const items = reactive([])

// onBeforeMount(async () => {
//     const data = await list()
//     items.push(...data)
// })
onBeforeMount(async () => {
    const techResponse = await getAllTechnicians()
    Object.assign(techniciansValues, techResponse)
})


async function save(fields) {
  try {
    await create_non_ionizing_radiation(fields)
    router.push(`/list_non_ionizing_radiation/`)
  } catch (error) {
    console.error(error)
  }  
}
</script>

<template>
  <FormNewNIR
    title="Nueva Medición de RNI Móvil"
    context="RNI" 
    :technicians = "technicians"
    :techniciansValues = "techniciansValues"
    @on-submit="save"
  />
</template>

<style scoped>


</style>