<script setup>
import { useApi } from '../composables/api'
import { onMounted, reactive } from 'vue'
import { RouterLink, useRouter } from 'vue-router'


const { getStation } = useApi()
const { currentRoute } = useRouter()

const items = reactive([])

onMounted(async () => {
    const data = await getStation(currentRoute.value.params.id)
    items.push(data)
})


</script>
<template>
  {{ items }}
  <RouterLink to="/list">
    Volver
  </RouterLink>
</template>

<style scoped>
.status{
    background-color: lightyellow;
}
</style>