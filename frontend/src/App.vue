<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MyButton from './components/MyButton.vue'
import { useRouter } from 'vue-router'
import { useSession } from './composables/session'
import { computed } from 'vue'
import BarMenu from './components/Menu.vue'

const router = useRouter()
const { logout, loggedIn } = useSession()


// const isLoggedIn = computed(() => {
//       return loggedIn.value;
//     });

// function checkAuth() {
    
//   if(document.cookie.split('=')[0] == 'appAuth') {
//     return true
//   } else return false
// }

// const cookie = document.cookie
// console.log("cookie: ", cookie)


// async function logout2() {
//   const response = await logout()

//   router.push('/login')
// }

</script>

<template>
  <div class="wrapper">
    <bar-menu></bar-menu>

<RouterView />

  </div>
    
</template>


<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  width: 900px;
  margin: 0 auto;

}

header {
  display: flex;
  flex-direction: row;
  background: linear-gradient(to right, rgba(202, 202, 202, 0), #cacaca, rgba(202, 202, 202, 0));
  width: 100%;

}

/* .logo {
  display: block;
  margin: 0 auto 2rem;
} */

nav {
  width: 100%;
  font-size: 15px;
  text-align: left;
  margin-top: 2rem;
  margin-left: 50px;
}

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
}
</style>
