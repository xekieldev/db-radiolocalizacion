<script setup>
import ChangePass from '../components/FormChangePass.vue';
import { useSession } from '../composables/session'
import { useRouter } from 'vue-router';
import { ref } from 'vue'



const { changePassword } = useSession()
const router = useRouter()
const loginError = ref()

async function newPass(fields) {
  // debugger
  try {
    await changePassword(fields)
    router.push(`/`)

  } catch (error) {
    console.error(error)
    loginError.value = error
    
  }
}

</script>

<template>
  <change-pass
    :login-error="loginError"
    @on-submit="newPass"
  />
</template>

<style scoped>

</style>
