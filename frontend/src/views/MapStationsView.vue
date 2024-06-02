<script setup>
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import Gmap from '../components/GlobalMap.vue'
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
        zoom = 10
        console.log("Coordenadas de mi ubicación: ",latitude.value, longitude.value)

      },
      error => {
         console.log(error.message);
         latitude.value = -39.6989
         longitude.value = -64.7597
         zoom = 4
      },
   )
}) 
function goBack() {  
  router.back()

}
</script>


<template>

  <heading>Mapa de Estaciones</heading>
  <div class="buttons-container">
    <my-button
      class="primary right"
      label="Volver"
      @on-tap="goBack"
    />
  </div>
  <gmap :zoom="zoom" :position="[ latitude.toString(), longitude.toString()]" v-if="latitude"/>

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