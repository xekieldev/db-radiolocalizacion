<template>
  <div style="height:600px; width:800px">
    <l-map ref="map" v-model:zoom="zoom" :center="[store.lat, store.lng]" :use-global-leaflet="false">
      <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" layer-type="base"
        name="OpenStreetMap"></l-tile-layer>
      <l-marker :lat-lng="[store.lat, store.lng]"></l-marker>
      
    </l-map>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker } from "@vue-leaflet/vue-leaflet";
import { useRlocFormData } from '../composables/rloc-form-data'

const store = useRlocFormData()

const props = defineProps({
  position: Array
})

const zoom = 18

</script>

<style></style>