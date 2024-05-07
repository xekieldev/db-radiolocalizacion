<template>
  <div class="map-container">
    <l-map
      ref="map"
      :zoom=19
      :center="[position[0] , position[1]]"
      :use-global-leaflet="false"
      :options="{ zoomControl: true }"
      :min-zoom=1
      draggable="false"
      dragging="false"
      
    >
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="base"
        name="OpenStreetMap"
        :max-zoom= 19
      />
      <l-marker :lat-lng="[position[0] , position[1] ]">
        <l-icon
          :icon-size="[50, 50]"
          icon-url="../../img/antena.png"
        />
        <l-popup>Coordenadas: {{ position[0] }}, {{ position[1] }}</l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LIcon, LPopup } from "@vue-leaflet/vue-leaflet";

const props = defineProps({
  
  position: {
    type: Array,
    default: () => [0, 0]
  }
  
})

</script>

<style scoped>
.map-container {
  height: 500px;
  width: 100%;
}

</style>