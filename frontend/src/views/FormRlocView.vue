<script setup>
import { useLocalStorage } from '../composables/localstorage'
import Fest from '../components/Form.vue'
import { onBeforeMount, reactive } from 'vue'

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { create, list, loading } = useLocalStorage(1000)

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
    const newData = await create(fields)
    items.splice(0, items.length)
    const data = await list()
    items.push(...data)
    
  } catch (error) {
  
  }
  
}
</script>

<template>
  <fest
    @on-submit="save"
    title="Planilla de Radiolocalización" 
    context="Radiolocalizacion"/>
    <div class="status">
      <span><strong>Loading:</strong> {{ loading }}</span>
      <span><strong>Items:</strong> {{ items}}</span>
    </div>
</template>

<style scoped>

</style>