<script setup>
import Fnewtechnician from '../components/FormNewTechnician.vue'
import { onBeforeMount, reactive } from 'vue'
import { useApi } from '../composables/api'
import { useRouter } from 'vue-router'


// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { create_technician, list } = useApi()
const router = useRouter()


// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const items = reactive([])


onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const data = await list()
    items.push(...data)
})

async function save(fields) {
  try {
    const response = await create_technician(fields)
    router.push(`/list_technicians`)
  } catch (error) {
    console.error(error)
  }
  
}
</script>

<template>
  <fnewtechnician
    title="Nuevo Técnico"
    context="Técnicos" 
    @on-submit="save"
  />
</template>

<style scoped>


</style>