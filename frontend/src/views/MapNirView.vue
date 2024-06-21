<script setup>
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import GNirmap from '../components/GlobalMapNir.vue'
import MyButton from '../components/MyButton.vue'


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
  <heading>Mapa de Mediciones de RNI</heading>
  <div class="buttons-container">
    <my-button
      class="primary right"
      label="Volver"
      @on-tap="goBack"
    />
  </div>
  <g-nirmap
    v-if="latitude"
    :zoom="zoom"
    :position="[ latitude.toString(), longitude.toString()]"
  />
</template>


<style scoped>
.buttons-container {
  display: flex;
  flex-direction: row;
  gap: 10px;
  justify-content: end;
  margin: 0 5px;
}
</style>