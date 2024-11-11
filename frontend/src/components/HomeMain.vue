<script setup>
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import { useRouter } from 'vue-router'
import FooterMain from '../components/FooterMain.vue'
import { ref } from 'vue';
import { perfil } from '../composables/loginstatus'

const router = useRouter()
const filesMenu = ref(false)
const mapsMenu = ref(false)
const stationsMenu = ref(false)

function closeDiv() {
  filesMenu.value = false
  stationsMenu.value = false
  mapsMenu.value = false
}

function list() {
  router.push({name: "list", query: { includeDeleted: 'false', fileStatus: 'Pendiente'}})
}

function newFile() { 
  router.push({name: "newFile"})
}

function listTechnicians() {
  router.push({name: "listTechnicians"})
}

function fileOptions() {
  filesMenu.value = !filesMenu.value
  stationsMenu.value = false
  mapsMenu.value = false
}

function stationsOptions() {
  stationsMenu.value = !stationsMenu.value
  filesMenu.value = false
  mapsMenu.value = false
}

function mapOptions() {
  mapsMenu.value = !mapsMenu.value
  filesMenu.value = false
  stationsMenu.value = false
}

function stationList() {
  router.push({ name: "stations", query: { includeDeleted: 'false'}})
}

function nirMeasurements() {
  router.push({ name:"listNIR"})
}

function statistics() {
  router.push({ name:"statistics", query: { type: 'pending'}})
}

function filesMap() {
  router.push({ name:"filesMap"})
}

function stationsMap() {
  router.push({ name:"map"})
}

function nirMap() {
  router.push({ name:"nirMap"})
}

</script>

<template>
  <div class="home-container">
    <heading class="home-title">
      Sistema de Gestión de Expedientes<br/>Sistema Nacional de Comprobación Técnica de Emisiones (SNCTE)
    </heading>
    <div class="home-buttons">
      <div class="first-row">
        <my-button
          tabindex="0"
          class="septenary button file-manage"
          label="Gestión de Expedientes"
          @on-tap="fileOptions"
        />
        <div
          v-if="filesMenu == true"
          class="file-options"
        >
          <button
            class="close-button"
            @click="closeDiv"
          >
            x
          </button>
          <my-button
            tabindex="0"
            class="quaternary sub-menu-button stations-list"
            label="Listado de Expedientes"
            @on-tap="list"
          />
          <my-button
            v-if="perfil == 'coordinator'"
            tabindex="0"
            class="quaternary sub-menu-button new-file"
            label="Alta Expediente"
            @on-tap="newFile"
          />
        </div>
        <my-button
          tabindex="0"
          class="septenary button statistics"
          label="Estadísticas"
          @on-tap="statistics"
        />
        <my-button
          tabindex="0"
          class="septenary button station-manage"
          label="Gestión de Estaciones"
          @on-tap="stationsOptions"
        />
        <div
          v-if="stationsMenu == true"
          class="stations-options"
        >
          <button
            class="close-button"
            @click="closeDiv"
          >
            x
          </button>
          <my-button
            tabindex="0"
            class="quaternary sub-menu-button stations-list"
            label="Listado de Estaciones"
            @on-tap="stationList"
          />
        </div>
      </div>
      <div class="second-row">
        <my-button
          tabindex="0"
          class="septenary button nir-measurements"
          label="Mediciones de RNI móvil"
          @on-tap="nirMeasurements"
        />
        <my-button
          tabindex="0"
          class="septenary button maps"
          label="Mapas"
          @on-tap="mapOptions"
        />
        <div
          v-if="mapsMenu == true"
          class="file-options"
        >
          <button
            class="close-button"
            @click="closeDiv"
          >
            x
          </button>
          <my-button
            tabindex="0"
            class="quaternary sub-menu-button files-map"
            label="Expedientes"
            @on-tap="filesMap"
          />
          <my-button
            tabindex="0"
            class="quaternary sub-menu-button stations-map"
            label="Estaciones"
            @on-tap="stationsMap"
          />
          <my-button
            tabindex="0"
            class="quaternary sub-menu-button nir-map"
            label="RNI móvil"
            @on-tap="nirMap"
          />
        </div>
        <my-button
          v-if="perfil == 'coordinator'"
          tabindex="0"
          class="septenary button technician-manage"
          label="Agregar/Eliminar Técnicos"
          @on-tap="listTechnicians"
        /> 
      </div>
    </div>
    <footer-main class="footer-main" />
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-content: space-between;  
}
.home-buttons {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  margin-top: 60px;
  gap: 10px;
  align-items: center;
}
.first-row {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
.second-row {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
.sub-menu-button {
  margin: 5px 20px 5px 5px;
}
.button {
  margin: 5px;
}
.stations-list {
  background-image: url(../../img/listado.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 25px;
}
.new-file {
  background-image: url(../../img/new-file.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 25px;
}
.new-rloc {
  background-image: url(../../img/antena-parabolica.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 25px;
}
.new-loc {
  background-image: url(../../img/mapa.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 25px;
}
.file-manage {
  background-image: url(../../img/expediente.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 25px;
}
.station-manage {
  background-image: url(../../img/estacion-de-radio.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 25px;
}
.technician-manage {
  background-image: url(../../img/conexion-inalambrica.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 25px;
}
.nir-measurements {
  background-image: url(../../img/camioneta-rni.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 25px;
}
.statistics {
  background-image: url(../../img/estadisticas.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 25px;
}
.maps {
  background-image: url(../../img/mapa-arg.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 25px;
}
.files-map {
  background-image: url(../../img/files-map.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 25px;
}
.stations-map {
  background-image: url(../../img/station-map.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 25px;
}
.nir-map {
  background-image: url(../../img/nir-map.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 25px;
}
.home-title {
  text-align: center;
}
.stations-options {
  display: flex;
  flex-direction: column;
  padding: 1px;
  align-content: space-between;
}
.close-button {
  position: absolute;
  top: 5px;
  right: 0px;
  background: none;
  border: none;
  font-size: 15px;
  font-weight: 300;
  cursor: pointer;
}
.footer-main {
  position: fixed;
  align-self: flex-end;
  bottom: 0;
}

</style>
