<template>
  <div class="global-map-container">
    <l-map
      ref="map"
      :zoom="zoom"
      :center="[position[0] , position[1]]"
      :use-global-leaflet="false"
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
      <l-marker 
        v-for="item in files"
        :key="item.id"
        :lat-lng="[ item.latitud , item.longitud ]"
      >
        <l-icon
          v-if="item.tipo"
          :icon-size="[25, 25]"
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
    </l-map>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LIcon, LPopup } from "@vue-leaflet/vue-leaflet";
import { useTerritory } from "../composables/territory";
import MyButton from "./MyButton.vue";
import { useRouter } from 'vue-router'
import PropValue from "./PropValue.vue";
import { useIconsMap } from "../composables/iconsmap"
import genericIcon from "../../img/map_icons/generic.png"


const { getNameByCode } = useTerritory()
const { getIconUrl } = useIconsMap()
const router = useRouter()


function pickIcon(item) {
  let icon = ''
  if (item.tipo.trim() === 'Interferencias en Estaciones Radioeléctricas'){
    if(item.usuario.trim() === 'Personal') icon = getIconUrl('Personal')     
    else if(item.usuario.trim() === 'Movistar') icon = getIconUrl('Movistar')
    else if(item.usuario.trim() === 'Claro') icon = getIconUrl('Claro')
  } else if(getIconUrl(item.tipo) === null){    
    icon = genericIcon
  } else icon = getIconUrl(item.tipo)  
  return icon
}

const props = defineProps({
  position: {
    type: Array,
    default: () => [0, 0]
  },
  zoom: Number,
  files: Array,
})

function viewItem(file_id) {  
  router.push(`/file/${file_id}`)
}

</script>

<style scoped>

.global-map-container {
  height: 700px;
  width: 100%;
  margin-top: 10px;
  position: relative;
}

.menu-container {
  position: absolute;
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