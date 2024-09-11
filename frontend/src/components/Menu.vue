<script setup>
import { useSession} from '../composables/session'
import MyButton from '../components/MyButton.vue';
import { RouterLink, useRouter } from 'vue-router'
import { ref, onUpdated, onMounted } from 'vue'
import { loggedIn, usuario } from '../composables/loginstatus'


const router = useRouter()
const { logout, checkUser, updateLoggedIn } = useSession()
const user_perfil = ref('')


async function doLogout() {
  const response = await logout()
  
  router.push('/')
}

onMounted( async ()=> {
    const response = await checkUser()
    loggedIn.value = response.data.loggedIn
})
onUpdated( async ()=> {
    const response = await checkUser()
    usuario.value = response.data.user_usuario
    user_perfil.value = response.data.user_perfil

})
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
          to="/list_non_ionizing_radiation"
        >
          RNI
        </RouterLink>
        <RouterLink
          v-if="loggedIn && user_perfil == 'coordinator'"
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
      <div class="menu-name"  v-if="loggedIn">
        <p>Hola,</p>
        <a title="Cambiar contraseña" href="/change_password">{{ usuario }}</a>

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
      /* height: 34px;  */
      margin-top: 5px;
  }

  .menu-name {
    display: flex;
    padding: 7px;
    gap: 3px;
  }
  </style>
