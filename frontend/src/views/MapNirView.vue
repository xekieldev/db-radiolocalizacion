<script setup>
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import GNirMap from '../components/GlobalMapNir.vue'
import MyButton from '../components/MyButton.vue'
import { useIconsMap } from "../composables/iconsmap"


const { getIconUrl } = useIconsMap()


let latitude = ref()
let longitude = ref()
let zoom = ref()
const router = useRouter()


onBeforeMount( () => {
  navigator.geolocation.getCurrentPosition(
      position => {
        latitude.value = position.coords.latitude
        longitude.value = position.coords.longitude
        zoom.value = 10
        console.log("Coordenadas de mi ubicación: ",latitude.value, longitude.value)
      },
      error => {
         console.log(error.message);
         latitude.value = -40.4989
         longitude.value = -64.7597
         zoom.value = 4
      },
   )
}) 
function goBack() {  
  router.back()

}
</script>


<template>
  <div class="nir-map-container">
    <g-nir-map
    v-if="latitude"
    :zoom="zoom"
    :position="[ latitude.toString(), longitude.toString()]"
  />
  <div class="map-references">
      <h2 class="heading">Mapa de RNI móviles</h2>
      <h3 class="heading">Referencias</h3>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Medición de Radiaciones No Ionizantes (móviles)')" alt="">
        Localidad medida
      </h4>
    </div>
  </div>
  
</template>


<style scoped>

.nir-map-container {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 91px);
  width: 100%;
  position: relative;
}
.map-references {
  /* display: flex;
  flex-direction: column; */
  position: absolute;
  bottom: 10px; /* Puedes ajustar la posición según prefieras */
  left: 10px;
  background-color: rgba(255, 255, 255, 0.6); /* Fondo semitransparente */
  padding: 10px;
  border-radius: 5px;
  z-index: 1000; 
  font-size: 12px;
}
.reference-icon {
  height: 23px;
  padding-right: 5px;
}
.reference-item {
  display: flex;
  align-items: center;
  padding-top: 3px;
  font-weight: 600;
}
.heading {
  font-weight: 500;
}
</style>