<script setup>

import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { Bar } from 'vue-chartjs'


const props = defineProps({
title: String,
chartData: Object,
})

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


</script>
<template>
    <Bar :data="chartData" :options="{
      plugins: {
        legend: {
          display: false,
          position: 'bottom',
          labels: {
            color: '#333', // Color de los labels
            font: {
              size: 10 // Tamaño de la fuente de los labels
            }
          }
        },
      },

      scales: {
        y: {
          beginAtZero: true, // Empieza desde cero
          ticks: {
            stepSize: 500, // Intervalos entre valores
            color: '#111', // Color de los números del eje
            font: {
              size: 8 // Tamaño de la fuente de los números del eje
            },
          },
        },
      },
      responsive: true,
      maintainAspectRatio: false
    }"/>
</template>

<style scoped>

</style>
