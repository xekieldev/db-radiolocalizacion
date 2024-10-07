<script setup>
import { ref } from 'vue'


const new_pass = ref()
const new_pass_confirm = ref()
const emits = defineEmits(['onSubmit'])


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
      <p class="login-box-title">
        Cambiar contraseña   
      </p>
      <form-kit
        v-model="new_pass"
        outer-class="field-login"
        type="password"
        label="Nueva Contraseña"
        name="new_pass"
        validation="required"
        :validation-messages="{
          required: 'Debe ingresar una contraseña',
        }"
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
          required: 'Debe ingresar una contraseña'
        }"
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
  align-items: center;
  margin: 5% 15%;
  border: 1px solid #0B1742;
  padding: 0 60px 30px;
  border-radius: 10px;
  column-gap: 20px;
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
  margin-bottom: 20px;
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
      width: 100%;
}
.login-button:hover {
      background-color: #007BFF;
      color: white;
}
.login-box-title {
  font-size: 20px;;
  font-weight: 700;
  align-self: center;
  padding: 20px 10px 15px;
}
.login-error {
  color: red;
  /* font-weight: 500; */
}
</style>
