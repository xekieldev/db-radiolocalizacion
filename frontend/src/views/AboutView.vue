<script setup>
import Heading from '../components/Heading.vue';
</script>

<template>
  <div class="about">
    <heading>Base de Datos de Radiolocalizaciones y Mediciones Técnicas Externas</heading>
    <div class="about-text">
      <h3 class="version-titles">
        Versión: 2.0
      </h3><br>
      <h4 class="version-titles">
        En esta versión:
      </h4>
      <ul class="items-version">
        <li>Visualización de las estaciones en un mapa con buscador</li>
        <li>Busqueda por expedientes</li>
        <li>Preview para imprimir</li>
        <li>Nuevas validaciones en los formularios</li>
        <li>Mejora de la Planilla de Mediciones Técnicas</li>
        <li>Agregado de mensaje de login failed</li>
        <li>Agregado de Antenas, Servicios, etc. en las listas desplegables</li>
        <li>Reparación de bugs</li>
      </ul><br>
      <h3 class="version-titles">
        Versión: 1.0
      </h3><br>
      <h4 class="version-titles">
        En esta versión:
      </h4>
      <ul class="items-version">
        <li>Acceso seguro con usuario y contraseña</li>
        <li>Base de datos de Radiolocalizaciones, Localizaciones y Mediciones Técnicas Externas</li>
        <li>Escalabilidad</li>
        <li>Interfaz moderna</li>
        <li>Ubicación automática en el mapa</li>
        <li>Validación de campos</li>
        <li>Estudio y Planta Transmisora relacionadas</li>
        <li>Mediciones técnicas relacionadas a la estación</li>
        <li>Gestión de Técnicos, ingresar nuevo técnico y eliminarlos (sólo en caso que no se hayan utilizado)</li>
        <li>Protección de los datos de las estaciones almacenadas en la base de datos</li>
        <li>Impresión directa desde el navegador</li>
        <li>Búsqueda por estaciones</li>
        <li>Y mucho más!</li>
      </ul>
    </div>
    <footer class="about-footer">
      <a href="https://github.com/xekieldev/db-radiolocalizacion.git"><img
        class="logo-github"
        src="../../img/github-logo.png"
        alt="xekieldev"
      ></a>
      <h5>Diseñado y desarrollado por Exequiel Sartor</h5>
    </footer>
  </div>
</template>

<style scoped>
.about {
  text-align: center;
  width: 900px;
}

.version-titles {
  text-align: left;
}
.items-version {
  text-align: left;
  align-items: center;
}

.logo-github {
  height: 50px;

}

.about-footer {
  position: fixed;
  bottom: 0;
  left: 0; /* Extiende el footer a lo largo de toda la anchura */
  right: 0;
  width: 100%; /* Ancho completo */
  background-color: transparent; /* Hace que el fondo del footer sea transparente */
  text-align: center; /* Centra el texto del footer horizontalmente */
  padding: 20px; /* Agrega un poco de espacio alrededor del contenido del footer */
  box-sizing: border-box; /* Asegura que el padding se incluya en el ancho total del footer */
}

.about-text {
  margin-bottom: 100px;
}
</style>
