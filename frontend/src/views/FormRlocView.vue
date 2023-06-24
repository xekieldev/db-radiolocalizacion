<script setup>
import { useLocalStorage } from '../composables/localstorage'
import Frloc from '../components/FormMain.vue'
import { onBeforeMount, reactive } from 'vue'
import Mapa from '../components/MapMain.vue'
import { useRlocFormData } from '../composables/rloc-form-data'

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { create, list } = useLocalStorage(1000)

// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const items = reactive([])
// const { lat, lng, zoom } = useRlocFormData()
const store = useRlocFormData()




onBeforeMount(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
    const data = await list()
    items.push(...data)
})

async function save(fields) {
  try {
    await create(fields)
    items.splice(0, items.length)
    const data = await list()
    items.push(...data)
    
  } catch (error) {
    console.error(error)
  }
  
}
</script>

<template>
  <frloc
    title="Datos de Radiolocalización"
    context="Radiolocalizacion" 
    @on-submit="save"
    
  />
  <form-kit
        v-model="store.zoom"
        type="range"
        label="Zoom"
        min="14"
        max="18"
  />
  <mapa :position="[ store.lat, store.lng ]" />
</template>

<style scoped>

</style>