<script setup>

</script>

<template>
  <!-- <div> -->
    <footer class="footer-container">
      <img
        src="../../img/Logo.png"
        alt="logo-enacom"
        class="logo-enacom"
      >
    </footer>
  <!-- </div> -->
</template>

<style scoped>
.footer-container {
  /* position: fixed; */
  bottom: 0;
  left: 0; /* Extiende el footer a lo largo de toda la anchura */
  right: 0;
  width: 100%; /* Ancho completo */
  background-color: transparent; /* Hace que el fondo del footer sea transparente */
  text-align: center; /* Centra el texto del footer horizontalmente */
  padding: 10px; /* Agrega un poco de espacio alrededor del contenido del footer */
  box-sizing: border-box; /* Asegura que el padding se incluya en el ancho total del footer */
}
.logo-enacom {
  height: 50px;
}
</style>
