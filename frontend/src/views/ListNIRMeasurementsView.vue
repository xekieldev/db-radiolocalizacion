<script setup>
import { useApi } from '../composables/api'
import { useTerritory } from '../composables/territory'
import { onBeforeMount, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'
import FormRow from '../components/FormRow.vue'



const { getAllNonIonizingRadiation, delete_non_ionizing_radiation, loading } = useApi()
const { getNameByCode, getCoordinates } = useTerritory()
const router = useRouter()

function createItem() {  
  router.push('/non_ionizing_radiation/create')
}

const items = ref([])
const status = ref({})
const coordinates = ref({})
const searchText = ref()



onBeforeMount(async () => {
    const data = await getAllNonIonizingRadiation()
    items.value.push(...data)    
    for (const item in items.value) {
        coordinates.value = getCoordinates(items.value[item].localidad)
        items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
        items.value[item].provincia = getNameByCode("province", items.value[item].provincia)     
      }
})  

async function searchStations() {
  const searchStringTemp = searchText.value ? searchText.value.toLowerCase() : ''
  const searchString = searchStringTemp.split('+')
  const data = await getAllNonIonizingRadiation()
  const searchResult = data.filter((item) => {
    const id = item.id
    const localidad = getNameByCode("city", item.localidad) ? getNameByCode("city", item.localidad).toLowerCase() : '' 
    const provincia = getNameByCode("province", item.provincia) ? getNameByCode("province", item.provincia).toLowerCase() : '' 
    
    return id == searchString || localidad.includes(searchString) || provincia.includes(searchString)
    
  })
  
  items.value = searchResult
  for (const item in items.value) {
    coordinates.value = getCoordinates(items.value[item].localidad)
    items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
    items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
  }
}

function viewItem(item) {  
  router.push(`/non_ionizing_radiation/${item}`)
}

const confirmar = (id) => {
      status.value[id] = status.value[id] === 1 ? 0 : 1
}


async function del(id) {
    try { 
      await delete_non_ionizing_radiation(id)
      status.value[id] = 0
      window.location.reload()
    } catch (error) {
    console.error(error)

    }
    
  }
  
function viewNirMap() {  

router.push(`/nir_map`)
}

</script>
<template>
  <heading>Listado de Mediciones de Radiaciones No Ionizantes</heading>
    <div class="bar-menu">
      <form-row class="search-bar">
        <form-kit
          v-model="searchText"
          outer-class="field-search"
          type="text"
          name="searchInput"
          placeholder="Buscar localidad/provincia"
        />
        <my-button
          class="secondary buscar-btn"
          label="Buscar"
          @on-tap="() => searchStations()"
        />
      </form-row>
      <div class="view-map-container">
        <my-button
          class="secondary right view-map-button"
          label="Ver Mapa"
          @on-tap="viewNirMap"
        />
        <my-button
          class="secondary right"
          label="Nueva Medición de RNI"
          @on-tap="createItem"
        />
      </div>
      
    </div>
    <table class="nir-table">
      <tr>
        <th>id</th>
        <th>Expediente</th>
        <th>Localidad</th>
        <th>Provincia</th>
        <th>Área/CCTE</th>
        <th>Cantidad de Mediciones</th>
        <th>Valor Máximo [%]</th>
        <th>Acciones</th>
      </tr>
      <tr
        v-for="item in items"
        :key="item"
      >
        <td>
          <my-button
            class="primary center"
            :label="(item.id.toString())"
            @on-tap="() => viewItem(item.id)"
          />
        </td> 
        <td>{{ item.expediente }}</td> 
        <td>{{ item.localidad }}</td> 
        <td>{{ item.provincia }}</td>
        <td>{{ item.area }}</td>
        <td>{{ item.cantidad }}</td>
        <td>{{ item.valor_maximo }}</td>
        <td>
          <my-button
            v-if="status[item.id]!=1"
            class="primary center"
            label="Borrar"
            @on-tap="confirmar(item.id)"
          />
          <my-button
            v-if="status[item.id]===1"
            class="tertiary center"
            label="¿Confirmar?"
            @on-tap="del(item.id)"
          />
        </td>
      </tr>
    
      
    </table>
    <div class="status">
        <span><strong>Loading:</strong> {{ loading }}</span>
      </div>
  <!-- </div> -->
</template>

<style scoped>

.status{
    background-color: lightyellow;
}
.nir-table{
  justify-content: center; 
  margin-top: 10px;
  
}
th, td{
  text-align: center;
  padding: 5px;
}
th{
  font-weight: 700;
  background-color: #cbcdce;
  border-radius: 10px 0 0;

}
tr:nth-child(odd) {
  background-color: #ebeded;
  border-radius: 10px 0 0;

}
.danger {
  color: red;
  font-weight: 700;
  border: 1px solid red;
}
.danger:hover {
  background-color: red;
}

.field-search {
  display: flex;
  /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
  /* flex: 0 0 50%; */
  margin: 0;
  
}
.search-bar {
  display: flex;
  justify-content: end;
  align-items: end;
  margin-right: auto;
  
}
.buscar-btn {
  margin: 0 5px;
  bottom: 2px;
  
}
.bar-menu {
  display: flex;
  justify-content: space-between;
  top: 2px;
}

.view-map-container {
  display: flex;
  flex-direction: row;
  gap: 5px;
  right: 0;
  margin-left: auto;
  
}

</style>