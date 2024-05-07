<script setup>
import LoginMain from '../components/LoginMain.vue';
import { useSession } from '../composables/session'
import { useRouter } from 'vue-router';



const { login, loggedIn } = useSession()
const router = useRouter()


  async function check(fields) {
    try {
      const response = await login(fields)
      router.push(`/home`)

    } catch (error) {
      console.log(error)
      
    }

  }
</script>

<template>
  
  <login-main
  @on-submit="check"
  />
  
</template>

<style scoped>

</style>
