<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'
import FormSearch from '../components/FormSearch.vue'
import { useSearch } from '../composables/search'
import FooterMain from '../components/FooterMain.vue'
import { userData, perfil } from '../composables/loginstatus'
import { useTerritory } from '../composables/territory'
import { exportFile, QBtn, QTable, QTd, QTh, QTr, QIcon } from 'quasar'




const { list, loading, deleteFile } = useApi()
const { search } = useSearch()
const { getNameByCode } = useTerritory()
const router = useRouter()

const items = ref([])
const newItems = ref([])
const inputTextToSearch = ref('')
const estado = ref('Pendiente')
const user_area = ref('')
const confirm_delete = ref({})

user_area.value = userData.value.area

function viewItem(item) {  
  router.push(`/file/${item}`)
}

function newFile() { 
  router.push({name: "newFile"})
}

function editItem(id) {
  router.push(`/file/${id}/edit`) 
}

function viewMap() {  
  router.push(`/files_map`)
}

async function deleteItem(id) {  
  const response = await deleteFile(id)
  if(response && response.status === 200){
    confirm_delete.value[id] = 0
    items.value=[]
    const data = await list(false, estado.value)
    items.value.push(...data)
  } else {
      console.error("Failed to delete item", response)
  }
}
const confirm = (id) => {
  confirm_delete.value[id] = confirm_delete.value[id] === 1 ? 0 : 1
}

onBeforeMount(async () => {
  if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined) {
    const data = await list(false, estado.value)
    items.value.push(...data)
    items.value.forEach((item) => {
      if (item.tipo !== 'Interferencias en Aeropuertos') {      
        item.localidad = getNameByCode('city', item.localidad)
        item.provincia = getNameByCode('province', item.provincia)
      }  
    })
      
  } else {
      const data = await list(true, estado.value)
      items.value.push(...data)    
  }  
})

async function searchFiles(textToSearch) {
  if(estado.value != 'Todos') {
    const data = await list(false, estado.value)
    data.forEach(item => {
      if (item.tipo !== 'Interferencias en Aeropuertos') {      
        item.localidad = getNameByCode('city', item.localidad)
        item.provincia = getNameByCode('province', item.provincia)
      }  
    })
    items.value = search(data, textToSearch, ['area_asignada','tipo','fecha','nota_inicio','expediente', 'area_actual','localidad','provincia','aeropuerto','prioridad','motivo'])
  } else {
      const data = await list(false, null)
      data.forEach(item => {
        if (item.tipo !== 'Interferencias en Aeropuertos') {      
          item.localidad = getNameByCode('city', item.localidad)
          item.provincia = getNameByCode('province', item.provincia)
        }  
      })
      items.value = search(data, textToSearch, ['area_asignada','tipo','fecha','nota_inicio','expediente', 'area_actual','localidad','provincia','aeropuerto','prioridad','motivo'])
  }
  
}

watch(estado, async(newValue, oldValue) => {
  if (newValue !== oldValue) {
    if(router.currentRoute.value.query.includeDeleted === 'false' || router.currentRoute.value.query.includeDeleted === undefined && estado.value != 'Todos') {
      const data = await list(false, newValue)
      items.value = ([])
      items.value.push(...data)
      items.value.forEach((item) => {
        if (item.tipo !== 'Interferencias en Aeropuertos') {      
          item.localidad = getNameByCode('city', item.localidad)
          item.provincia = getNameByCode('province', item.provincia)
        }  
      })
      newItems.value.push(...data)
    } else {
        const data = await list(true, newValue)
        items.value = ([])
        items.value.push(...data)
        items.value.forEach((item) => {
          if (item.tipo !== 'Interferencias en Aeropuertos') {      
            item.localidad = getNameByCode('city', item.localidad)
            item.provincia = getNameByCode('province', item.provincia)
          }  
        }) 
        newItems.value.push(...data)
    }  

  if (newValue == 'Todos') {
    const data = await list(false, null)
    items.value = ([])
    items.value.push(...data)
    items.value.forEach((item) => {
      if (item.tipo !== 'Interferencias en Aeropuertos') {      
        item.localidad = getNameByCode('city', item.localidad)
        item.provincia = getNameByCode('province', item.provincia)
      }  
    })
    newItems.value.push(...data)
  } 
    router.push({name: "list", query: { includeDeleted: 'false', fileStatus: newValue }})
  }
})

