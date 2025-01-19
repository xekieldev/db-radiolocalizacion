<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useTerritory } from '../composables/territory'
import DisplayRow from '../components/DisplayRow.vue'
import PropValue from '../components/PropValue.vue'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'
import FormNewActivity from '../components/FormNewActivity.vue'
import FormMoveFile from '../components/FormMoveFile.vue'
import FooterMain from '../components/FooterMain.vue'
import { perfil } from '../composables/loginstatus'


const { getFile, stationsPerFile, deleteStation, newActivity, getActivities, patchFile, getNIRMeasurementInFile } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()
const { getNameByCode } = useTerritory()
const tipoTramite = ref()
const currentLocation = ref()
const file = reactive({})
const nirMeasurement = reactive({})
const items = ref([])
const activities = ref([])
const menu = ref(false)

function editItem(file_id, id) {
  if (items.value.find(station => station.id === id).frecuencia != null || items.value.find(station => station.id === id).frecuencia != undefined) {
    router.currentRoute.value.query.rloc = 'true'
    router.push({ name: 'editStation', params: { file_id: file_id, id: id }, query: { rloc: 'true'} })
  } else {
    router.currentRoute.value.query.rloc = 'false'
    router.push({ name: 'editStation', params: { file_id: file_id, id: id }, query: { rloc: 'false'} })
  }
}

async function deleteItem(file_id, id) {  
  await deleteStation(file_id, id)
  window.location.reload() 
}

onBeforeMount(async () => {  
    const response = await getFile(router.currentRoute.value.path.slice(6))
    Object.assign(file, response.file)
    currentLocation.value = response.currentArea
    tipoTramite.value = file.tipo 
    if (tipoTramite.value !== 'Interferencias en Aeropuertos') {      
      file.localidad = getNameByCode('city', file.localidad)
      file.provincia = getNameByCode('province', file.provincia)
    }    
    const data = await stationsPerFile(file.id)
    items.value.push(...data)
    for (const item in items.value) {      
      items.value[item].localidad = getNameByCode("city", items.value[item].localidad)
      items.value[item].provincia = getNameByCode("province", items.value[item].provincia)
    }
    const file_id = currentRoute.value.params.id
    const activities_response = await getActivities(file_id)
    activities.value.push(...activities_response)
    if (file.tipo == 'Medición de Radiaciones No Ionizantes (móviles)') {
      const nirResponse = await getNIRMeasurementInFile(file.id)      
      if (nirResponse && nirResponse.length > 0) {
          Object.assign(nirMeasurement, nirResponse[0])
      } else {
          console.error("nirResponse no contiene datos válidos")
      }
    }
})

function newFile() { 
  router.push({name: "newFile"})
}

function createStation() { 
  router.push({name: "createStation", query: { rloc: 'true' }})
}

function createLocStation() { 
  router.push({name: "createStation", query: { rloc: 'false' }})
}

function goBack() {  
  router.back()
}

function viewItem(file_id, id) {  
  router.push(`/file/${file_id}/station/${id}`)
}

function viewNirMeas(file_id, id) {  
  router.push(`/file/${file_id}/non_ionizing_radiation/${id}`)
}

async function save(fields) {
  try {
    const file_id = currentRoute.value.params.id
    
    await newActivity (file_id, fields)
    // window.location.reload() 
    const activities_response = await getActivities(file_id)
    activities.value = activities_response

  } catch (error) {
    console.error(error)
  }
}


const currentDate = new Date(); 

const fullHours = currentDate.getHours() < 10 ? "0" + currentDate.getHours() : currentDate.getHours()
const fullMinutes = currentDate.getMinutes() < 10 ? "0" + currentDate.getMinutes() : currentDate.getMinutes()
// const fullSeconds = currentDate.getSeconds() < 10 ? "0" + currentDate.getSeconds() : currentDate.getSeconds()
const myTime = fullHours + ":" + fullMinutes //+ ":" + fullSeconds

const fullMonth = (currentDate.getMonth()+1)<10 ? "0"+(currentDate.getMonth()+1) : (currentDate.getMonth()+1)
const fullDay = currentDate.getDate()<10 ? "0"+currentDate.getDate() : currentDate.getDate()
const myDate = currentDate.getFullYear() + "-" + fullMonth + "-" + fullDay

async function patch_file(fields) {
  try {
    const file_id = currentRoute.value.params.id
    fields.fecha = myDate
    fields.hora = myTime
    await patchFile (file_id, fields)
    router.push({name: "list", query: { includeDeleted: 'false', fileStatus: 'Pendiente'}})
  } catch (error) {
    console.error(error)
  }
}

function openMenu() {
  menu.value = !menu.value
}

function closeDiv() {
  menu.value = false
}


