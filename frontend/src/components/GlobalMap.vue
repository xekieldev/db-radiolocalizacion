<template>
  <div class="map-container">
    <div class="menu-container">
      <form-row class="search-items">
          <form-kit
            outer-class="field-search"
            type="text"
            name="searchInput"
            placeholder="Buscar estaciones"
            v-model="searchText"
          />
          <my-button @on-tap="() => searchStations()" class="secondary search-btn" label="Buscar"/>
      </form-row>
    </div>
  
    <l-map
      ref="map"
      :zoom= zoom
      :center= "[position[0] , position[1]]"
      :use-global-leaflet="false"
      :options="{ zoomControl: false }"
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
      <l-marker :lat-lng="[ item.latitud , item.longitud ]" v-for="item in items">
        <l-icon
          :icon-size="[50, 30]"
          :icon-url= pickIcon(item)
        />
        <l-popup :options="{}"> <p class="popup-title">Datos de la estación - id: {{ item.id}}</p>
                  <prop-value class="prop" label="Identificación" :value="item.identificacion"/>
                  <prop-value class="prop" label="Frecuencia" value="---" v-if="item.frecuencia == null"/>
                  <prop-value class="prop" label="Frecuencia" :value="item.frecuencia + ' ' + item.unidad" v-else/>
                  <prop-value class="prop" label="Emplazamiento" :value="item.emplazamiento"/>
                  <prop-value class="prop" label="Localidad" :value="item.localidad"/>
                  <prop-value class="prop" label="Provincia" :value="item.provincia"/><br>
                  <div class="popup-buttons">
                    <my-button @on-tap="() => viewItem(item.id)" class="primary" label="Ver"/>
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
import FormRow from "./FormRow.vue";


const { listStations } = useApi()
const { getNameByCode } = useTerritory()
const router = useRouter()


const items = ref([])
const searchText = ref()

onBeforeMount(async () => {

      const data = await listStations()
      items.value.push(...data)
      for (const item in items.value) {
        items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
        items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
      }
})

async function searchStations() {
  const searchStringTemp = searchText.value ? searchText.value.toLowerCase() : ''
  const searchString = searchStringTemp.split('+')
  const data = await listStations(false)
  const searchResult = data.filter((item) => {

    const id = item.id
    const identificacion = item.identificacion ? item.identificacion.toLowerCase() : ''
    const servicio = item.servicio ? item.servicio.toLowerCase() : ''
    const frecuencia = item.frecuencia !== null && item.frecuencia !== undefined ? item.frecuencia.toString() : ''
    const domicilio = item.domicilio ? item.domicilio.toString().toLowerCase() : ''
    const localidad = getNameByCode("city", item.localidad) ? getNameByCode("city", item.localidad).toLowerCase() : '' 
    const provincia = getNameByCode("province", item.provincia) ? getNameByCode("province", item.provincia).toLowerCase() : '' 
    const emplazamiento = item.emplazamiento ? item.emplazamiento.toLowerCase() : ''
    
    return id == searchString || identificacion.includes(searchString) || servicio.includes(searchString) || frecuencia.includes(searchString) || domicilio.includes(searchString) || localidad.includes(searchString) || provincia.includes(searchString) || emplazamiento.includes(searchString)
    
  })
  items.value = searchResult
  for (const item in items.value) {
    items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
    items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
  }
}

function viewItem(item) {  
  router.push(`/file/${item}`)
}

function pickIcon(station) {
  if( station.servicio != '---') {
    return `../../img/${station.servicio}_new.png`
  } else if ( station.servicio === '---' || station.servicio == null) {
    return "../../img/generic_new.png"
  }
}

const props = defineProps({
  
  position: {
    type: Array,
    default: () => [0, 0]
  },
  zoom: Number
  
})


</script>

<style scoped>

.map-container {
  height: 510px;
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

</style>