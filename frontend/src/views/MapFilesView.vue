<script setup>
import { onBeforeMount, ref, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import GeneralMap from '../components/GeneralMap.vue'
import MyButton from '../components/MyButton.vue'
import FormSearch from '../components/FormSearch.vue'
import { useApi } from '../composables/api'
import { useSearch } from '../composables/search'
import { useIconsMap } from "../composables/iconsmap"
import { useTerritory } from '../composables/territory';


const { getIconUrl } = useIconsMap()
const { getNameByCode } = useTerritory()


let latitude = ref()
let longitude = ref()
let zoom = ref()
let inputTextToSearch = ref('')
const router = useRouter()
const { list, loading, deleteFile } = useApi()
const { search } = useSearch()

const estado = ref('Pendiente')

const files = ref([])
const items = ref([])


onBeforeMount(async() => {
  navigator.geolocation.getCurrentPosition(
      position => {
        latitude.value = position.coords.latitude
        longitude.value = position.coords.longitude
        zoom.value = 10
        console.log("Coordenadas de mi ubicación: ", latitude.value, longitude.value)

      },
      error => {
         console.log(error.message);
         latitude.value = -40.4989
         longitude.value = -64.7597
         zoom.value = 4
      },
   )
   nextTick(() => {
    const checkDomReady = setInterval(async () => {
      try {
        let data
        if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
          data = await list(false, estado.value)
        } else {
            data = await list(true, estado.value)
        }  
        files.value.push(...data)
        files.value = files.value.map(item => {
          if (item.tipo !== 'Interferencias en Aeropuertos') {
            item.localidad = getNameByCode('city', item.localidad)
            item.provincia = getNameByCode('province', item.provincia)
          }
          return item
        }).filter(item => {
          return !(item.tipo === 'Medición de Radiaciones No Ionizantes (móviles)' || item.tipo === 'Descargo')
        })
        clearInterval(checkDomReady)
      } catch(error) {
          console.log(error.response)
          clearInterval(checkDomReady)  
        }
      }, 200)
    })
  })

function goBack() {  
  router.back()
}

async function searchFiles(textToSearch) {
  if(textToSearch != '') {
    files.value = search(files.value, textToSearch, ['area_asignada','tipo','usuario','fecha','expediente', 'area_actual','localidad','provincia','prioridad'])
    textToSearch = ''    
  } else {
    if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
      files.value = []
      const data = await list(false, estado.value)
      files.value.push(...data)
      files.value = files.value.map(item => {
        if (item.tipo !== 'Interferencias en Aeropuertos') {
          item.localidad = getNameByCode('city', item.localidad)
          item.provincia = getNameByCode('province', item.provincia)
        }
        return item
        }).filter(item => {
          return !(item.tipo === 'Medición de Radiaciones No Ionizantes (móviles)' || item.tipo === 'Descargo')
        })
    }
  }
  
}

</script>


<template>
  <div class="map-files">
    <!-- <heading class="map-heading">Mapa de Expedientes</heading> -->
    <!-- <div class="buttons-container">
      <my-button
        class="primary map-btn"
        label="Volver"
        @on-tap="goBack"
      />
    </div> -->
    <div class="view-map-container">
      <div class="form-search-container">
        <form-search
          class="search-input"
          :text-to-search="inputTextToSearch"
          placeholder="Buscar Expedientes"
          @on-submit="searchFiles"
        />
      </div>
      
      <general-map
        class="general-map"
        v-if="latitude"
        :zoom="zoom"
        :position="[ latitude.toString(), longitude.toString()]"
        :files="files"
      />
    </div>
    <div class="map-references">
      <h2 class="heading map-heading">Mapa de Expedientes</h2><br>
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


<style scoped>

.map-files {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 91px);
  width: 100%;
  position: relative;
}
.buttons-container {
  display: flex;
  flex-direction: row;
  gap: 10px;
  justify-content: right;
  margin: 0 5px;
  position: absolute;
  z-index: 2;
}
.view-map-container {
  height: 100%;
  position: relative;
}

.form-search-container {
  position: absolute;  
  /* background-color: white; */
  top: 25px;
  z-index: 2;
}

.general-map {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  z-index: 1;
}
.map-heading {
  font-size: 16px;
  /* position: absolute;
  z-index: 2; */
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