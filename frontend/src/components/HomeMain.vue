<script setup>
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
  router.push({ name: "station", query: { includeDeleted: 'false'}})
}

</script>

<template>

<heading>Base de datos de Radiolocalizaciones y Localizaciones</heading>
  <div class="home-buttons">
    <my-button tabindex="0" @on-tap="createFile" class="quaternary button new-rloc" label="Nueva Radiolocalización"></my-button>
    <my-button tabindex="0" @on-tap="createLocFile" class="quaternary button new-loc" label="Nueva Localización"></my-button>
    <my-button tabindex="0" @on-tap="list" class="quaternary button file-manage" label="Gestión de Expedientes"></my-button>
    <my-button tabindex="0" @on-tap="stationList" class="quaternary button station-manage" label="Gestión de Estaciones"></my-button>
    <my-button tabindex="0" @on-tap="listTechnicians" class="quaternary button technician-manage" label="Gestión de Técnicos"></my-button>

  </div>

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
