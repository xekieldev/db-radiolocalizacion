<script setup>
import FormRow from './FormRow.vue'
import { useArea } from '../composables/area'
import { ref } from 'vue'



const user = ref()
const pass = ref()
const new_pass = ref()
const new_pass_confirm = ref()
const emits = defineEmits(['onSubmit'])
const { area } = useArea()


function submitHandler(fields) {
  emits('onSubmit', fields)
}

defineProps({
      loginError: Object,
})

</script>

<template>

  <div class="change-pass-container">
    <form-kit
      type="form"
      submit-label="Cambiar"
      :actions="false"
      @submit="submitHandler"
    >
      <img
        class="login-img"
        src="../../img/Logo.png"
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
      <form-kit
        v-model="new_pass"
        outer-class="field-login"
        type="password"
        label="Nueva Contraseña"
        name="new_pass"
        validation="required"
      />
      <form-kit
        v-model="new_pass_confirm"
        outer-class="field-login"
        type="password"
        label="Confirmar Nueva Contraseña"
        name="new_pass_confirm"
        validation="required|confirm"
        :validation-messages="{
          confirm: 'Error. Las contraseñas no coinciden',
        }"
        validation-label="Password confirmation no coincide"
      />
      <p
        v-if="loginError && loginError.response.data === 'Error de login'"
        class="login-error"
      >
        Usuario o contraseña incorrectos
      </p>
      <button
        class="login-button"
        type="submit"
      >
        Cambiar
      </button>

    </form-kit>
  </div>
  
</template>

<style scoped>


.change-pass-container {
      display: flex;
      flex-direction: column;
      margin: auto;
      margin-top: 5%;
      border: 1px solid gray;
      padding: 0 60px 30px;
      border-radius: 10px;
      box-shadow: 5px 5px 5px 5px gray;
      /* width: 400px; */
}

.login-img {
      margin: 0 auto;
      height: 70px;
      width: 70px;
      margin: 15px auto;
      margin-bottom: 5px;
}
.field-login {
  /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
  flex: 0 0 50%;
  width: 300px;
}
.login-button {
      background-color: white;
      margin-top: 10px;
      padding: 10px 18px;
      border-radius: 20px;
      font-weight: 800;
      cursor: pointer;
      border: 1px solid #007BFF;
      font-weight: 500;  
      color: #007BFF;  
      align-self: flex-end;
}
.login-button:hover {
      background-color: #007BFF;
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
