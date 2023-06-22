<script setup>
import { useLocalStorage } from '../composables/localstorage'
import { onBeforeMount, reactive } from 'vue'

// const ls = useLocalStorage()
// debugger
// const data = ls.list()
// console.log(data)

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { list, loading } = useLocalStorage(1000)

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


</script>
<template>
  <ul>
    <li
      v-for="item in items"
      :key="item"
    >
      Expediente: {{ item.expediente }} - Área: {{ item.area }}
    </li>
    <p>Detalle local storage</p>
    <div class="status">
      <span><strong>Loading:</strong> {{ loading }}</span>
      <br>
      <span><strong>Items:</strong><br> {{ items }}</span>
      <br>
    </div>
  </ul>
</template>

<style scoped>
.status{
    background-color: lightyellow;
}
</style>