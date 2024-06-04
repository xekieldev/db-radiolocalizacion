<script setup>
import { useSession} from '../composables/session'
import MyButton from '../components/MyButton.vue';
import { RouterLink, useRouter } from 'vue-router'


const router = useRouter()
const { logout, loggedIn, updateLoggedIn } = useSession()

async function doLogout() {
  await logout()
  router.push('/')
}

setInterval(updateLoggedIn, 500);

</script>

<template>
  <div>
    <header>
      <img
        alt="ENACOM logo"
        class="logo"
        src="../../img/Logo.png"
        width="100"
        height="100"
      >
      <nav>
        <RouterLink
          v-if="!loggedIn"
          to="/"
        >
          Login
        </RouterLink>
        <RouterLink
          v-if="loggedIn"
          to="/home"
        >
          Home
        </RouterLink>
        <RouterLink
          v-if="loggedIn"
          to="/list?includeDeleted=false"
        >
          Expedientes
        </RouterLink>
        <RouterLink
          v-if="loggedIn"
          to="/station?includeDeleted=false"
        >
          Estaciones
        </RouterLink>
        <RouterLink
          v-if="loggedIn"
          to="/list_technicians"
        >
          Técnicos
        </RouterLink>
        <RouterLink
          v-if="loggedIn"
          to="/about"
        >
          About
        </RouterLink>
      </nav>
      <my-button
        v-if="loggedIn"
        class="tertiary logout-button"
        label="Salir"
        @on-tap="() => doLogout()"
      />
    </header>
  </div>
</template>

<style scoped>
header {
    display: flex;
    flex-direction: row;
    background: linear-gradient(to right, white 0%, #cacaca 25%, #cacaca 75%, white 100%);
    width: 100%;
  
  }
  
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
  .logout-button {
      height: 34px; 
      margin-top: 5px;
  }

  </style>