const columns = [
  { name: 'id',
    label: 'id', 
    field: 'id', 
    sortable: true, 
    align: 'center'
  },
  { name: 'expediente', label: 'Expediente', field: 'expediente', sortable: true, align: 'center', style:'white-space: nowrap;' },
  { name: 'area_asignada', label: 'Área asignada', field: 'area_asignada', sortable: true, align: 'center' },
  { name: 'tipo', label: 'Tipo de trámite', field: 'tipo', sortable: true, align: 'center' },
  { name: 'localidad', label: 'Localidad/Aeropuerto', field: row => row.tipo != 'Interferencias en Aeropuertos' ? row.localidad : row.aeropuerto, sortable: true, align: 'center' },
  { name: 'provincia', label: 'Provincia', field: row => row.tipo != 'Interferencias en Aeropuertos' ? row.provincia : '---', sortable: true, align: 'center' },
  { name: 'fecha', label: 'Fecha ingreso', field: row => `${row.fecha} ${row.hora}`, sortable: true, align: 'center' },
  { name: 'fecha_informe', label: 'Fecha informe', field: row => `${row.fecha_informe} ${row.hora_informe}`, sortable: true, align: 'center' },
  { name: 'fecha_fin', label: 'Fecha fin', field: row => `${row.fecha_fin}`, sortable: true, align: 'center' },
  { name: 'ubicacion', label: 'Ubicación actual', field: 'area_actual', sortable: true, align: 'center' },
  { name: 'status', label: 'Estado', field: 'tramitacion', sortable: true, align: 'center' },
  { name: 'acciones', label: 'Acciones', field: 'acciones', align: 'center' },
]

function wrapCsvValue (val, formatFn, row) {
  let formatted = formatFn !== void 0
    ? formatFn(val, row)
    : val

  formatted = formatted === void 0 || formatted === null
    ? ''
    : String(formatted)

  formatted = formatted.split('"').join('""')
  /**
   * Excel accepts \n and \r in strings, but some other CSV parsers do not
   * Uncomment the next two lines to escape new lines
   */
  // .split('\n').join('\\n')
  // .split('\r').join('\\r')

  return `"${formatted}"`
}

function exportTable () {
        // naive encoding to csv format
        const exportColumns = columns.filter(col => col.name !== 'acciones')
        const content = [exportColumns.map(col => wrapCsvValue(col.label))].concat(
          items.value.map(row => exportColumns.map(col => wrapCsvValue(
            typeof col.field === 'function'
              ? col.field(row)
              : row[ col.field === void 0 ? col.name : col.field ],
            col.format,
            row
          )).join(','))
        ).join('\r\n')

        const status = exportFile(
          'SNCTE-DB-export.csv',
          content,
          'text/csv'
        )

        if (status !== true) {
          notify({
            message: 'Browser denied file download...',
            color: 'negative',
            icon: 'warning'
          })
        }
      }
 
