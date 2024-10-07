<script setup>
import { RouterView } from 'vue-router'
import BarMenu from './components/Menu.vue'
import { onMounted } from 'vue'
import { useSession } from './composables/session'
import { loggedIn, usuario, userData, perfil } from './composables/loginstatus'
import { printFlag } from './composables/printflag'

const { checkUser } = useSession()


onMounted(async() => {
    const response = await checkUser()
    userData.value = response
    
    loggedIn.value = response.loggedIn
    usuario.value = response.usuario
    perfil.value = response.perfil
})

</script>

<template>
  <div :class="['wrapper', { 'wrapper-to-print': printFlag.isActive}]">
    <bar-menu />
    <RouterView />
  </div>
</template>


<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  width: 95vw;
  margin: 0 auto;
  min-height: 100vh;
  padding: 1px;
  /* font-size: 11px; */
}

.wrapper-to-print {
  display: flex;
  flex-direction: column;
  width: 1000px;
  margin: 0 auto;
  min-height: 100vh;
  padding: 1px;
}

header {
  display: flex;
  flex-direction: row;
  background: linear-gradient(to right, rgba(202, 202, 202, 0), #cacaca, rgba(202, 202, 202, 0));
  width: 100%;
}

/* nav {
  width: 1050%;
  font-size: 15px;
  text-align: left;
  margin-top: 2rem;
  margin-left: auto;
} */
/* 
nav a.router-link-exact-active {
  color: #426aaf;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
  color: black;
  text-decoration: none;
  font-weight: 700;
}

nav a:hover {
  color: rgb(255, 136, 0);
}
nav a:first-of-type {
  border: 0;
} */

</style>
