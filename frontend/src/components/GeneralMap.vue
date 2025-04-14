<template>
  <div class="global-map-container">
    <l-map 
    ref="map"
    :zoom="zoom"
    :useGlobalLeaflet="true" 
    :center="[position[0], position[1]]"
    :options="{ zoomControl: false }"
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
        :max-zoom="19"
      />
      <l-tile-layer
        layer-type="base"
        name="Satellite"
        url="https://mt1.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}"
        attribution="Map data ©2024 Google"
        :z-index="1"
      />
      <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        layer-type="base"
        name="OpenStreetMap"
        :max-zoom="19"
      />

      <l-marker-cluster-group>
        <l-marker 
          v-for="item in files"
          :key="item.id"
          :lat-lng="[ item.latitud , item.longitud ]"
        >
          <l-icon
            v-if="item.tipo"
            :icon-size="[35, 35]"
            :icon-url="pickIcon(item)"
            :icon-anchor="[12, 12]"
          />
          <l-icon
            v-else
            :icon-size="[40, 25]"
            :icon-url="pickIcon(item)"
            :icon-anchor="[12, 12]"
          />
          <l-popup
            :options="{}"
            class="popup-content"
          >
            <p class="popup-title">
              {{ item.expediente }}
            </p>
            <prop-value
              v-if="item.aeropuerto"
              class="prop"
              label="Aeropuerto"
              :value="item.aeropuerto"
            />
            <prop-value
              class="prop"
              label="Tipo de trámite"
              :value="item.tipo"
            />
            <prop-value
              v-if="item.localidad"
              class="prop"
              label="Localidad (Provincia)"
              :value="item.localidad + ' (' + item.provincia +')'"
            />
            <prop-value
              v-if="item.frecuencia"
              class="prop"
              label="Frecuencia"
              :value="item.frecuencia + ' ' + item.unidad"
            />
            <my-button
              class="primary view-button"
              label="Ver"
              @on-tap="() => viewItem(item.id)"
            />
          </l-popup>
        </l-marker>
      </l-marker-cluster-group>
    </l-map>
  </div>
</template>

<script setup>
import L from 'leaflet'
// globalThis.L = L
import { LMap, LTileLayer, LIcon, LPopup, LMarker, LControlLayers } from '@vue-leaflet/vue-leaflet'
import { LMarkerClusterGroup } from 'vue-leaflet-markercluster'
import 'leaflet/dist/leaflet.css'
import 'vue-leaflet-markercluster/dist/style.css'
import { useIconsMap } from "../composables/iconsmap"
import genericIcon from "../../img/map_icons/generic.png"
import { useTerritory } from "../composables/territory";
import MyButton from "./MyButton.vue";
import { useRouter } from 'vue-router'
import PropValue from "./PropValue.vue";
import Heading from '../components/Heading.vue';

const { getIconUrl } = useIconsMap()
const { getNameByCode } = useTerritory()
const router = useRouter()

const props = defineProps({
  position: {
    type: Array,
    default: () => [0, 0]
  },
  zoom: Number,
  files: Array,
})

function pickIcon(item) {
  let icon = ''
  if (item.tipo.trim() === 'Interferencias Celulares'){
    icon = getIconUrl(item.usuario)     
  } else{
      if(getIconUrl(item.tipo) != null || getIconUrl(item.tipo) != undefined){ 
        icon = getIconUrl(item.tipo)
      } else {
          // icon = genericIcon
          icon = getIconUrl('Otros')

      }
  }
  return icon
}

function viewItem(file_id) {  
  router.push(`/file/${file_id}`)
}

</script>

<style scoped>
.global-map-container {
  height: 700px;
  width: 100%;
  /* margin-top: 10px; */
  position: relative;
}

.menu-container {
  position: relative;
  z-index: 2000;
  margin-top: 15px;
}

.popup-title {
  font-weight: 700;
}

.prop {
  text-align: center;
}

.popup-content {
  font-size: 10px;
}
.view-button {
  margin-top: 5px;
  width: 100%;
}
</style>