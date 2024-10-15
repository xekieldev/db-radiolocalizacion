<script setup>
import { onBeforeMount, ref, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import GeneralMap from '../components/GeneralMap.vue'
import MyButton from '../components/MyButton.vue'
import FormSearch from '../components/FormSearch.vue'
import { useApi } from '../composables/api'
import { useSearch } from '../composables/search'



let latitude = ref()
let longitude = ref()
let zoom = ref()
let textToSearch = ref('')
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
        files.value.forEach(() => {
          files.value = files.value.filter(item => {
            return !(item.tipo === 'Medición de Radiaciones No Ionizantes (móviles)' || item.tipo === 'Descargo')
          })
          clearInterval(checkDomReady)
        })
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
  if(textToSearch.value != '' && textToSearch != '') {
  //   const data = await list(false, estado.value)
    files.value = search(files.value, textToSearch, ['area_asignada','tipo','usuario','fecha','expediente', 'area_actual'])
textToSearch = ''    
  } else {
   
    if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
      files.value = []
      const data = await list(false, estado.value)
      files.value.push(...data)
      console.log(files)

      files.value.forEach(() => {
      files.value = files.value.filter(item => {
        return !(item.tipo === 'Medición de Radiaciones No Ionizantes (móviles)' || item.tipo === 'Descargo')
      })
    })}
  }
  
}

</script>


<template>
  <heading>Mapa de Expedientes</heading>
  <div class="buttons-container">
    <my-button
      class="primary right"
      label="Volver"
      @on-tap="goBack"
    />
  </div>
  <div class="view-map-container">
    <div class="form-search-container">
      <form-search
        class="search-input"
        :text-to-search="textToSearch"
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
  
</template>


<style scoped>
.buttons-container {
  display: flex;
  flex-direction: row;
  gap: 10px;
  justify-content: end;
  /* margin: 0 5px; */
}
.view-map-container {
  position: relative
}

.form-search-container {
  position: absolute;  
  /* background-color: white; */
  top: 25px;
  z-index: 3000;
}
</style>