<script setup>
import formtc from "../components/FormTM.vue"
import { useRouter } from 'vue-router'


import { useApi} from '../composables/api'
import { reactive, onBeforeMount } from "vue";
const { currentRoute } = useRouter()


const {create_tech_measurement, getAllTechnicians, getTechMeasurement } = useApi()
const router = useRouter()
const technicians = reactive([])
const techniciansValues = reactive([])
const techMeasurement = reactive([])


onBeforeMount(async () => {
    const techResponse = await getAllTechnicians()
    const techMeasurementResponse = await getTechMeasurement(currentRoute.value.params.id)
    Object.assign(techniciansValues, techResponse)
    Object.assign(techMeasurement, techMeasurementResponse)
    
})

async function save(fields) {
  try {
    const id = currentRoute.value.params.id
    const file_id = currentRoute.value.params.file_id
    console.log("id", id)
    
    await create_tech_measurement(file_id, id, fields)
    router.push(`/file/${file_id}/station/${id}/tech_measurement`)
  } catch (error) {
    console.error(error)
  }
}
  
</script>
<template>
  <formtc
    title="Mediciones Técnicas Externas"
    :technicians-values="techniciansValues"
    :technicians="technicians"
    :tech-measurement="techMeasurement"
    @on-submit="save"
  />
</template>

<style scoped>

</style>