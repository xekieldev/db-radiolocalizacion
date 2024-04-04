<script setup>
import { useSession} from '../composables/session'
import MyButton from '../components/MyButton.vue';
import { RouterLink, useRouter } from 'vue-router'


const router = useRouter()

const { logout, loggedIn, updateLoggedIn } = useSession()

async function doLogout() {
  const response = await logout()
  router.push('/')
}

const intervalID = setInterval(updateLoggedIn, 500);

// function myCallback() {
//   // Your code here
//   // Parameters are purely optional.
//   updateLoggedIn()
// }

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
                  <RouterLink to="/" v-if="!loggedIn">
                  Login
                  </RouterLink>
                  <RouterLink to="/home" v-if="loggedIn">
                  Home
                  </RouterLink>
                  <RouterLink to="/list?includeDeleted=false" v-if="loggedIn">
                  Expedientes
                  </RouterLink>
                  <RouterLink to="/station?includeDeleted=false" v-if="loggedIn">
                  Estaciones
                  </RouterLink>
                  <RouterLink to="/list_technicians" v-if="loggedIn">
                  Técnicos
                  </RouterLink>
                  <RouterLink to="/about" v-if="loggedIn">
                  About
                  </RouterLink>
                  </nav>

                  <my-button @on-tap="() => doLogout()" class="tertiary logout-button" label="Salir" v-if="loggedIn"></my-button>

            </header>
      </div>
</template>
  
  
  <style scoped>
    
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
  .logout-button {
      height: 34px; 
      margin-top: 5px;
  }
  </style>
