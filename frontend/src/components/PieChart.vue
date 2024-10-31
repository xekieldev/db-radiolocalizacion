<script setup>

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'


const props = defineProps({
title: String,
chartData: Object,
})

ChartJS.register(ArcElement, Tooltip, Legend)


</script>
<template>
    <Pie :data="chartData" :options="{
      plugins: {
        legend: {
          display: true,
          position: 'bottom',
          labels: {
            color: '#333', // Color de los labels
            font: {
              size: 10 // Tamaño de la fuente de los labels
            }
          }
        }
      },
      responsive: true,
      maintainAspectRatio: false
    }"/>
</template>

<style scoped>

</style>
