<script setup>
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import { useRouter } from 'vue-router'
import FooterMain from '../components/FooterMain.vue'
import { ref } from 'vue';

const router = useRouter()
const stationsMenu = ref(false)

const emits = defineEmits(['update: stationsMenu']);

function closeDiv() {
  stationsMenu.value = false
}


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

function stationsOptions() {
  stationsMenu.value = !stationsMenu.value

}

function stationList() {
  router.push({ name: "station", query: { includeDeleted: 'false'}})
}

function nirMeasurements() {
  router.push({ name:"listNIR"})
}

</script>

<template>
  <div class="home-container">
  <heading class="home-title">
    Base de Datos del Sistema Nacional de Comprobación Técnica de Emisiones
  </heading>
  <div class="home-buttons">
    <div class="first-row">
      <my-button
        tabindex="0"
        class="septenary button file-manage"
        label="Gestión de Expedientes"
        @on-tap="list"
      />
      <my-button
        tabindex="0"
        class="septenary button station-manage"
        label="Gestión de Estaciones"
        @on-tap="stationsOptions"
      />
      <div class="stations-options" v-if="stationsMenu == true">
        <button class="close-button" @click="closeDiv">x</button>
        <my-button
          tabindex="0"
          class="quaternary sub-menu-button stations-list"
          label="Listado de Estaciones"
          @on-tap="stationList"
        />
        <my-button
          tabindex="0"
          class="quaternary sub-menu-button new-rloc"
          label="Nueva Radiolocalización"
          @on-tap="createFile"
        />
        <my-button
          tabindex="0"
          class="quaternary sub-menu-button new-loc"
          label="Nueva Localización"
          @on-tap="createLocFile"
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
        class="septenary button technician-manage"
        label="Agregar/Eliminar Técnicos"
        @on-tap="listTechnicians"
      /> 
    </div>
  </div>
  <footer-main class="footer-main"/>
</div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-content: space-between;
  /* column-gap: 30px; */
  
}
.home-buttons {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  margin-top: 50px;
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
  background-position: center left 15px;
}
.new-rloc {
  background-image: url(../../img/antena-parabolica.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 15px;
}
.new-loc {
  background-image: url(../../img/mapa.png);
  background-repeat: no-repeat;
  background-size: 30px;
  background-position: center left 15px;
}
.file-manage {
  background-image: url(../../img/expediente.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 15px;
}
.station-manage {
  background-image: url(../../img/estacion-de-radio.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 15px;
}
.technician-manage {
  background-image: url(../../img/conexion-inalambrica.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 15px;
}
.nir-measurements {
  background-image: url(../../img/camioneta-rni.png);
  background-repeat: no-repeat;
  background-size: 50px;
  background-position: center top 15px;
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
