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
              :value="getNameByCode('city', item.localidad) + ' (' + getNameByCode('province', item.provincia)+')'"
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
    <div class="map-references">
      <h2 class="heading">Mapa de Expedientes</h2>
      <h3 class="heading">Referencias</h3>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Interferencias en Aeropuertos')" alt="">
        Interferencias en Aeropuertos
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Interferencias en Estaciones Radioeléctricas')" alt="">
        Interferencias en Estaciones Radioeléctricas
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Interferencias en Estaciones de Radiodifusión')" alt="">
        Interferencias en Estaciones de Radiodifusión
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Personal')" alt="">
        <img class="reference-icon" :src="getIconUrl('Claro')" alt="">
        <img class="reference-icon" :src="getIconUrl('Movistar')">
        Interferencias Celulares
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Inspección de Estaciones Radioeléctricas')" alt="">
        Inspección de Estaciones Radioeléctricas
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Inspección de Estaciones de Radiodifusión')" alt="">
        Inspección de Estaciones de Radiodifusión
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Radiolocalización de Estaciones Radioeléctricas')" alt="">
        Radiolocalización de Estaciones Radioeléctricas
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Radiolocalización de Estaciones de Radiodifusión')" alt="">
        Radiolocalización de Estaciones de Radiodifusión
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Detectar actividad')" alt="">
        Detectar actividad
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Denuncias del Público en General')" alt="">
        Denuncias del Público en General
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Medición de Radiaciones No Ionizantes')" alt="">
        Medición de Radiaciones No Ionizantes
      </h4>
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Otros')" alt="">
        Otros
      </h4>
      <!-- <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Inspección de Estaciones Radioeléctricas')" alt="">
        Medición de Radiaciones No Ionizantes (móviles)
      </h4 >
      <h4 class="reference-item">
        <img class="reference-icon" :src="getIconUrl('Descargo')" alt="">
        Descargo
      </h4> -->
    </div>
  </div>
</template>

<script setup>
import L from 'leaflet'
// globalThis.L = L
import { LMap, LTileLayer, LIcon, LPopup, LMarker } from '@vue-leaflet/vue-leaflet'
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
      console.log('item tipo', item.tipo, getIconUrl(item.tipo))
      icon = getIconUrl(item.tipo)
    } else {
       icon = genericIcon
    }
   
  } 
     
  console.log('icon', icon)
   
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