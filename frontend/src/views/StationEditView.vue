<script setup>
import { useApi} from '../composables/api'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'
import { useRouter } from 'vue-router'


const { getStation, getAllTechnicians, edit, getFile } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()


const file = reactive({})
const station = reactive({})
const techniciansValues = reactive([])
const technicians = reactive([])

onBeforeMount(async () => {
    const response = await getStation(currentRoute.value.params.id)  
    const techResponse = await getAllTechnicians()
    Object.assign(station, response.station)
    Object.assign(techniciansValues, techResponse)
    Object.assign(technicians, response.technicians)    
    const file_response = await getFile(station.file_id)
    Object.assign(file, file_response.file)

})

async function save(fields) {
  try {
    const id = currentRoute.value.params.id
    const file_id = currentRoute.value.params.file_id
    const response = await edit(file_id, id, fields)        
    router.push(`/file/${response.file_id}/station/${response.station_id}`)
  } catch (error) {
    console.error(error)
  } 
}

</script>

<template>
  <frloc
    v-if="station.provincia"
    title="Datos de Radiolocalización"
    context="Radiolocalizacion" 
    :file="file"
    :station="station"
    :technicians="technicians"
    :technicians-values="techniciansValues"
    @on-submit="save"
  />
</template>

<style scoped>

</style>