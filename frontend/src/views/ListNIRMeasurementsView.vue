<script setup>
import { useApi } from '../composables/api'
import { useTerritory } from '../composables/territory'
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'
import FormSearch from '../components/FormSearch.vue'
import { useSearch } from '../composables/search'
import FooterMain from '../components/FooterMain.vue'


const { getAllNonIonizingRadiation, loading } = useApi()
const { getNameByCode, getCoordinates } = useTerritory()
const router = useRouter()
const { search } = useSearch()

const items = ref([])
const coordinates = ref({})
const textoToSearch = ref('')


onBeforeMount(async () => {
  const data = await getAllNonIonizingRadiation()
  items.value.push(...data)  
  for (const item in items.value) {
    coordinates.value = getCoordinates(items.value[item].localidad)
    items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
    items.value[item].provincia = getNameByCode("province", items.value[item].provincia)     
  }
})  

async function searchNIRMeasurement(textoToSearch) {
  const data = await getAllNonIonizingRadiation()
  items.value = search(data, textoToSearch, ['localidad', 'provincia'])  
}

function viewItem(file_id, item) {  
  router.push(`/file/${file_id}/non_ionizing_radiation/${item}`)
}

function viewNirMap() {  
  router.push(`/nir_map`)
}

</script>
<template>
  <heading>Listado de Mediciones de Radiaciones No Ionizantes</heading>
  <div class="nir-menu">
    <form-search 
      :text-to-search="textoToSearch"
      placeholder="Buscar mediciones de RNI"
      @on-submit="searchNIRMeasurement"
    />
    <div class="right-section">
      <my-button
        class="secondary right view-map-button"
        label="Ver Mapa"
        @on-tap="viewNirMap"
      />
    </div> 
  </div>
  <div class="nir-measurements-container">
    <table class="nir-table">
      <tr>
        <th>id</th>
        <!-- <th>id Expediente</th> -->
        <th>Localidad</th>
        <th>Provincia</th>
        <th>Área/CCTE</th>
        <th>Cantidad de Mediciones</th>
        <th>Valor Máximo [%]</th>
        <!-- <th>Acciones</th> -->
      </tr>
      <tr
        v-for="item in items"
        :key="item"
      >
        <td>
          <my-button
            class="primary center"
            :label="(item.id.toString())"
            @on-tap="() => viewItem(item.file_id, item.id)"
          />
        </td> 
        <!-- <td class="file-field">{{ item.file_id }}</td>  -->
        <td>{{ item.localidad }}</td> 
        <td>{{ item.provincia }}</td>
        <td>{{ item.area_asignada }}</td>
        <td>{{ item.cantidad }}</td>
        <td>{{ item.valor_maximo }}</td>
        <!-- <td>
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
          </td> -->
      </tr>  
    </table>
  </div>
  <div class="status">
    <span><strong>Loading:</strong> {{ loading }}</span>
  </div>
  <footer-main class="footer-main" />
</template>

<style scoped>

.status{
  background-color: lightyellow;
  margin: 0 30px;
}
.nir-measurements-container{
  justify-content: center; 
  margin-top: 10px;
  font-size: 12px;
  padding: 0 30px;
}
.nir-table {
  width: 100%;
}
.file-field {
  /* display: flex;
  flex: 0 0 80%; */
  width: 300px;
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

.nir-menu {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0 30px;
}
.right-section {
  display: flex;
  flex-direction: row;
  gap: 10px;
}

</style>