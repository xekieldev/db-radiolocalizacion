<script setup>
import Heading from './Heading.vue';
import MyButton from './MyButton.vue';
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router'
import { useApi } from '../composables/api'
import { getNode } from '@formkit/core'
import FormRow from './FormRow.vue';

const router = useRouter()
const { getStatistics } = useApi()


console.log(getNode('startDate'))


// const fileStatus = ref('pending')
const inbound = ref(true)
const outbound = ref(false)
const pending = ref(false)
const items = ref({})


onMounted(async ()=> {

  items.value = await getStatistics(props.startDate, props.endDate, props.type, props.selectedArea)

})



const startDate = ref(props.startDate)
const endDate = ref(props.endDate)
const emit = defineEmits(['onSubmit'])


const props = defineProps({
title: String,
items: Object,
startDate: Date,
endDate: Date,
type: {
  validator(value) {
    // The value must match one of these strings
    return ['inbound', 'outbound', 'pending'].includes(value)
  }
},
selectedArea: {
  validator(value) {
    // The value must match one of these strings
    return ['Buenos Aires', 'Lima', 'Córdoba', 'Salta', 'Posadas', 'Neuquén', 'Comodoro Rivadavia'].includes(value)
  }
},
})


function handleFormChange(data) {
  console.log('objeto', { 
    startDate: props.startDate, 
    endDate: props.endDate, 
    type: props.type,
    area: props.selectedArea
  })
  
  console.log('function', data)
  
  router.push({ name: 'statistics', query: { 
    startDate: props.startDate, 
    endDate: props.endDate, 
    type: props.type,
    area: props.selectedArea,
    ...data
  }})
}

watch(()=> props, async (newValue, oldValue) => {
  console.log(newValue)
  // props.type = newValue.type
  items.value = await getStatistics( newValue.startDate, newValue.endDate, newValue.type, newValue.selectedArea)
console.log('para tablas', items.value)
  
}, {deep: true})


</script>

