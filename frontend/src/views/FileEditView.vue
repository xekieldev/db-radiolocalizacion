<script setup>
import { useApi} from '../composables/api'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'
import Mapa from '../components/MapMain.vue'
import { useRouter } from 'vue-router'


// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getFile, getAllTechnicians, edit } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()



// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const file = reactive({})
const station = reactive({})
const techniciansValues = reactive([])
const technicians = reactive([])

onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const response = await getFile(currentRoute.value.params.id)  
    const techResponse = await getAllTechnicians()
    Object.assign(file, response.file)
    Object.assign(station, response.station)
    Object.assign(techniciansValues, techResponse)
    Object.assign(technicians, response.technicians)
    console.log(file)
    
})

console.log("lakhjd", typeof(station))

async function save(fields) {
  try {
    const id = currentRoute.value.params.id
    console.log("Id Edit: ", id)
    
    const response = await edit(id, fields)
    console.log(response)
    
    
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