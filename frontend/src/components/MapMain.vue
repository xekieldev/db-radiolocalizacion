<template>
  <div class="map-container">
    <l-map
      ref="map"
      :zoom="18"
      :center="[position[0] || 0 , position[1] || 0]"
      :use-global-leaflet="false"
      :options="{ zoomControl: true }"
      :min-zoom="1"
      draggable="false"
      dragging="false"
    >
      <l-control-layers/>
      <l-tile-layer
        layer-type="base"
        name="GoogleMap"
        url="https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
        :subdomains="['mt0','mt1','mt2','mt3']"
        :max-zoom="20"
      />
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="base"
        name="OpenStreetMap"
        :max-zoom="19"
      />
      <l-marker :lat-lng="[position[0] || 0 , position[1] || 0]">
        <l-icon
          :icon-size="[50, 50]"
          :icon-url="antenaImage"
          :icon-anchor="[25, 40]"
        />
        <l-popup>Coordenadas: {{ position[0] || 0 }}, {{ position[1] ||0 }}</l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LIcon, LPopup, LControlLayers } from "@vue-leaflet/vue-leaflet";
import antenaImage from "../../img/antena.png";

const props = defineProps({
  
  position: {
    type: Array,
    default: () => [0, 0]
  }
  
})

</script>

<style scoped>
.map-container {
  height: 600px;
  width: 100%;
}

</style>