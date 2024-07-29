<script setup>
import { useApi} from '../composables/api'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import FooterMain from '../components/FooterMain.vue'



const { create , getAllTechnicians, updateRelatedStation, getStation, getFile } = useApi()
const router = useRouter()
const { currentRoute } = useRouter()

const file = reactive({})
const expediente = ref()
const station = reactive({})
const technicians = reactive([])
const techniciansValues = reactive([])


onBeforeMount(async () => {
    const techResponse = await getAllTechnicians()
    Object.assign(techniciansValues, techResponse)
    const file_response = await getFile(currentRoute.value.params.id)
    Object.assign(file, file_response.file)
    expediente.value = file.expediente
    
})

async function save(fields) {
  try {
    const file_id = currentRoute.value.params.id
    const response = await create(file_id, fields)
    const station = await getStation(response.id_station)

    if( station.station.related_station_id != null || station.station.related_station_id != undefined) {
      
      await updateRelatedStation(file_id, station.station.related_station_id, station.station.id)  
      
    }
    router.push(`/file/${file_id}/station/${response.id_station}`)
    
  } catch (error) {
    console.error(error)
  }
  
}

</script>

<template>
  <frloc
    title="Datos de Radiolocalización"
    context="Radiolocalizacion" 
    :file="file"
    :station="station"
    :technicians="technicians"
    :technicians-values="techniciansValues"
    
    @on-submit="save"
  />
  <footer-main/>
</template>

<style scoped>

</style>