<script setup>
import { ref, watch } from 'vue'
import FooterMain from '../components/FooterMain.vue'
import StatisticsMain from '../components/StatisticsMain.vue'
import { useRouter } from 'vue-router'


const items = ref({})
const router = useRouter()
const type = ref(router.currentRoute.value.query.type)
const selectedArea = ref(null)
const startDate = ref(router.currentRoute.value.query.startDate)
const endDate = ref(router.currentRoute.value.query.endDate)

watch(()=> router, (newValue, oldValue) => {
  console.log(newValue)
  type.value = newValue.currentRoute.value.query.type
  startDate.value = newValue.currentRoute.value.query.startDate
  endDate.value = newValue.currentRoute.value.query.endDate
  selectedArea.value = newValue.currentRoute.value.query.area

  
}, {deep: true})

</script>
<template>
  <statistics-main
    title="Estadísticas"
    :items="items"
    :type="type"
    :selectedArea="selectedArea"
    :startDate="startDate"
    :endDate="endDate"
  />
 
  <footer-main class="footer-main" />

</template>

<style scoped>



</style>