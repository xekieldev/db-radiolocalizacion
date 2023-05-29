<script setup>
import { useLocalStorage } from '../composables/localstorage'

const ls = useLocalStorage()
const data = ls.list()
console.log(data)

</script>
<template>
    <ul>
        <li v-for="item in data">Expediente: {{ item.expediente }} - Área: {{ item.area }}</li>
    </ul>
</template>

<style scoped></style>