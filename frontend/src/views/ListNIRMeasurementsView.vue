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
import { exportFile, QBtn, QTable, QTd, QTh } from 'quasar'



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
  data.forEach((item) => {   
    item.localidad = getNameByCode('city', item.localidad)
    item.provincia = getNameByCode('province', item.provincia)
  })
  items.value = search(data, textoToSearch, ['localidad', 'provincia']) 
}

function viewItem(file_id, item) {  
  router.push(`/file/${file_id}/non_ionizing_radiation/${item}`)
}

function viewNirMap() {  
  router.push(`/nir_map`)
}

const columns = [
  { name: 'id',
    label: 'id', 
    field: 'id', 
    sortable: true, 
    align: 'center'
  },
  { name: 'localidad', label: 'Localidad', field: 'localidad', sortable: true, align: 'center' },
  { name: 'provincia', label: 'Provincia', field: 'provincia', sortable: true, align: 'center' },
  { name: 'area', label: 'Área/CCTE', field: 'area_asignada', sortable: true, align: 'center' },
  { name: 'cantidad', label: 'Cantidad de Mediciones', field: 'cantidad', sortable: true, align: 'center' },
  { name: 'valor_maximo', label: 'Valor Máximo [%]', field: 'valor_maximo', sortable: true, align: 'center' },
]

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
    <q-table
      dense
      flat
      wrap-cells
      :rows="items"
      :columns="columns"
      row-key="id"
      :pagination="{ rowsPerPage: 15 }"
      separator="vertical"
      table-class="zebra"
      table-header-style="height: 45px;"
    >
  
      <template v-slot:header-cell="props">
        <q-th :props="props">
          {{ props.col.label }}
        </q-th>
      </template>
      <template v-slot:body-cell-id="props">
          <q-td :props="props">
            <my-button
              class="primary center my-btn"
              :label="props.row.id.toString()"
              @on-tap="() => viewItem(props.row.file_id, props.row.id)"
            />
          </q-td>
        </template>
    </q-table>
  </div>
  <div class="status">
    <span><strong>Loading:</strong> {{ loading }}</span>
  </div>
  <footer-main class="footer-main" />
</template>

<style scoped>

:deep(div.zebra table tr:nth-child(even))
{background-color: #ebeded;}

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
.my-btn {
  height: fit-content;
}
</style>