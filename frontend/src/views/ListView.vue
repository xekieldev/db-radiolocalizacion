<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, ref } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue';
import MyButton from '../components/MyButton.vue';
import FormRow from '../components/FormRow.vue';


const { list, loading, deleteFile } = useApi()

const router = useRouter()

const items = ref([])
const searchText = ref()



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

async function searchFiles() {
  const searchStringTemp = searchText.value ? searchText.value.toLowerCase() : ''
  const searchString = searchStringTemp.split('+')
  const data = await list(false)
  // console.log("data: ", data)
  
  const searchResult = data.filter((item) => {
    const id = item.id
    const area = item.area ? item.area.toLowerCase() : ''
    const expediente = item.expediente ? item.expediente.toLowerCase() : ''
    
    return id == searchString || expediente.includes(searchString) || area.includes(searchString)
    
  })
  
   items.value = searchResult

}

</script>
<template>
  <heading>Gestión de Expedientes</heading>
  <div class="list-container">
    <div class="bar-menu">
      <form-row class="search-bar">
        <form-kit
          v-model="searchText"
          outer-class="field-search"
          type="text"
          name="searchInput"
          placeholder="Buscar expedientes"
        />
        <my-button
          class="secondary buscar-btn"
          label="Buscar"
          @on-tap="() => searchFiles()"
        />
      </form-row>
    </div>
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
</template>

<style scoped>
.list-container{
  display: flex;
  flex-direction: column;
  /* max-width: 900px; */
  width: 100%;
  justify-content: center;
  font-size: 14px;
}
.status{
    background-color: lightyellow;
}
.files-table {
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

.action-buttons-container {
  display: flex;
  flex-direction: row;
  gap: 1px;
  margin: 0;
}

.search-bar {
  display: flex;
  justify-content: start;
  align-items: start;
  margin-right: auto;
  
}
.buscar-btn {
  margin: 0 5px;
  bottom: 2px;
  
}
.formkit-outer.search-bar {
  margin: 0;
}

.field-search {
  display: flex;
  /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
  flex: 0 0 75%;
  margin: 0;
  
}

.bar-menu {
  display: flex;
  justify-content: space-between;
  top: 2px;
}
  
</style>