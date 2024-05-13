<script setup>
import LoginMain from '../components/LoginMain.vue';
import { useSession } from '../composables/session'
import { useRouter } from 'vue-router';
import { ref } from 'vue'



const { login } = useSession()
const router = useRouter()
const loginError = ref()

  async function check(fields) {
    try {
      await login(fields)
      router.push(`/home`)

    } catch (error) {
      console.error(error)
      loginError.value = error
      
    }

  }
</script>

<template>
  <login-main
    :login-error="loginError"
    @on-submit="check"
  />
</template>

<style scoped>

</style>
