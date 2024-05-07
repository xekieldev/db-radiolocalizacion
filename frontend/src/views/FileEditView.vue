<script setup>
import { useApi} from '../composables/api'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'
import Mapa from '../components/MapMain.vue'
import { useRouter } from 'vue-router'


const { getFile, getAllTechnicians, edit } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()


const file = reactive({})
const station = reactive({})
const techniciansValues = reactive([])
const technicians = reactive([])

onBeforeMount(async () => {
    const response = await getFile(currentRoute.value.params.id)  
    const techResponse = await getAllTechnicians()
    Object.assign(file, response.file)
    Object.assign(station, response.station)
    Object.assign(techniciansValues, techResponse)
    Object.assign(technicians, response.technicians)    
})

async function save(fields) {
  try {
    const id = currentRoute.value.params.id  
    const response = await edit(id, fields)        
    router.push(`/file/${response.id_file}`)
  } catch (error) {
    console.error(error)
  } 
}

</script>

<template>
  <frloc v-if="station.provincia"
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