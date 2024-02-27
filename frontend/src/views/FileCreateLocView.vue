<script setup>
import { useApi} from '../composables/api'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'
import Mapa from '../components/MapMain.vue'
import { useRouter } from 'vue-router'


// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { create , getAllTechnicians} = useApi()
const router = useRouter()



// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const file = reactive({})
const station = reactive([])
const technicians = reactive([])
const techniciansValues = reactive([])




onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
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
  <!-- <form-kit
    v-model="store.zoom"
    type="range"
    label="Zoom"
    min="14"
    max="18"
  />
  <mapa :position="[ store.lat, store.lng ]" /> -->
</template>

<style scoped>

</style>