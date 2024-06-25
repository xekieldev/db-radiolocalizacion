<script setup>
import Heading from '../components/Heading.vue';
import FooterMain from '../components/FooterMain.vue';
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
        <li>Visualización de estaciones en un mapa con buscador</li>
        <li>Búsqueda por expedientes</li>
        <li>Función para imprimir</li>
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
    <footer-main />
    <h5 class="developer-name">
      Developed by Exequiel Sartor
    </h5>
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

.logo-enacom {
  height: 50px;
}

.about-text {
  margin-bottom: 100px;
}
.developer-name {
  /* position: sticky; */
  color: #2C3E50;
  bottom: 5px;
  left: 0; 
  right: 0;
  width: 100%; 
}
</style>
