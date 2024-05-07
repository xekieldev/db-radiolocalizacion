<script setup>
import { useApi} from '../composables/api'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'
import { useRouter } from 'vue-router'


const { create , getAllTechnicians} = useApi()
const router = useRouter()
const file = reactive({})
const station = reactive([])
const technicians = reactive([])
const techniciansValues = reactive([])




onBeforeMount(async () => {
    const techResponse = await getAllTechnicians()
    Object.assign(techniciansValues, techResponse)
})

async function save(fields) {
  try {
    const response = await create(fields)
    router.push(`/file/${response.id_file}`)
  } catch (error) {
    console.error(error)
  }
  
}

</script>

<template>
  <frloc
    title="Datos de Localización"
    context="Localizacion" 
    :file="file"
    :station="station"
    :technicians="technicians"
    :technicians-values="techniciansValues"
    
    @on-submit="save"
  />
</template>

<style scoped>

</style>