<script setup>
import Heading from '../components/Heading.vue';
import FooterMain from '../components/FooterMain.vue';
</script>

<template>
  
  <div class="about">
    <heading class="about-title">
      Sistema de Gestión de Expedientes<br/>Sistema Nacional de Comprobación Técnica de Emisiones (SNCTE)
    </heading>
      <h3 class="version-titles">
        Versión: 5.0
      </h3>
      <h4 class="version-titles">
        En esta versión:
      </h4>
      <ul class="items-version">
        <li>Se agregaron tablas que permiten ordenar los datos</li>
        <li>Se agregó función para exportar a .csv</li>
        <li>Se mejoró la búsqueda</li>
        <li>Mejoras visuales en diferentes componentes</li>
        <li>Corrección de errores</li>
      </ul><br>
    <div class="about-text">
      <h3 class="version-titles">
        Versión: 4.1
      </h3><br>
      <h4 class="version-titles">
        En esta versión:
      </h4>
      <ul class="items-version">
        <li>Agregado de campos a la lista de Expedientes</li>
        <li>Ampliación de campos de búsqueda en lista y mapa de expedientes</li>
        <li>Mejoras visuales en diferentes componentes</li>
        <li>Agregado de campos en estadísticas</li>
        <li>Corrección de errores</li>
      </ul><br>
      <h3 class="version-titles">
        Versión: 4.0
      </h3><br>
      <h4 class="version-titles">
        En esta versión:
      </h4>
      <ul class="items-version">
        <li>Visualización de estadísticas automáticas por fechas y áreas</li>
        <li>Visualización de expedientes en el mapa con agrupación por zonas</li>
        <li>Y más!</li>
      </ul><br>
      <h3 class="version-titles">
        Versión: 3.0
      </h3><br>
      <h4 class="version-titles">
        En esta versión:
      </h4>
      <ul class="items-version">
        <li>Gestión de expedientes, alta, pase entre Áreas y borrado</li>
        <li>Campos selectivos para alta de expedientes</li>
        <li>Seguimiento de expedientes en los CCTE</li>
        <li>Visualización de lugares de medición Radiaciones No Ionizantes móviles</li>
        <li>Autenticación con roles para cada CCTE (Coordinador y Técnico)</li>
        <li>Carga de actividades para cada expedientes</li>
        <li>Fácil identificación de expedientes prioritarios</li>
        <li>Y más!</li>
      </ul><br>
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
  display: flex;
  flex-direction: column;
  /* text-align: center; */
  width: 100%;
  padding: 0 30px;
}

.about-title {
  text-align: center;
}


.version-titles {
  align-items: left;
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
  text-align: center;
  font-size: 12px;
  color: #2C3E50;
  bottom: 5px;
  left: 0; 
  right: 0;
  width: 100%; 
}
</style>
