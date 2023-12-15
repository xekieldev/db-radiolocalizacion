<script setup>
// import { useLocalStorage } from '../composables/localstorage'
import { useApi } from '../composables/api'
import { onMounted, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'



// const ls = useLocalStorage()
// debugger
// const data = ls.list()
// console.log(data)

// El 1000 es la cantidad de milisegundos que se tardarán
// en responder los métodos. Esto es para emular la naturaleza
// asíncrona que vas a tener cuando uses un API HTTP.
const { getFile, loading } = useApi()
const { currentRoute } = useRouter()

// El reactive es para que la variable items se actualice
// automáticamente cuando cambia. Es necesario porque acá se
// inicializa como una lista vacía y más abajo se hace la llamada
// al método que tarda 1000ms. Cuando la respuesta del método llega
// el valor de la variable se actualiza automáticamente en el
// template sin necesidad de que su valor sea reasignado
const items = reactive([])

onMounted(async () => {
    // El await acá es necesario para representar que se está
    // haciendo una llamada a un método asíncrono
// debugger
    const data = await getFile(currentRoute.value.params.id)
    items.push(data)
})


</script>
<template>
  {{ items }}
  <RouterLink to="/list">Volver</RouterLink>
</template>

<style scoped>
.status{
    background-color: lightyellow;
}
</style>