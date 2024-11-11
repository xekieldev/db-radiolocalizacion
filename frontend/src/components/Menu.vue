<script setup>
import { useSession} from '../composables/session'
import MyButton from '../components/MyButton.vue';
import { RouterLink, useRouter } from 'vue-router'
import { loggedIn, usuario, perfil } from '../composables/loginstatus'

const router = useRouter()
const { logout } = useSession()

async function doLogout() {
  await logout()
  router.push('/')
}

</script>

<template>
  <div>
    <header>
      <img
        alt="ENACOM logo"
        class="logo"
        src="../../img/new_logo.png"
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
          to="/statistics?type=pending"
        >
          Estadísticas
        </RouterLink>
        <RouterLink
          v-if="loggedIn"
          to="/station?includeDeleted=false"
        >
          Estaciones
        </RouterLink>
        <RouterLink
          v-if="loggedIn"
          to="/list_non_ionizing_radiation"
        >
          RNI
        </RouterLink>
        <RouterLink
          v-if="loggedIn && perfil == 'coordinator'"
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
      <div
        v-if="loggedIn"
        class="menu-name"
      >
        <p>Hola,</p>
        <a
          title="Cambiar contraseña"
          href="/change_password"
        >{{ usuario }}</a>
      </div>
      <my-button
        v-if="loggedIn"
        class="tertiary logout-button"
        label="Salir"
        @on-tap="doLogout"
      />
    </header>
  </div>
</template>

<style scoped>
header {
    display: flex;
    flex-direction: row;
    /* background: linear-gradient(to right, white 0%, #cacaca 25%, #cacaca 75%, white 100%); */
    width: 100%;
    border-bottom: 1px solid #0B1742;
    /* margin-bottom: 15px; */
  
  }
  
nav {
    width: 100%;
    font-size: 15px;
    text-align: left;
    margin-top: 2rem;
    margin-left: 50px;
  }
  
  nav a.router-link-exact-active {
    color: #005297;
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
      /* height: 34px;  */
      margin-top: 5px;
  }

  .menu-name {
    display: flex;
    padding: 7px;
    gap: 3px;
  }
  .logo {
    height: 90px;
  }
  </style>
