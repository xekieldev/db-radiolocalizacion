<script setup>
import Heading from './Heading.vue';
import MyButton from './MyButton.vue';
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router'
import { useApi } from '../composables/api'
import { getNode } from '@formkit/core'

const router = useRouter()
const { getStatistics } = useApi()


console.log(getNode('startDate'))


// const fileStatus = ref('pending')
const inbound = ref(true)
const outbound = ref(false)
const pending = ref(false)
const items = ref({})


onMounted(async ()=> {

  items.value = await getStatistics(props.startDate, props.endDate, props.type == 'inbound', props.type == 'outbound', props.type == 'pending')

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
})


function handleFormChange(data) {
  console.log('objeto', { 
    startDate: props.startDate, 
    endDate: props.endDate, 
    type: props.type,
  })
  
  console.log('function', data)
  
  router.push({ name: 'statistics', query: { 
    startDate: props.startDate, 
    endDate: props.endDate, 
    type: props.type,
    ...data
  }})
}

watch(()=> props, async (newValue, oldValue) => {
  console.log(newValue)
  // props.type = newValue.type
  items.value = await getStatistics( newValue.startDate, newValue.endDate, newValue.type == 'inbound', newValue.type == 'outbound', newValue.type == 'pending')
  
}, {deep: true})


</script>

<template>
  <heading>{{ title }}</heading>
  <div class="stat-container">
  <div class="stat-menu">
    <h3>Seleccione tipo</h3>
    <div class="stat-type-btns">
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
    <h3>Seleccione fechas</h3>

    <form-kit
      name="dates"
      id="dates"
      type="form"
      submit-label="Cargar"
      :config="{ validationVisibility: 'submit',
                validation:'required', 
                validationMessages:{ required:'Campo obligatorio', 
                                      
                }
      }"
      :actions="false"
    >
    <!-- <form-row> -->
      <!-- {{formkit}} -->
      <form-kit
        id="startDate"
        type="date"
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
        label="Fecha de Fin"
        v-model="endDate"
        name="fechaFin"
        validation="date_after:04-30-2024"
        validation-visibility="live"
        :validation-messages="{
          date_after: 'La fecha debe ser posterior al 01/05/2024.',
        }"
        @change="(event) => handleFormChange({endDate: event.target.value })"

      />
      
    </form-kit>
    
  </div>
  <div class="screen">
    <div class="titles-general">
      <h2 v-if="inbound">Trámites Ingresados</h2>
      <h2 v-if="outbound">Trámites Egresados</h2>
      <h2 v-if="pending">Trámites Pendientes</h2>
    </div>
    
    <div class="tables">
      <div class="area-table">
        <h4 class="tables-title">Por CCTE/Área</h4>
        <table>
          <tr>
            <th>Centro/Área</th>
            <th>Cantidad</th>
          </tr>
          <tr 
            v-for="(item, index) in items.Area"
                :key="index"
          >
            <td>{{ item.area }}</td>
            <td>{{ item.cantidad }}</td>
          </tr> 
        </table>
      </div>
      <div class="type-table">
        <h4 class="tables-title">Por Tipo</h4>
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
}

.stat-container {
  display: flex;
  flex-direction: row;
  gap: 20px;
}

.stat-type-btns {
  display: flex;
  flex-direction: row;
  gap: 3px;
  flex-wrap: wrap;
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
  /* margin: 10px 0 20px;
  padding: 10px 18px;
  border-radius: 20px; */
  cursor: pointer;
  border: 1px solid #007BFF;
  font-weight: 600;  
  color: white;
}

.tables-title {
  font-weight: 500;
}
.screen {
  display: flex;
  flex-direction: column;
}
.titles-general {
  display: flex;
  justify-content: center;
}

</style>
