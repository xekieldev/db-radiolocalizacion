<script setup>
import { useApi} from '../composables/api'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'
import { useRouter } from 'vue-router'
import FooterMain from '../components/FooterMain.vue'


const { create , getAllTechnicians} = useApi()
const router = useRouter()
const { currentRoute } = useRouter()
const station = reactive([])
const technicians = reactive([])
const techniciansValues = reactive([])


onBeforeMount(async () => {
    const techResponse = await getAllTechnicians()
    Object.assign(techniciansValues, techResponse)
})

async function save(fields) {
  try {
    const file_id = currentRoute.value.params.id
    const response = await create(file_id, fields)
    router.push(`/file/${file_id}/station/${response.id_station}`)
  } catch (error) {
    console.error(error)
  }
  
}

</script>

<template>
  <frloc
    title="Datos de Localización"
    context="Localizacion" 
    :station="station"
    :technicians="technicians"
    :technicians-values="techniciansValues"
    @on-submit="save"
  />
  <footer-main/>
</template>

<style scoped>

</style>