</script>
<template>
  <div class="options-button">
    <my-button
      v-if="perfil == 'coordinator'"
      tabindex="0"
      class="secondary right"
      label="Alta Expediente"
      @on-tap="newFile"
    />
    <my-button
      tabindex="0"
      class="primary"
      label="Volver"
      @on-tap="goBack"
    />
  </div>
  <heading>
    {{ file.expediente }}
  </heading>
  <div class="menu-container">
    <div class="left-options">
      <my-button
        v-if="file.tramitacion != 'Finalizado'"
        tabindex="0"
        class="secondary"
        label="Nueva Radiolocalización"
        @on-tap="createStation"
      />
      <my-button
        v-if="file.tramitacion != 'Finalizado'"
        tabindex="0"
        class="secondary"
        label="Nueva Localización"
        @on-tap="createLocStation"
      />
      <my-button
        v-if="file.tipo === 'Medición de Radiaciones No Ionizantes (móviles)' && false"
        tabindex="0"
        class="primary"
        label="Ver Resultados RNI"
        @on-tap="viewNirMeas(file.id, nirMeasurement.id)"
      />
    </div>
    <my-button
      v-if="perfil === 'coordinator' && file.tramitacion != 'Finalizado'"
      tabindex="0"
      class="primary options-menu"
      label="Acciones"
      @on-tap="openMenu"
    />
  </div>
  <div
    v-if="menu == true"
    class="file-options"
  >
    <button
      class="close-button"
      @click="closeDiv"
    >
      x
    </button>
    <!-- <br> -->
    <div class="actions-menu">
      <form-move-file
        :context="tipoTramite"
        :file-number="file.expediente"
        :location="file.area_actual"
        :informe="file.informe"
        @on-submit="patch_file"
      />
    </div>
  </div>

  <div class="file-container">
    <display-row>
      <prop-value
        class="prop"
        label="id"
        :value="file.id"
      />
      <prop-value
        class="prop"
        label="Fecha y hora"
        :value="file.fecha + ' ' + file.hora"
      />
      <prop-value
        
        class="prop"
        label="Tipo de trámite"
        :value="file.tipo"
      />
      <prop-value
        class="prop"
        label="CCTE/Área"
        :value="file.area_asignada"
      />
      <prop-value
        class="prop"
        label="Prioridad"
        :value="file.prioridad"
      />
    </display-row>
    <display-row v-if="tipoTramite != 'Descargo'">
      <prop-value
        v-if="tipoTramite == 'Interferencias en Aeropuertos'"
        class="prop double"   
        label="Nota de Inicio"
        :value="file.nota_inicio"
      />
      <prop-value
        v-if="tipoTramite !== 'Medición de Radiaciones No Ionizantes (móviles)'"
        class="prop double"
        label="Usuario"
        :value="file.usuario"
      />
      <div v-if="tipoTramite !== 'Medición de Radiaciones No Ionizantes (móviles)'">
        <prop-value
          v-if="file.frecuencia == undefined || file.frecuencia == null"
          class="prop double"
          label="Frecuencia"
          value="---" 
        />
        <prop-value
          v-else
          class="prop double"
          label="Frecuencia"
          :value="file.frecuencia + ' ' + file.unidad" 
        />
      </div>
    </display-row>
    <display-row 
      v-if="tipoTramite !== 'Medición de Radiaciones No Ionizantes (móviles)' && tipoTramite !== 'Interferencias en Aeropuertos'"
    >
      <prop-value
        class="prop double"
        label="Localidad"
        :value="file.localidad"
      />
      <prop-value
        class="prop double"
        label="Provincia"
        :value="file.provincia"
      />
    </display-row>
    <display-row 
      v-if="tipoTramite === 'Medición de Radiaciones No Ionizantes (móviles)'"
    >
      <prop-value
        class="prop double"
        label="Localidad"
        :value="file.localidad"
      />
      <prop-value
        class="prop double"
        label="Provincia"
        :value="file.provincia"
      />
      <!-- <prop-value
        class="prop double"
        label="Cantidad"
        :value="nirMeasurement.cantidad"
      />
      <prop-value
        class="prop double"
        label="Valor Máximo [%]"
        :value="nirMeasurement.valor_maximo"
      /> -->
      <display-row>
        <prop-value
          v-if="nirMeasurement.observaciones"
          class="prop"
          label="Observaciones"
          :value="nirMeasurement.observaciones"
        />
        <prop-value
          v-else
          class="prop"
          label="Observaciones"
          value="---"
        />
      </display-row>
    </display-row>
    <display-row
      v-if="!(tipoTramite == 'Medición de Radiaciones No Ionizantes (móviles)' || tipoTramite == 'Descargo' || tipoTramite == 'Interferencias en Aeropuertos')"
    >
      <prop-value
        class="prop double"
        label="Domicilio"
        :value="file.domicilio"
      />
      <prop-value
        class="prop double"
        label="Latitud"
        :value="file.latitud"
      />
      <prop-value
        class="prop double"
        label="Longitud"
        :value="file.longitud"
      />
    </display-row>
    <display-row>
      <prop-value
        v-if="tipoTramite !== 'Medición de Radiaciones No Ionizantes (móviles)'"
        class="prop double"
        label="Motivo"
        :value="file.motivo"
      />
    </display-row>
    <display-row>
      <prop-value
        class="prop"
        label="Ubicación actual"
        :value="currentLocation"
      />
      <prop-value
        v-if="file.tramitacion == 'Informado'"
        class="prop"
        label="Informe"
        :value="file.informe"
      />
      <prop-value
        v-if="tipoTramite == 'Interferencias en Aeropuertos' && file.tramitacion == 'Informado'"
        class="prop"
        label="Nota de Fin"
        :value="file.nota_fin"
      />
    </display-row>
  </div>

  <br>
 
  <div
    v-if="items.length > 0"
    class="stations-table-container"
  >
    <h2 class="file-titles">
      Estaciones relacionadas
    </h2>
    <table class="stations-table">
      <tr>
        <th>id</th>
        <th>Identificación</th>
        <th>Servicio</th>
        <th>Frecuencia</th>
        <th>Emplazamiento</th>
        <!-- <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">Status</th> -->
        <th>Domicilio</th>
        <th>Localidad</th>
        <th>Provincia</th>
        <th v-if="router.currentRoute.value.query.includeDeleted === 'true'">
          Status
        </th>
        <th v-if="file.tramitacion != 'Finalizado'">
          Acciones
        </th>
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
        <!-- <td>{{ item.id }}</td> -->
        <td>{{ item.identificacion }}</td> 
        <td>{{ item.servicio }}</td> 
        <td v-if="item.frecuencia">
          {{ item.frecuencia +" "+item.unidad }}
        </td>
        <td v-else>
          ---
        </td>
        <td>{{ item.emplazamiento }}</td>
        <td>{{ item.domicilio }}</td>
        <td>{{ item.localidad }} </td>
        <td>{{ item.provincia }} </td>
        <!-- <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">{{ item.status }}</td> -->
        <td v-if="router.currentRoute.value.query.includeDeleted === 'true'">
          {{ item.status }}
        </td>
        <td v-if="file.tramitacion != 'Finalizado'"> 
          <div class="action-buttons-container">
            <my-button
              v-if="file.tramitacion != 'Finalizado'"
              class="primary center"
              label="Editar"
              @on-tap="() => editItem(item.file_id, item.id)"
            />
            <my-button
              v-if="file.tramitacion != 'Finalizado'"
              class="tertiary center"
              label="Borrar"
              @on-tap="() => deleteItem(item.file_id, item.id)"
            />
            <!-- <my-button @on-tap="() => deleteItem(item.id)" class="tertiary center" label="Borrar"/> -->
          </div>
        </td>
      </tr>
    </table>
  </div>
  
  <div class="activities-container">

    <form-new-activity
      v-if="file.tramitacion != 'Finalizado'"
      @on-submit="save"
    />

    <table v-if="activities && activities.length > 0">
      <tr>
        <th class="date-field">
          Fecha
        </th>
        <th>Detalle</th>
        <th class="usuario-field">Usuario</th>
      </tr>
      <tr
        v-for="activity in activities"
        :key="activity"
      >
        <td class="date-field">
          {{ activity.fecha }}
        </td>
        <td>{{ activity.detalle }}</td>
        <td>{{ activity.usuario }}</td>
      </tr>
    </table>
  </div>
  <footer-main class="footer-main" />
