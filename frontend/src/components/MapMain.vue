<template>
  <div class="map-container">
    <l-map
      ref="map"
      v-model:zoom="store.zoom"
      :center="[store.lat, store.lng]"
      :use-global-leaflet="false"
      :options="{ zoomControl: false }"
      :min-zoom="14"
      :max-zoom="18"
    >
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="base"
        name="OpenStreetMap"
      />
      <l-marker :lat-lng="[store.lat, store.lng]">
        <l-icon
          :icon-size="[60, 60]"
          icon-url="../img/antena.png"
        />
        <l-popup>Coordenadas: {{ store.lat }}, {{ store.lng }} <br> Nivel de Zoom: {{ store.zoom }}</l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LIcon, LPopup } from "@vue-leaflet/vue-leaflet";
import { useRlocFormData } from '../composables/rloc-form-data'

const store = useRlocFormData()

</script>

<style scoped>
.map-container {
  height: 600px;
  width: 800px;
}
</style>