<template>
  <heading>{{ title }}</heading>
  <div class="stat-container">
  <div class="stat-menu">
    <h4 class="titles">Seleccione tipo</h4>
    <div class="type-btns-container">
      <my-button
        class="primary"
        :class="{ 'selected-btn': 'inbound' == type}"
        label="Ingresados"
        @on-tap="() => handleFormChange({type: 'inbound'})"
      />
      <my-button
        class="primary"
        :class="{ 'selected-btn': 'outbound' == type}"
        label="Egresados"
        @on-tap="() => handleFormChange({type: 'outbound'})"
      />
      <my-button
        class="primary"
        :class="{ 'selected-btn': 'pending' == type}"
        label="Pendientes"
        @on-tap="() => handleFormChange({type: 'pending'})"

      />
    </div>
    <br>
    <h4 class="titles">Seleccione fechas</h4>

    <form-kit
      type="group"
    >
    <div class="dates-container">
      <form-kit
        id="startDate"
        type="date"
        outer-class="date-input"
        label="Fecha de Inicio"
        v-model="startDate"
        name="startDate"
        validation="date_after:04-30-2024"
        validation-visibility="live"
        :validation-messages="{
          date_after: 'La fecha debe ser posterior al 01/05/2024.',
        }"
        @change="(event) => handleFormChange({startDate: event.target.value })"
      />
      <form-kit
        type="date"
        outer-class="date-input"
        label="Fecha de Fin"
        v-model="endDate"
        name="endDate"
        validation="date_after_node:startDate"
        validation-visibility="live"
        :validation-messages="{
          date_after_node: 'La fecha debe ser posterior a la Fecha de Inicio',
        }"
        @change="(event) => handleFormChange({endDate: event.target.value })"
      />
    </div>
    </form-kit>
    <h4 class="titles">Seleccione Área/CCTE</h4>
    <div class="type-btns-container">
      <my-button
        class="primary area-btn"
        :class="{ 'selected-btn': 'Buenos Aires' == selectedArea}"
        label="Buenos Aires"
        @on-tap="() => handleFormChange({area: 'Buenos Aires'})"
      />
      <my-button
        class="primary area-btn"
        :class="{ 'selected-btn': 'Lima' == selectedArea}"
        label="Lima"
        @on-tap="() => handleFormChange({area: 'Lima'})"
      />
      <my-button
        class="primary area-btn"
        :class="{ 'selected-btn': 'Córdoba' == selectedArea}"
        label="Córdoba"
        @on-tap="() => handleFormChange({area: 'Córdoba'})"
      />
      <my-button
        class="primary area-btn"
        :class="{ 'selected-btn': 'Salta' == selectedArea}"
        label="Salta"
        @on-tap="() => handleFormChange({area: 'Salta'})"
      />      
      <my-button
        class="primary area-btn"
        :class="{ 'selected-btn': 'Posadas' == selectedArea}"
        label="Posadas"
        @on-tap="() => handleFormChange({area: 'Posadas'})"
      />
      <my-button
        class="primary area-btn"
        :class="{ 'selected-btn': 'Neuquén' == selectedArea}"
        label="Neuquén"
        @on-tap="() => handleFormChange({area: 'Neuquén'})"
      />
      <my-button
        class="primary"
        :class="{ 'selected-btn': 'Comodoro Rivadavia' == selectedArea}"
        label="Comodoro Rivadavia"
        @on-tap="() => handleFormChange({area: 'Comodoro Rivadavia'})"
      />
    </div>
    
  </div>
  <div class="screen">
    <div class="titles-general">
      
    </div>
    
    <div class="tables">
      <div class="area-table">
        <h4 class="titles">Por CCTE/Área</h4>
        <table>
          <tr>
            <th>Centro/Área</th>
            <th>Cantidad</th>
          </tr>
          <tr
            v-for="(item, index) in items.Area"
                :key="index"
          >
            <td :class="{ 'selected-area': item.area == selectedArea}">{{ item.area }}</td>
            <td :class="{ 'selected-area': item.area == selectedArea}">{{ item.cantidad }}</td>
          </tr> 
        </table>
      </div>
      <div class="type-table">
        <h4 class="titles">Por Tipo</h4>
        <table>
          <tr>
            <th>Tipo</th>
            <th>Cantidad</th>
          </tr>
          <tr 
            v-for="(item, index) in items.Tipo"
                :key="index"
          >
            <td>{{ item.tipo }}</td>
            <td>{{ item.cantidad }}</td>
          </tr> 
      </table>
      </div>   
  </div>
</div>
</div>
</template>

<style scoped>
table {
  width: fit-content;
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
.stat-menu {
  background-color: #ebeded;
  height: 100%;
  width: 22%;
  padding: 10px;
  min-width: 170px;

}

.stat-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.type-btns-container {
  display: flex;
  flex-direction: row;
  width: 100%;
  gap: 5px;
  flex-wrap: wrap;
  justify-content: center;
}

.submit-button {
  background-color: #007BFF;
  margin: 10px 0 20px;
  padding: 10px 18px;
  border-radius: 20px;
  cursor: pointer;
  border: 1px solid #007BFF;
  font-weight: 600;  
  color: white;
}
.submit-button:hover {
  background-color: #005ec2;
  color: white
}
.tables {
  display: flex;
  flex-direction: row;
  gap: 30px;
  align-items: start;
}
.area-table {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.type-table {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.selected-btn {
  background-color: #007BFF;
  cursor: pointer;
  border: 1px solid #007BFF;
  font-weight: 600;  
  color: white;
  
}

.area-btn {
  flex: 1;
}

.selected-area {
  background-color: #7cd7fe;
  color: black;
  /* font-style: italic; */
  font-weight: 500;
}

.titles {
  font-weight: 500;
  display: flex;
  justify-content: center;
  margin-bottom: 5px;
}
.screen {
  display: flex;
  flex-direction: column;
}
.titles-general {
  display: flex;
  justify-content: center;
}

.dates-container {
  display: flex;
  flex-direction: row;
  gap: 5px;
  /* width: 100%; */
  flex-wrap: wrap;
  /* flex-wrap: wrap-reverse; */
}

.date-input {
  flex: 1;
  min-width: 125px;
  /* flex-wrap: wrap; */
  /* justify-self: center; */
}

</style>
