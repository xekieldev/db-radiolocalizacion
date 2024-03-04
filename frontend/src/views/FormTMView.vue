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


onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const fileResponse = await getFile(currentRoute.value.params.id)
    const techResponse = await getAllTechnicians()
    // console.log(currentRoute.value.params.id)
    
    // const response = getTechMeasurement(currentRoute.value.params.id)
    Object.assign(techniciansValues, techResponse)
    // Object.assign(technicians, response.technicians)
    Object.assign(file, fileResponse.file)
    console.log("fR",fileResponse.file)
    

})



async function save(fields) {
  try {
    const id = currentRoute.value.params.id
    console.log("id del path: ", id)
    const response = await create_tech_measurement(id, fields)
    console.log("id respuesta: ", response.id)
    router.push(`/file/${id}/tech_measurement`)
  } catch (error) {
    console.error(error)
  }
}
  
</script>
<template>
  <formtc
    title="Mediciones Técnicas Externas"
    :file=  "file"
    :techniciansValues="techniciansValues"
    :technicians="technicians"
    @on-submit="save"
  />
</template>

<style scoped></style>