<script setup>
import Fnewfile from '../components/FormNewFile.vue'
import { onBeforeMount, reactive } from 'vue'
import { useApi } from '../composables/api'
import { useRouter } from 'vue-router'


const { create_non_ionizing_radiation, newFile, getAllTechnicians } = useApi()
const router = useRouter()
const technicians = reactive([])
const techniciansValues = reactive([])

onBeforeMount(async () => {
    const techResponse = await getAllTechnicians()
    Object.assign(techniciansValues, techResponse)
})

async function save(fields) {
  try {
    if( fields.tipo != 'Medición de Radiaciones No Ionizantes (móviles)') {
      fields.area_destino = fields.area
      const response = await newFile(fields)
      router.push(`/file/${response.id}`)
    } else {
      const response = await newFile(fields)
      console.log("file", response.id)
      console.log(fields)
      
      await create_non_ionizing_radiation(response.id, fields)
      router.push(`/list_non_ionizing_radiation/`)
    }
    
    
  } catch (error) {
    console.error(error)
  }  
}
</script>

<template>
  <fnewfile
    title="Alta Expediente"
    context="Expedientes" 
    :technicians = "technicians"
    :techniciansValues = "techniciansValues"
    @on-submit="save"
  />
</template>

<style scoped>


</style>