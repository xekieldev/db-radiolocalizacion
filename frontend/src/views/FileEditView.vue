<script setup>
import { useApi} from '../composables/api'
import FFile from '../components/FormNewFile.vue'
import { onBeforeMount, reactive } from 'vue'
import { useRouter } from 'vue-router'


const { getFile, editFile, getNIRMeasurementInFile, getAllTechnicians } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()


const file = reactive({})
const nirMeas = reactive({})
const techniciansValues = reactive([])
const technicians = reactive([])

onBeforeMount(async () => {
  const id = currentRoute.value.params.id
  const response = await getFile(id)
  const nir_response = await getNIRMeasurementInFile(id)
  const techResponse = await getAllTechnicians()
  Object.assign(file, response.file)  
  Object.assign(nirMeas, nir_response[0])
  Object.assign(techniciansValues, techResponse)  

})

async function save(fields) {
  try {
    const id = currentRoute.value.params.id
    const response = await editFile(id, fields)      
    router.push(`/file/${response.id}`)
  } catch (error) {
    console.error(error)
  } 
}

</script>

<template>
  <f-file
    title="Editar Expediente"
    context="Radiolocalizacion" 
    :file="file"
    :nir-meas="nirMeas"
    :technicians="technicians"
    :technicians-values="techniciansValues"
    @on-submit="save"
  />
</template>

<style scoped>

</style>