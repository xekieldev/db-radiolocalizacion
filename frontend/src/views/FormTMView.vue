<script setup>
import formtc from "../components/FormTM.vue"
import { useRouter } from 'vue-router'


import { useApi} from '../composables/api'
import { reactive, onBeforeMount } from "vue";
const { currentRoute } = useRouter()


const {create_tech_measurement, getAllTechnicians, getTechMeasurement, getFile} = useApi()
const router = useRouter()
const file = reactive({})
const technicians = reactive([])
const techniciansValues = reactive([])
const techMeasurement = reactive([])


onBeforeMount(async () => {
    const fileResponse = await getFile(currentRoute.value.params.id)
    const techResponse = await getAllTechnicians()
    const techMeasurementResponse = await getTechMeasurement(currentRoute.value.params.id)
    Object.assign(techniciansValues, techResponse)
    Object.assign(file, fileResponse.file)
    Object.assign(techMeasurement, techMeasurementResponse)
})

async function save(fields) {
  try {
    const id = currentRoute.value.params.id
    const response = await create_tech_measurement(id, fields)
    router.push(`/file/${id}/tech_measurement`)
  } catch (error) {
    console.error(error)
  }
}
  
</script>
<template>
  <formtc
    title="Mediciones Técnicas Externas"
    :file="file"
    :techniciansValues="techniciansValues"
    :technicians="technicians"
    :techMeasurement="techMeasurement"
    @on-submit="save"
  />
</template>

<style scoped>

</style>