</script>
<template>
  <heading>Gestión de Expedientes</heading>
  <div class="files-menu">
    <form-search 
      :text-to-search="inputTextToSearch"
      placeholder="Buscar Expedientes"
      @on-submit="searchFiles"
    />
    
    <div class="list-sub-actions">
      <my-button
        class="quinary"
        label="Exportar a .csv"
        @click="exportTable"
        />
      <my-button
        class="secondary right view-map-button"
        label="Ver Mapa"
        @on-tap="viewMap"
      />
      <my-button
        v-if="perfil == 'coordinator'"
        tabindex="0"
        class="primary center"
        label="Alta Expediente"
        @on-tap="newFile"
      />
      <form-kit
        v-model="estado"
        type="select"
        :value="estado"
        name="estado" 
        :options="[
          'Pendiente',
          'Informado',
          'Finalizado',
          'Todos',
        ]"
        outer-class="short-field"
        style="height: 35px; padding: 8px 30px 8px 10px;"
      />
    </div>
  </div>
  <div class="list-container">
    <q-table
      dense
      flat
      wrap-cells
      sort-by="provincia"
      :rows="items"
      :columns="columns"
      row-key="id"
      :pagination="{ 
        rowsPerPage: 30,
        sortBy:'fecha',
        descending: true
       }"
      separator="vertical"
      table-class="zebra"
      table-header-style="height: 45px;"
    >
    
      <!-- Encabezado de la tabla -->
      <template v-slot:header-cell="props">
        <q-th :props="props">
          {{ props.col.label }}
        </q-th>
      </template>

      <template v-slot:header-cell-acciones="props">
        <q-th :props="props" v-if="user_area == 'AGCCTYL' && perfil == 'coordinator'">
          {{ props.col.label }}
        </q-th>
      </template>

      <template v-slot:header-cell-fecha_informe="props">
        <q-th :props="props" v-if="estado == 'Informado' || estado == 'Finalizado' || estado == 'Todos'">
          {{ props.col.label }}
        </q-th>
      </template>

      <template v-slot:header-cell-fecha_fin="props">
        <q-th :props="props" v-if="estado == 'Finalizado' || estado == 'Todos'">
          {{ props.col.label }}
        </q-th>
      </template>
      
      <!-- Celdas del cuerpo de la tabla -->
      <template v-slot:body-cell-expediente="props">
        <q-td :props="props">
          {{ props.row.expediente }}
          
          <!-- Agregar el icono cuando se cumpla la condición -->
          <q-icon
            v-if="props.row.prioridad === 'Urgente' || props.row.tipo === 'Interferencias en Aeropuertos'"
            name="warning"
            color="negative"
            size="xs"
            class="q-ml-xs"
          />
        </q-td>
      </template>

      <template v-slot:body-cell-fecha_informe="props">
        <q-td :props="props" v-if="estado == 'Informado' || estado == 'Finalizado' || estado == 'Todos'">
          <span v-if="props.row.fecha_informe">
            {{ props.row.fecha_informe }} {{ props.row.hora_informe || '' }}
          </span>
          <span v-else>---</span>
        </q-td>
      </template>

      <template v-slot:body-cell-fecha_fin="props">
        <q-td :props="props" v-if="estado == 'Finalizado' || estado == 'Todos'">
          <span v-if="props.row.fecha_fin">
            {{ props.row.fecha_fin }} {{ props.row.hora_fin || '' }}
          </span>
          <span v-else>---</span>
        </q-td>
      </template>

      <!-- Celdas personalizadas para el id -->
      <template v-slot:body-cell-id="props">
        <q-td :props="props">
          <my-button
            class="primary center my-btn"
            :label="props.row.id.toString()"
            @on-tap="() => viewItem(props.row.id)"
          />
        </q-td>
      </template>

      <!-- Celdas personalizadas para las acciones -->
      <template v-slot:body-cell-acciones="props">
        <q-td :props="props" v-if="user_area == 'AGCCTYL' && perfil == 'coordinator'">
          <div class="action-buttons-container">
            <my-button
              class="primary center"
              label="Editar"
              @on-tap="() => editItem(props.row.id)"
            />
            <my-button
              v-if="confirm_delete[props.row.id] !== 1"
              class="tertiary center"
              label="Borrar"
              @on-tap="() => confirm(props.row.id)"
            />
            <my-button
              v-if="confirm_delete[props.row.id] === 1"
              class="tertiary center"
              label="¿Confirmar?"
              @on-tap="deleteItem(props.row.id)"
            />
          </div>
        </q-td>
      </template>

    </q-table>
    <div class="status">
      <span><strong>Loading:</strong> {{ loading }}</span>
    </div>
  </div>
  <footer-main class="footer-main" />
</template>

<style scoped>

:deep(div.zebra table tr:nth-child(even))
{background-color: #ebeded;}

.list-container{
  display: flex;
  flex-direction: column;
  /* max-width: 900px; */
  width: 100%;
  justify-content: center;
  margin-top: 10px;
  padding: 0 30px;
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
  white-space: nowrap;
}
tr:nth-child(odd) {
  background-color: #ebeded;
  border-radius: 10px 0 0;
}

.action-buttons-container {
  display: flex;
  flex-direction: row;
  gap: 5px;
  margin: 0;
}
.action-column {
  width: 30px;
}
.files-menu {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0 30px;
}
.red-text {
  color: red;
  font-weight: 700;
}
.list-sub-actions {
  display: flex;
  flex-direction: row;
  gap: 10px;
  justify-content: space-between;
}
.short-field {
  margin-bottom: 0;
}
.my-btn {
  height: fit-content;
}

</style>