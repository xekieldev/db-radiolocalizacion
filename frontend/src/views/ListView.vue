<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'
import FormSearch from '../components/FormSearch.vue'
import { useSearch } from '../composables/search'
import FooterMain from '../components/FooterMain.vue'


const { list, loading, deleteFile } = useApi()
const { search } = useSearch()

const router = useRouter()

const items = ref([])
const searchText = ref('')



function viewItem(item) {  
  router.push(`/file/${item}`)
}

async function deleteItem(item) {  
  await deleteFile(item)
  window.location.reload() 
}

onBeforeMount(async () => {
  if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
    const data = await list()
    items.value.push(...data)
  } else {
      const data = await list(true)
      items.value.push(...data)    
  }  
})

async function searchFiles(searchText) {
  const data = await list(false)
  items.value = search(data, searchText, ['area','expediente'])  
}

</script>
<template>
  <heading>Gestión de Expedientes</heading>
  <div class="files-menu">
    <form-search 
      :searchText = "searchText"
      placeholder = "Buscar Expedientes"
      @on-submit="searchFiles"
    />
  </div>
  <div class="list-container">
    <table class="files-table">
      <tr>
        <th>id</th>
        <th>Expediente</th>
        <th>Área</th>
        <th>Fecha y hora</th>
        <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">
          Status
        </th>
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
        <td>{{ item.area }}</td> 
        <td>{{ item.fecha +" "+item.hora }}</td> 
        <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">
          {{ item.status }}
        </td>
        <td> 
          <div class="action-buttons-container">
            <my-button
              class="tertiary center"
              label="Borrar"
              @on-tap="() => deleteItem(item.id)"
            />
          </div>
        </td>
      </tr>      
    </table>
    <div class="status">
        <span><strong>Loading:</strong> {{ loading }}</span>
    </div>
  </div>
  <footer-main class="footer-main"/>
</template>

<style scoped>
.list-container{
  display: flex;
  flex-direction: column;
  /* max-width: 900px; */
  width: 100%;
  justify-content: center;
  margin-top: 10px;
}
.status{
    background-color: lightyellow;
}
.files-table {
  justify-content: center; 
  font-size: 12px; 
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

.action-buttons-container {
  display: flex;
  flex-direction: row;
  gap: 1px;
  margin: 0;
}
  
</style>