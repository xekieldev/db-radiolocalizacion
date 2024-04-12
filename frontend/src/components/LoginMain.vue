<script setup>
import { useSession} from '../composables/session'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import router from '../router';

import { ref } from 'vue'
// const { loggedIn } = useSession()

const { loggedIn } = useSession()


const user = ref()
const pass = ref()

console.log("Logeado?? ", loggedIn)

// async function credentials() {

//       const usuario = user.value
//       const password = pass.value
//       const credentials = {
//             usuario: 'usuario',
//             password: 'password'
//       }
//       const credentialsResponse = await checkCredentials(credentials)
//       console.log("Respuesta", credentialsResponse)
//       console.log(usuario, password)
      
  
//   }
const emit = defineEmits(['onSubmit'])

function submitHandler(fields) {
  emit('onSubmit', fields)
}


</script>

<template>
<div class="login-box">

<form-kit
    type="form"
    submit-label="Ingresar"
    :actions="false"
    @submit="submitHandler"

>
      <img class="login-img" src="../../img/Logo.png" alt="logo">
      <form-kit
            outer-class="field-login"
            type="text"
            label="Usuario"
            name="user"
            v-model="user"
      />
      <form-kit
            outer-class="field-login"
            type="password"
            label="Contraseña"
            name="pass"
            v-model="pass"
      />
      <button class="login-button" slot="submit">Ingresar</button>


</form-kit>
</div>

</template>

<style scoped>

.login-box {
      display: flex;
      flex-direction: column;
      margin: auto;
      margin-top: 10%;
      border: 1px solid gray;
      padding: 0 60px 60px;
      border-radius: 10px;
      box-shadow: 5px 5px 5px 5px gray;
      /* width: 400px; */
}

.login-img {
      margin: 0 auto;
      height: 70px;
      width: 70px;
      margin: 15px auto;
}
.field-login {
  /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
  flex: 0 0 50%;
  width: 300px;
}

.login-button {
      /* display: flex; */
      background-color: white;
      margin-top: 10px;
      padding: 10px 18px;
      border-radius: 20px;
      font-weight: 800;
      /* width: fit-content; */
      cursor: pointer;
      /* text-decoration: none; */
      border: 1px solid #007BFF;
      font-weight: 500;  
      color: #007BFF;  
      align-self: flex-end;
}
.login-button:hover {
      background-color: #007BFF;
      color: white;
}

</style>
