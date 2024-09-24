<script setup>
import { ref } from 'vue'

const user = ref()
const pass = ref()
const emit = defineEmits(['onSubmit'])

function submitHandler(fields) {
  emit('onSubmit', fields)
  
}

const props = defineProps({
      loginError: Object,
})

</script>

<template>
  <div class="login-box">
    <form-kit
      type="form"
      submit-label="Ingresar"
      :actions="false"
      @submit="submitHandler"
    >
      <img
        class="login-img"
        src="../../img/new_logo.png"
        alt="logo"
      >
      <p class="login-box-title">
        Área Gestión de CCTE y Laboratorios
      </p>
      <form-kit
        v-model="user"
        outer-class="field-login"
        type="text"
        label="Usuario"
        name="user"
      />
      <form-kit
        v-model="pass"
        outer-class="field-login"
        type="password"
        label="Contraseña"
        name="pass"
      />
      <p
        v-if="loginError && loginError.response.data.message === 'Unauthorized'"
        class="login-error"
      >
        Usuario o contraseña incorrectos
      </p>
      <button
        class="login-button"
        type="submit"
      >
        Ingresar
      </button>
    </form-kit>
  </div>
</template>

<style scoped>

.login-box {
      display: flex;
      flex-direction: column;
      align-items: center;
      /* margin: auto; */
      margin: 10%;
      border: 1px solid #0B1742;
      padding: 0 60px 30px;
      border-radius: 10px;
      /* box-shadow: 5px 5px 5px 5px gray; */
      /* width: 400px; */
      column-gap: 20px;
      
}

.login-img {
      margin: 0 auto;
      height: 80px;
      width: 220px;
      margin: 15px auto;
      margin-bottom: 5px;
}
.field-login {
  /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
  flex: 0 0 50%;
  width: 300px;
  margin-bottom: 20px;
}
.login-button {
      background-color: #0B1742;
      margin-top: 10px;
      padding: 10px 18px;
      border-radius: 20px;
      font-weight: 800;
      cursor: pointer;
      border: 1px solid #0B1742;
      font-weight: 600;  
      color: white;  
      align-self: flex-end;
      width: 100%;
}
.login-button:hover {
      background-color: #005297;
      color: white;
}
.login-box-title {
      font-weight: 700;
      align-self: center;
      padding: 5px 10px 15px;
}
.login-error {
  color: red;
  /* font-weight: 500; */
}

</style>
