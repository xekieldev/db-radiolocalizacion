<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useTerritory } from '../composables/territory'
import DisplayRow from '../components/DisplayRow.vue'
import PropValue from '../components/PropValue.vue'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'

const router = useRouter()
const { getNonIonizingRadiation, getAllTechnicians, getFile } = useApi()
const { currentRoute } = useRouter()
const { getNameByCode } = useTerritory()

const nirMeasurement = reactive({})
const technicians = reactive({})
const techniciansValues = reactive({})
const file = reactive({})

onBeforeMount(async () => {
    const response = await getNonIonizingRadiation(currentRoute.value.params.id)
    const techResponse = await getAllTechnicians()
    Object.assign(nirMeasurement, response.nir)
    const fileResponse = await getFile(nirMeasurement.file_id)
    Object.assign(file, fileResponse.file)
    file.localidad = getNameByCode("city", file.localidad)
    file.provincia = getNameByCode("province", file.provincia)    
    Object.assign(technicians, response.technicians)
    Object.assign(techniciansValues, techResponse)
})

function goBack() {  
  router.back()
}

</script>
<template>
  <div class="options-button">
    <my-button
      tabindex="0"
      class="primary"
      label="Volver"
      @on-tap="goBack"
    />
  </div>
  <heading>
    Mediciones de RNI (móviles)
  </heading>
  <div class="nir-container">
    <display-row> 
      <prop-value
        class="prop"
        label="id"
        :value="nirMeasurement.id"
      />
      <prop-value
        class="prop"
        label="Fecha y hora"
        :value="nirMeasurement.fecha + ' ' + nirMeasurement.hora"
      />
      <prop-value
        class="prop"
        label="Expediente"
        :value="file.expediente"
      />
      <prop-value
        class="prop"
        label="Área"
        :value="file.area_asignada"
      />
    </display-row>
    <display-row> 
      <prop-value
        class="prop"
        label="Localidad"
        :value="file.localidad"
      />
      <prop-value
        class="prop"
        label="Provincia"
        :value="file.provincia"
      />
      <prop-value
        class="prop"
        label="Cantidad de mediciones"
        :value="nirMeasurement.cantidad"
      />
      <prop-value
        class="prop"
        label="Valor máximo [%]"
        :value="nirMeasurement.valor_maximo"
      />
      <display-row>
        <prop-value
          v-for="value, index in technicians"
          :key="value"
          class="prop technicians"
          label="Técnico"
          :value=" technicians[index].apellido + ', ' + technicians[index].nombre"
        />
      </display-row>
    </display-row>
    <br>
    <div class="color-code">
      <div :class="['box-attributes', 'maya-blue', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) <= 1 }]">
        <p class="box-text">
          P &le; 1
        </p>
      </div>
      <div :class="['box-attributes', 'dodger-blue', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 1 && parseFloat(nirMeasurement.valor_maximo) <= 2 }]">
        <p class="box-text">
          1 &lt; P &le; 2
        </p>
      </div>
      <div :class="['box-attributes', 'cerulen-blue', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 2 && parseFloat(nirMeasurement.valor_maximo) <= 4 }]">
        <p class="box-text">
          2 &lt; P &le; 4
        </p>
      </div>
      <div :class="['box-attributes', 'light-green', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 4 && parseFloat(nirMeasurement.valor_maximo) <= 8 }]">
        <p class="box-text">
          4 &lt; P &le; 8
        </p>        
      </div>
      <div :class="['box-attributes', 'lime-green', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 8 && parseFloat(nirMeasurement.valor_maximo) <= 15 }]">
        <p class="box-text">
          8 &lt; P &le; 15
        </p>
      </div>
      <div :class="['box-attributes', 'green', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 15 && parseFloat(nirMeasurement.valor_maximo) <= 20 }]">
        <p class="box-text">
          15 &lt; P &le; 20
        </p>
      </div>
      <div :class="['box-attributes', 'golden-yellow', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 20 && parseFloat(nirMeasurement.valor_maximo) <= 35 }]">
        <p class="box-text">
          20 &lt; P &le; 35
        </p>
      </div>
      <div :class="['box-attributes', 'orange', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 35 && parseFloat(nirMeasurement.valor_maximo) <= 50 }]">
        <p class="box-text">
          35 &lt; P &le; 50
        </p>
      </div>
      <div :class="['box-attributes', 'orange-red', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 50 && parseFloat(nirMeasurement.valor_maximo) <= 100 }]">
        <p class="box-text">
          50 &lt; P &le; 100
        </p>
      </div>
      <div :class="['box-attributes', 'red', { 'marked-border': parseFloat(nirMeasurement.valor_maximo) > 100 }]">
        <p class="box-text">
          P > 100
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>

.nir-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* text-transform: uppercase; */
  padding: 0 30px;
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
.technicians{
  border-bottom: 1px solid #cbcdce;
}
.color-code {
  display: flex;
  flex-direction: row;
  /* align-items: center; */
  /* align-content: center;
  justify-content: center; */
}
.box-attributes {
  height: 50px;
  width: 90px; 
  border: solid 1px;
}
.box-text {
  font-weight: 800;
  font-size: 12px;
  color: black;
}
.marked-border {
  /* background-color: white; */
  border: 3px solid black;
  height: 70px;
  width: 100px;

}

.maya-blue {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #73c2fb;
  
}
.dodger-blue {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1e90ff;
}
.cerulen-blue {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #2a52be;
}
.light-green {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #90ee90;
}
.lime-green {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #32cd32 ;
}
.green{
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #008000 ;
}
.golden-yellow {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ffdf00;
}
.orange {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ffa500 ;
}
.orange-red {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ff4500;
}
.red {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ff0000;
}
.options-button {
  display: flex;
  justify-content: end;
  gap: 10px;
  margin: 5px 0;
  padding: 0 30px;

}
</style>