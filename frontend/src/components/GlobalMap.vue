<template>
  <div class="global-map-container">
    <div class="menu-container">
      <form-search 
        :text-to-search="textToSearch"
        placeholder="Buscar Estaciones"
        @on-submit="searchStations"
      />
    </div>
  
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
        v-for="item in items"
        :key="item.id"
        :lat-lng="[ item.latitud , item.longitud ]"
      >
        <l-icon
          :icon-size="[55, 35]"
          :icon-url="pickIcon(item)"
          :icon-anchor="[20, 35]"
        />
        <l-popup
          :options="{}"
          class="popup-content"
        >
          <p class="popup-title">
            Datos de la estación - id: {{ item.id }}
          </p>
          <prop-value
            class="prop"
            label="Identificación"
            :value="item.identificacion"
          />
          <prop-value
            v-if="item.frecuencia == null"
            class="prop"
            label="Frecuencia"
            value="---"
          />
          <prop-value
            v-else
            class="prop"
            label="Frecuencia"
            :value="item.frecuencia + ' ' + item.unidad"
          />
          <prop-value
            class="prop"
            label="Emplazamiento"
            :value="item.emplazamiento"
          />
          <prop-value
            class="prop"
            label="Localidad"
            :value="item.localidad"
          />
          <prop-value
            class="prop"
            label="Provincia"
            :value="item.provincia"
          /><br>
          <div class="popup-buttons">
            <my-button
              class="primary"
              label="Ver"
              @on-tap="() => viewItem(item.file_id, item.id)"
            />
          </div>
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script setup>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LIcon, LPopup } from "@vue-leaflet/vue-leaflet";
import { onBeforeMount, ref } from "vue";
import { useApi } from '../composables/api'
import { useTerritory } from "../composables/territory";
import MyButton from "./MyButton.vue";
import { useRouter } from 'vue-router'
import PropValue from "./PropValue.vue";
import FormSearch from "./FormSearch.vue";
import { useIconsMap } from "../composables/iconsmap"
import { useSearch } from "../composables/search"
import genericIcon from "../../img/map_icons/generic.png"


const { listStations } = useApi()
const { getNameByCode } = useTerritory()
const { getIconUrl } = useIconsMap()
const { search } = useSearch()
const router = useRouter()


const items = ref([])
const textToSearch = ref('')

onBeforeMount(async () => {

      const data = await listStations()      
      items.value.push(...data)      
      for (const item in items.value) {
        items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
        items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
      }
})

async function searchStations(textToSearch) {
    const data = await listStations(false)
    items.value = search(data, textToSearch, ['identificacion','servicio', 'frecuencia', 'domicilio', 'localidad', 'provincia', 'emplazamiento'])  
}

function viewItem(file_id, id) {  
  router.push(`/file/${file_id}/station/${id}`)
}

function pickIcon(station) {
  if( station.servicio != '---') {
    return getIconUrl(station.servicio)
  } else if ( station.servicio === '---' || station.servicio == null) {
    return genericIcon
  }
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
  height: 700px;
  width: 100%;
  margin-top: 10px;
  position: relative;
  background: linear-gradient(to right, rgba(202, 202, 202, 0), #cacaca, rgba(202, 202, 202, 0));
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