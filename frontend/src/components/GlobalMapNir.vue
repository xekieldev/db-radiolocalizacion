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
      <l-control-layers/>
      <l-tile-layer
        layer-type="base"
        name="GoogleMap"
        url="https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
        :subdomains="['mt0','mt1','mt2','mt3']"
        :max-zoom="20"
      />
      <l-tile-layer
        name="Satellite"
        layer-type="base"
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
      <l-marker
        v-for="item in items"
        :key="item.id"
        :lat-lng="[ item.coordinates.lat , item.coordinates.lon ]"
      >
        <l-icon
          :icon-size="[35, 35]"
          :icon-url="pickIcon()"
          :icon-anchor="[20, 35]"
        />
        <l-popup
          :options="{}"
          class="popup-content"
        >
          <p class="popup-title">
            Medición de RNI Móvil - id: {{ item.id }}
          </p>
          <prop-value
            class="prop"
            label="Localidad"
            :value="getNameByCode('city', item.localidad)"
          />
          <prop-value
            class="prop"
            label="Provincia"
            :value="getNameByCode('province', item.provincia)"
          />
          <prop-value
            class="prop"
            label="Cantidad de mediciones"
            :value="item.cantidad"
          />
          <prop-value
            class="prop"
            label="Valor Máximo [%]"
            :value="item.valor_maximo"
          />
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LIcon, LPopup, LControlLayers } from "@vue-leaflet/vue-leaflet";
import { onBeforeMount, ref } from "vue";
import { useApi } from '../composables/api'
import { useTerritory } from "../composables/territory";
import PropValue from "./PropValue.vue";
import { useIconsMap } from "../composables/iconsmap"



const { getAllNonIonizingRadiation } = useApi()
const { getNameByCode, getCoordinates } = useTerritory()
const { getIconUrl } = useIconsMap()


const items = ref([])

onBeforeMount(async () => {

      const data = await getAllNonIonizingRadiation()      
      items.value.push(...data)
      for (const item of items.value) {
        const coordinates = getCoordinates(item.localidad)
        item.coordinates = coordinates
      }     
})

function pickIcon() {
    return getIconUrl("NIR")
}

defineProps({
  
  position: {
    type: Array,
    default: () => [0, 0]
  },
  zoom: Number
  
})


</script>

<style scoped>

.global-map-container {
  height: 100%;
  width: 100%;
  /* margin-top: 10px; */
  position: relative;
  /* background: linear-gradient(to right, rgba(202, 202, 202, 0), #cacaca, rgba(202, 202, 202, 0)); */
}

.menu-container {
  position: absolute;
  z-index: 2000;
  margin-top: 15px;
}

.search-items {
  display: flex;
  justify-content: end; 
}

.field-search {
  display: flex;
  /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
  flex: 0 0 65%;
  margin: 0;
  background-color: white;
}

.search-btn {
  margin: 0 5px;
  background-color: white;
}

.popup-title {
  font-weight: 700;
}

.prop {
  text-align: center;
}

.popup-buttons {
  display: flex;
  justify-content: flex-end;
  margin-right: 10px;
}
.popup-content {
  font-size: 10px;
}
</style>