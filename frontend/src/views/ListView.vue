<script setup>
import { useApi } from '../composables/api'
import { useSession } from '../composables/session'
import { onBeforeMount, ref, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'
import FormSearch from '../components/FormSearch.vue'
import { useSearch } from '../composables/search'
import FooterMain from '../components/FooterMain.vue'


const { list, loading, deleteFile } = useApi()
const { checkUser } = useSession()
const { search } = useSearch()
const router = useRouter()

const items = ref([])
const newItems = ref([])
const searchText = ref('')
const estado = ref('Pendiente')
const user_area = ref('')
const user_perfil = ref('')
const confirm_delete = ref({})


function viewItem(item) {  
  router.push(`/file/${item}`)
}

async function deleteItem(id) {  
  const response = await deleteFile(id)
  console.log(response)
  if(response && response.status === 200){
    confirm_delete.value[id] = 0
    items.value=[]
    const data = await list(false, estado.value)
    items.value.push(...data)
  } else {
      console.error("Failed to delete item", response)
  }
  
  // window.location.reload() 
}
const confirm = (id) => {
  console.log(confirm_delete.value)

  confirm_delete.value[id] = confirm_delete.value[id] === 1 ? 0 : 1
  console.log(confirm_delete.value)

}

onBeforeMount(async () => {
  if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
    const data = await list(false, estado.value)
    items.value.push(...data)
  } else {
      const data = await list(true, estado.value)
      items.value.push(...data)    
  }  
})

onMounted( async ()=> {
    const response = await checkUser()
    user_area.value = response.data.user_area
    user_perfil.value = response.data.user_perfil
})

async function searchFiles(searchText) {
  if(estado.value != 'Todos') {
    const data = await list(false, estado.value)
    items.value = search(data, searchText, ['area_asignada','tipo','fecha','expediente', 'area_actual'])
  } else {
      const data = await list(false, null)
      items.value = search(data, searchText, ['area_asignada','expediente', 'area_actual'])
  }
  
}

watch(estado, async(newValue, oldValue) => {
  if (newValue !== oldValue) {
    if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined && estado != 'Todos') {
      const data = await list(false, newValue)
      items.value = ([])
      items.value.push(...data)
      newItems.value.push(...data)
    } else {
      const data = await list(true, newValue)
      items.value = ([])
      items.value.push(...data)   
      newItems.value.push(...data)

  }  

  if (newValue == 'Todos') {
    const data = await list(false, null)
    items.value = ([])
    items.value.push(...data)
    newItems.value.push(...data)
  } 
    router.push({name: "list", query: { includeDeleted: 'false', fileStatus: newValue }})
  }
})

</script>
<template>
  <heading>Gestión de Expedientes</heading>
  <div class="files-menu">
    <form-search 
      :searchText = "searchText"
      placeholder = "Buscar Expedientes"
      @on-submit="searchFiles"
    />
    <div>
      <form-kit
          v-model="estado"
          type="select"
          :value="estado"
          name="estado" 
          :options="[
            'Pendiente',
            'Informado',
            'Todos',
          ]"
          outer-class="short-field"
        />
    </div>
  </div>
  <div class="list-container">
    <table class="files-table">
      <tr>
        <th>id</th>
        <th>Expediente</th>
        <th>Área</th>
        <th>Tipo de trámite</th>
        <th>Fecha y hora</th>
        <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">
          Status
        </th>
        <th>Ubicación</th>
        <th>Estado</th>
        <th v-if="user_area == 'AGCCTYL' && user_perfil == 'coordinator'">Acciones</th>
      </tr>
      <tr
        v-for="item in items"
        :key="item"
        v-bind:class="{ 'red-text': item.prioridad == 'Urgente'}"
      >
        <td>
          <my-button
            class="primary center"
            :label="(item.id.toString())"
            @on-tap="() => viewItem(item.id)"
          />
        </td>
        <td>{{ item.expediente }}</td> 
        <td>{{ item.area_asignada }}</td> 
        <td>{{ item.tipo }}</td> 
        <td>{{ item.fecha +" "+item.hora }}</td> 
        <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">
          {{ item.status }}
        </td>
        <td>{{ item.area_actual }}</td> 
        <td>{{ item.tramitacion }}</td> 
        <td v-if="user_area == 'AGCCTYL' && user_perfil == 'coordinator'"> 
          <div class="action-buttons-container">
            <my-button
              v-if="confirm_delete[item.id]!==1"
              class="tertiary center"
              label="Borrar"
              @on-tap="() => confirm(item.id)"
            />
            <my-button
              v-if="confirm_delete[item.id]===1"
              class="tertiary center"
              label="¿Confirmar?"
              @on-tap="deleteItem(item.id)"
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
.files-menu {
  display: flex;
  flex-direction: row;
  justify-content: space-between
}
.red-text {
  color: red;
}
  
</style>