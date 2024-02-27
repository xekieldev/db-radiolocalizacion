<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
import { RouterLink } from 'vue-router';
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import router from '../router';



function createFile() { 
  router.push({name: "createFile", query: { rloc: 'true' }})
}

function createLocFile() { 
  router.push({name: "createFile", query: { rloc: 'false' }})
}

function list() {
  router.push({name: "list", query: { includeDeleted: 'false'}})
}

function listTechnicians() {
  router.push({name: "listTechnicians"})
}

function stationList() {
  router.push({ name: "station"})
}

</script>

<template>
  <heading>Base de datos de Radiolocalizaciones y Localizaciones</heading>
  <div class="home-buttons">
    <my-button @on-tap="createFile" class="quaternary button new-rloc" label="Nueva Radiolocalización"></my-button>
    <!-- <img src="../../img/antena-parabolica.png" alt=""> -->
    <my-button @on-tap="createLocFile" class="quaternary button new-loc" label="Nueva Localización"></my-button>
    <my-button @on-tap="list" class="quaternary button file-manage" label="Gestión de Expedientes"></my-button>
    <my-button @on-tap="stationList" class="quaternary button station-manage" label="Gestión de Estaciones"></my-button>
    <my-button @on-tap="listTechnicians" class="quaternary button technician-manage" label="Gestión de Técnicos"></my-button>
    <!-- <my-button @on-tap="createLocFile" class="quaternary button" label="Gestión de Técnicos" src="../../img/antena-parabolica.png"></my-button> -->
    <!-- <my-button @on-tap="createFile" class="quaternary button" label="About"></my-button>
    <my-button @on-tap="createFile" class="quaternary button" label="Help"></my-button>
    <my-button @on-tap="createFile" class="quaternary button" label="Help"></my-button>
    <my-button @on-tap="createFile" class="quaternary button" label="Help"></my-button> -->
  </div>

  <!-- <main>
    <TheWelcome />
  </main> -->
</template>

<style scoped>
.home-buttons {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  margin-top: 10px;
  width: 600px;
  align-items: center;
  align-self: center;
  flex-wrap: wrap;
  border: 1px solid lightgray;
  border-radius: 30px;
  padding: 30px
}

.button {
  margin: 10px;
}
.new-rloc {
  margin: 10px;
  background-image: url(../../img/antena-parabolica.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: 25px 15px;
}
.new-loc {
  margin: 10px;
  background-image: url(../../img/mapa.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: 25px 15px;
}
.file-manage {
  margin: 10px;
  background-image: url(../../img/expediente.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: 25px 15px;
}
.station-manage {
  margin: 10px;
  background-image: url(../../img/estacion-de-radio.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: 25px 15px;
}
.technician-manage {
  margin: 10px;
  background-image: url(../../img/conexion-inalambrica.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: 25px 15px;
}
</style>
