<script setup>
import { ref, watch } from 'vue'
import FooterMain from '../components/FooterMain.vue'
import StatisticsMain from '../components/StatisticsMain.vue'
import { useRouter } from 'vue-router'
import PieChart from '../components/PieChart.vue'


const items = ref({})
const router = useRouter()
const type = ref(router.currentRoute.value.query.type)
const selectedArea = ref(null)
const startDate = ref(router.currentRoute.value.query.startDate)
const endDate = ref(router.currentRoute.value.query.endDate)

watch(()=> router, (newValue, oldValue) => {
  type.value = newValue.currentRoute.value.query.type
  startDate.value = newValue.currentRoute.value.query.startDate
  endDate.value = newValue.currentRoute.value.query.endDate
  selectedArea.value = newValue.currentRoute.value.query.area

  
}, {deep: true})

</script>
<template>
  <div class="statistics-view">
    <statistics-main
    title="Estadísticas"
    :items="items"
    :type="type"
    :selectedArea="selectedArea"
    :startDate="startDate"
    :endDate="endDate"
    />

 
  </div>
  
  <footer-main class="footer-main" />

</template>

<style scoped>

.footer-main {
  margin-top: auto;
  margin-bottom: 0;
}

</style>