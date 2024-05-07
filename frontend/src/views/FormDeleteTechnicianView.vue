<script setup>
import { onBeforeMount, reactive } from 'vue'
import { useApi } from '../composables/api'
import { useRouter } from 'vue-router'


const { delete_technician, list } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()

const items = reactive([])

onBeforeMount(async () => {
    const data = await list()
    items.push(...data)
})

async function save() {
  try {
    const id = currentRoute.value.params.id
    const response = await delete_technician(id)
    router.push(`/technician/${response.id}/delete_technician`)
  } catch (error) {
    console.error(error)
  }
  
}
</script>

<template>
  <p>¿Estás seguro que quieres eliminar el técnico?</p>
  <button @click="save">Borrar</button>
  
</template>

<style scoped>

</style>