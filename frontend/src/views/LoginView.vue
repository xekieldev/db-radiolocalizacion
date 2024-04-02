<script setup>
import LoginMain from '../components/LoginMain.vue';
import { useSession } from '../composables/session'
import { useRouter } from 'vue-router';



const { login, loggedIn } = useSession()
const router = useRouter()


// async function check(fields) {
//   try {
//     const response = await checkCredentials(fields)
//     const fechaActual = new Date()
//     const expira = new Date(fechaActual.getTime() + (30 * 60 * 1000))
//     const expiraGMT = expira.toGMTString()
//     console.log("Expira: ", expiraGMT)

//     document.cookie = `appAuth=${response}; expires=${expiraGMT}`
//     router.push(`/`)
//   } catch (error) {
//     console.log("error", error)
//   }
  
// }
//  console.log("Estado login? ", loggedIn.value)
 

  async function check(fields) {
    try {
      const response = await login(fields)
      console.log("cookie creada")
      
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

</style>../composables/session