</template>

<style scoped>

.file-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
  padding: 0 30px;
}

.status{
  background-color: lightyellow;
}
.prop:hover {
  background-color: #bdc0c2;
}
.prop{
  flex-grow: 1;
  border-radius: 10px 0 0;
}
.prop.double{
  flex-grow: 4;
}
.menu-container {
  display: flex;
  flex-direction: row;
  gap: 5px;
  /* padding: 10px; */
  justify-content: space-between;
  padding: 0 30px;
}

.left-options {
  display: flex;
  flex-direction: row;
  gap: 5px;
}

.stations-table-container {
  display: flex;
  flex-direction: column;
  /* width: 100%; */
  /* padding: 30px; */
  margin: 30px;
  border-top: solid 1px gray;

}

.stations-table{
  justify-content: center; 
  margin-top: 10px;
  word-wrap: break-word;
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

.date-field {
  width: 20%;
}
.action-buttons-container {
  display: flex;
  flex-direction: row;
  gap: 5px;
  margin: 0;
}

.file-titles {
  padding-top: 10px;
  align-self: center;
  font-weight: 500;
}

.activities-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-top: 20px;
  /* border-top: solid 1px gray; */
  padding: 0 30px;
}

.field-date {
      flex: 0 0 25%;
}



/* .go-back-button {
  display: flex;
  flex-direction: row;
  gap: 10px;
  justify-content: end;
  margin: 5px 0;
} */
.options-button {
  display: flex;
  justify-content: end;
  gap: 10px;
  margin: 5px 0;
  padding: 0 30px;

}
.close-button {
  position: absolute;
  top: 0px;
  right: 0px;
  background: none;
  border: none;
  font-size: 15px;
  font-weight: 300;
  cursor: pointer;
  z-index: 100;
  padding: 0 30px;
}

.options-menu {
  display: flex;
  align-items: flex-end;
}

.actions-menu {
  padding: 0 30px;
}

.usuario-field {
  width: 15%;
}
</style>