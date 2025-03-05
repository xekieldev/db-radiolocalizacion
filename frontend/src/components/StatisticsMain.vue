<script setup>
import Heading from './Heading.vue'
import MyButton from './MyButton.vue'
import { onBeforeMount, onMounted, reactive, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import PieChart from './PieChart.vue'
import BarChart from './BarChart.vue'
import { useApi } from '../composables/api'

const router = useRouter()
const { getStatistics, getAllNonIonizingRadiation } = useApi()

const areaToShow = [
  'Buenos Aires',
  'Lima',
  'Córdoba',
  'Salta',
  'Posadas',
  'Neuquén',
  'Comodoro Rivadavia'
]
const fileType = [
  'Interferencias en Aeropuertos',
  'Interferencias en Estaciones Radioeléctricas',
  'Interferencias en Estaciones de Radiodifusión',
  'Interferencias Celulares',
  'Inspección de Estaciones Radioeléctricas',
  'Inspección de Estaciones de Radiodifusión',
  'Radiolocalización de Estaciones Radioeléctricas',
  'Radiolocalización de Estaciones de Radiodifusión',
  'Detectar actividad',
  'Denuncias del Público en General',
  'Medición de Radiaciones No Ionizantes',
  'Otros',
  'Inspección Aeronave',
  // 'Medición de Radiaciones No Ionizantes (móviles)',
  'Descargo'
]

const items = ref([])
const nirStat = ref([])
const chartLabels = ref([])
const chartValues = ref([])
const chartData = ref({
  labels: [],
  datasets: [
    {
      backgroundColor: [],
      data: [],
    }
  ]
})
const nirChartLabels = ref([])
const nirChartValues = ref([])
const nirChartData = ref({
  labels: [], 
  datasets: [
    {
      backgroundColor: [],
      data: [],
    }
  ]
})
const chartColors = ref([])
const countByArea = reactive({})
const countNIRByArea = reactive({})
let totalByArea = ref(0)
const countByType = reactive({})
const totalByType = ref(0)
let totalLocalidades = ref(0);
let totalCantidad = ref(0);

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

const startDate = ref(props.startDate)
const endDate = ref(props.endDate)
const emit = defineEmits(['onSubmit'])

onMounted(async ()=> {
  items.value = await getStatistics( props.startDate, props.endDate, props.type, props.selectedArea)
  nirStat.value = await getAllNonIonizingRadiation()
  
    
  areaToShow.forEach((area) => {
      countByArea[area] = 0;
    })

    areaToShow.forEach((area) => {
    const localidades = nirStat.value.filter((item) => item.area_asignada === area).length;
    const cantidad = nirStat.value.filter((item => item.area_asignada === area)).reduce((sum, item) => sum + item.cantidad, 0)
    countNIRByArea[area] = { localidades, cantidad}
    totalLocalidades.value += localidades
    totalCantidad.value += cantidad
  })
  


  if (props.type === 'inbound') {
    // Recorrer items.value y contar los areas
    items.value.forEach((item) => {
      if (countByArea[item.area_asignada] !== undefined) {
        if (item.tipo !== "Medición de Radiaciones No Ionizantes (móviles)"  && item.tipo != "Tareas Programadas") {
          countByArea[item.area_asignada]++
        }
      }
    })
  } else {
      // Recorrer items.value y contar los areas
      items.value.forEach((item) => {
        if (countByArea[item.recibe] !== undefined) {
          if (item.tipo !== "Medición de Radiaciones No Ionizantes (móviles)"  && item.tipo != "Tareas Programadas") {
            countByArea[item.recibe]++
          }
        }
      })
  }
  totalByArea.value = Object.values(countByArea).reduce((total, value) => total + value, 0)
  
  fileType.forEach((type) => {
    countByType[type] = 0;
  })
  console.log(items.value)
  
  if (props.type === 'inbound' && props.selectedArea) {
    items.value.forEach((item) => {
      if (countByType[item.tipo] !== undefined) {
        if ( item.area_asignada === props.selectedArea) {
          countByType[item.tipo]++;
        }
      }
    })
  } else {
      // Recorrer items.value y contar los tipos
    items.value.forEach((item) => {
      if (countByType[item.tipo] !== undefined) {
        countByType[item.tipo]++;
      }
    })
  }
  totalByType.value = Object.values(countByType).reduce((total, value) => total + value, 0)


  Object.entries(countByType).forEach(([key, value], index) => {
    chartLabels.value[index] = key;   // El tipo (nombre de la categoría)
    chartValues.value[index] = value; // La cantidad asociada

  const hue = (index * 40) % 360; // Cambia el tono (0-360) para crear colores únicos
  const saturation = 90;          // Saturación constante
  const lightness = 50;           // Luminosidad constante
  const alpha = 0.4;              // Transparencia constante

  chartColors.value[index] = `hsla(${hue}, ${saturation}%, ${lightness}%, ${alpha})`;
  })

  chartData.value = {
    labels: chartLabels.value,
    datasets: [
      {
        backgroundColor: chartColors.value,
        data: chartValues.value,
      }
    ]
  }

  Object.entries(countNIRByArea).forEach(([key, value], index) => {
    nirChartLabels.value[index] = key;   // El tipo (nombre de la categoría)
    nirChartValues.value[index] = value.cantidad; // La cantidad asociada
    
    const hue = (index * 57) % 360; // Cambia el tono (0-360) para crear colores únicos
    const saturation = 75;          // Saturación constante
    const lightness = 45;           // Luminosidad constante
    const alpha = 0.4;              // Transparencia constante

    chartColors.value[index] = `hsla(${hue}, ${saturation}%, ${lightness}%, ${alpha})`;
  })

  nirChartData.value = {
    labels: nirChartLabels.value,
    datasets: [
      {
        backgroundColor: chartColors.value,
        data: nirChartValues.value,
      }
    ]
  }

})

function handleFormChange(data) {
  router.push({ name: 'statistics', query: { 
    startDate: props.startDate, 
    endDate: props.endDate, 
    type: props.type,
    area: props.selectedArea,
    ...data
    }
  })
}

watch(()=> props, async (newValue, oldValue) => {
  items.value = await getStatistics( newValue.startDate, newValue.endDate, newValue.type, newValue.selectedArea)  
  areaToShow.forEach((area) => {
      countByArea[area] = 0
      // countNIRByArea[area] =0
    })
    totalLocalidades.value = 0
    totalCantidad.value = 0
    areaToShow.forEach((area) => {
      const localidades = nirStat.value
        .filter(
          (item) =>
            item.area_asignada === area &&
            (!props.startDate || new Date(item.fecha) >= new Date(props.startDate)) &&
            (!props.endDate || new Date(item.fecha) <= new Date(props.endDate))
        ).length;

      const cantidad = nirStat.value
        .filter(
          (item) =>
            item.area_asignada === area &&
            (!props.startDate || new Date(item.fecha) >= new Date(props.startDate)) &&
            (!props.endDate || new Date(item.fecha) <= new Date(props.endDate))
        )
        .reduce((sum, item) => sum + item.cantidad, 0);

      countNIRByArea[area] = { localidades, cantidad };
      totalLocalidades.value += localidades
      totalCantidad.value += cantidad
    })
    Object.entries(countNIRByArea).forEach(([key, value], index) => {
    nirChartLabels.value[index] = key;   // El tipo (nombre de la categoría)
    nirChartValues.value[index] = value.cantidad; // La cantidad asociada
    
    // const hue = (index  * 40) % 360; // Cambia el tono (0-360) para crear colores únicos
    // const saturation = 90;          // Saturación constante
    // const lightness = 50;           // Luminosidad constante
    // const alpha = 0.4;              // Transparencia constante

    // chartColors.value[index] = `hsla(${hue}, ${saturation}%, ${lightness}%, ${alpha})`;
  })

  nirChartData.value = {
    labels: nirChartLabels.value,
    datasets: [
      {
        backgroundColor: chartColors.value,
        data: nirChartValues.value,
      }
    ]
  }
  
  if (newValue.type === 'inbound') {
    // Recorrer items.value y contar los areas
    items.value.forEach((item) => {
      if (countByArea[item.area_asignada] !== undefined) {
        if (item.tipo !== "Medición de Radiaciones No Ionizantes (móviles)"  && item.tipo != "Tareas Programadas") {
          countByArea[item.area_asignada]++
        }
      }
    })
  } else if (newValue.type === 'outbound' || newValue.type === 'finished') {
    // Recorrer items.value y contar los areas
      items.value.forEach((item) => {
        if (countByArea[item.area_asignada] !== undefined) {
          if (item.tipo !== "Medición de Radiaciones No Ionizantes (móviles)"  && item.tipo != "Tareas Programadas") {
            countByArea[item.area_asignada]++
          }
        }
      })
  } else {
      // Recorrer items.value y contar los areas
      items.value.forEach((item) => {
        if (countByArea[item.recibe] !== undefined) {
          if (item.tipo !== "Medición de Radiaciones No Ionizantes (móviles)"  && item.tipo != "Tareas Programadas") {
            countByArea[item.recibe]++
          }
        }
      })
  }
  totalByArea.value = Object.values(countByArea).reduce((total, value) => total + value, 0)
  
  fileType.forEach((type) => {
    countByType[type] = 0;
  })
  
  if (newValue.selectedArea) {
    items.value.forEach((item) => {
      if (countByType[item.tipo] !== undefined) {
        if ( item.area_asignada === newValue.selectedArea) {
          countByType[item.tipo]++;
        }
      }
    })
  } else {
      // Recorrer items.value y contar los tipos
    items.value.forEach((item) => {
      if (countByType[item.tipo] !== undefined) {
        countByType[item.tipo]++;
      }
    })
  }
  totalByType.value = Object.values(countByType).reduce((total, value) => total + value, 0)

  Object.entries(countByType).forEach(([key, value], index) => {
    chartLabels.value[index] = key;   // El tipo (nombre de la categoría)
    chartValues.value[index] = value; // La cantidad asociada

    // const baseRed = 0
    // const baseGreen = 0
    // const baseBlue = 255
    // const alpha = 0.1 + index * 0.05 // Ajusta el nivel de transparencia para cada color

    // chartColors.value[index] = `rgba(${baseRed}, ${baseGreen}, ${baseBlue - index * 10}, ${alpha})`
  })

  chartData.value = {
  labels: chartLabels.value,
  datasets: [
    {
      backgroundColor: chartColors.value,
      data: chartValues.value,
    }
  ]
}

}, {deep: true})


</script>

<template>
  <heading>{{ title }} {{ selectedArea }} </heading>
  <div class="stat-container">
  <div class="stat-menu">
    <h2 class="titles filters">Filtros</h2>
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
        v-if="endDate"
        type="date"
        style="background: white"
        outer-class="date-input"
        label="Fecha de Inicio"
        v-model="startDate"
        name="startDate"
        @change="(event) => handleFormChange({startDate: event.target.value })"
      />
      <form-kit
        type="date"
        style="background: white"
        outer-class="date-input"
        inner-class="date-input-field"
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
        v-if="selectedArea !== 'Buenos Aires'"
        class="primary area-btn"
        :class="{ 'selected-btn': 'Buenos Aires' == selectedArea}"
        label="Buenos Aires"
        @on-tap="() => handleFormChange({area: 'Buenos Aires'})"
      />
      <my-button
        v-else
        class="primary area-btn"
        :class="{ 'selected-btn': 'Buenos Aires' == selectedArea}"
        label="Buenos Aires"
        @on-tap="() => handleFormChange({area: null})"
      />
      <my-button
        v-if="selectedArea !== 'Lima'"
        class="primary area-btn"
        :class="{ 'selected-btn': 'Lima' == selectedArea}"
        label="Lima"
        @on-tap="() => handleFormChange({area: 'Lima'})"
      />
      <my-button
        v-else
        class="primary area-btn"
        :class="{ 'selected-btn': 'Lima' == selectedArea}"
        label="Lima"
        @on-tap="() => handleFormChange({area: null})"
      />
      <my-button
        v-if="selectedArea !== 'Córdoba'"
        class="primary area-btn"
        :class="{ 'selected-btn': 'Córdoba' == selectedArea}"
        label="Córdoba"
        @on-tap="() => handleFormChange({area: 'Córdoba'})"
      />
      <my-button
        v-else
        class="primary area-btn"
        :class="{ 'selected-btn': 'Córdoba' == selectedArea}"
        label="Córdoba"
        @on-tap="() => handleFormChange({area: null})"
      />
      <my-button
        v-if="selectedArea !== 'Salta'"
        class="primary area-btn"
        :class="{ 'selected-btn': 'Salta' == selectedArea}"
        label="Salta"
        @on-tap="() => handleFormChange({area: 'Salta'})"
      />
      <my-button
        v-else
        class="primary area-btn"
        :class="{ 'selected-btn': 'Salta' == selectedArea}"
        label="Salta"
        @on-tap="() => handleFormChange({area: null})"
      />    
      <my-button
        v-if="selectedArea !== 'Posadas'"
        class="primary area-btn"
        :class="{ 'selected-btn': 'Posadas' == selectedArea}"
        label="Posadas"
        @on-tap="() => handleFormChange({area: 'Posadas'})"
      />
      <my-button
        v-else
        class="primary area-btn"
        :class="{ 'selected-btn': 'Posadas' == selectedArea}"
        label="Posadas"
        @on-tap="() => handleFormChange({area: null})"
      />
      <my-button
        v-if="selectedArea !== 'Neuquén'"
        class="primary area-btn"
        :class="{ 'selected-btn': 'Neuquén' == selectedArea}"
        label="Neuquén"
        @on-tap="() => handleFormChange({area: 'Neuquén'})"
      />
      <my-button
        v-else
        class="primary area-btn"
        :class="{ 'selected-btn': 'Neuquén' == selectedArea}"
        label="Neuquén"
        @on-tap="() => handleFormChange({area: null})"
      />
      <my-button
        v-if="selectedArea !== 'Comodoro Rivadavia'"
        class="primary"
        :class="{ 'selected-btn': 'Comodoro Rivadavia' == selectedArea}"
        label="Comodoro Rivadavia"
        @on-tap="() => handleFormChange({area: 'Comodoro Rivadavia'})"
      />
      <my-button
        v-else
        class="primary"
        :class="{ 'selected-btn': 'Comodoro Rivadavia' == selectedArea}"
        label="Comodoro Rivadavia"
        @on-tap="() => handleFormChange({area: null})"
      />
    </div>
  </div>
  <div class="screen">
    <div class="tables">
      <div class="area-table">
        <h4 class="titles">Por CCTE/Área</h4>
        <table>
          <tr>
            <th>Centro/Área</th>
            <th>Cantidad</th>
          </tr>
          <tr
            v-for="(cantidad, area) in countByArea"
                :key="area"
          >
            <td :class="{ 'selected-area': area == selectedArea}">{{ area }}</td>
            <td :class="{ 'selected-area': area == selectedArea}">{{ cantidad }}</td>
          </tr> 
          <tr style="background-color: lightblue;">
            <td style="font-weight: 700;">Total</td>
            <td style="font-weight: 700;">{{ totalByArea }}</td>
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
            v-for="(cantidad, tipo) in countByType"
                :key="tipo"
          >
            <td>{{ tipo }}</td>
            <td>{{ cantidad }}</td>
          </tr> 
          <tr style="background-color: lightblue;">
            <td style="font-weight: 700;">Total</td>
            <td style="font-weight: 700;">{{ totalByType }}</td>
          </tr>
      </table>
      </div>   
    </div>
  </div>
  <div class="pie-container">
      <pie-chart
        :chartData="chartData"/>
  </div>
  <div class="nir-table">
    <h4 class="titles">RNI móviles Por CCTE/Área</h4>
        <table>
          <tr>
            <th>Centro/Área</th>
            <th>Localidades</th>
            <th>Mediciones</th>
          </tr>
          <tr
            v-for="(values, area) in countNIRByArea"
                :key="area"
          >
            <td :class="{ 'selected-area': area == selectedArea}">{{ area }}</td>
            <td :class="{ 'selected-area': area == selectedArea}">{{ values.localidades }}</td>
            <td :class="{ 'selected-area': area == selectedArea}">{{ values.cantidad }}</td>
          </tr> 
          <tr style="background-color: lightblue;">
            <td style="font-weight: 700;">Total</td>
            <td style="font-weight: 700;">{{ totalLocalidades }}</td>
            <td style="font-weight: 700;">{{ totalCantidad }}</td>
          </tr>
        </table>
        <div class="bar-chart-container">
            <bar-chart
              :chartData="nirChartData"/>
        </div>
  </div>
</div>

</template>

<style scoped>
table {
  width: fit-content;
  font-size: 12px;
}

td{
  text-align: center;
  padding: 2px;
}
th{
  text-align: center;
  padding: 5px;
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
  padding: 0 30px;
}

.type-btns-container {
  display: flex;
  flex-direction: row;
  width: 100%;
  gap: 3px;
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
.filters {
  font-size: 18px;
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

.formkit-input.date-input-field {
  background: white;
}

.pie-container {
  width: 23%;
  flex:1;
  justify-self: start;
  padding-top: 35px;;
}

.nir-table {
  display: flex;
  flex-direction: column;
  max-width: 100%;
  margin: 0 auto;
}

.nir-table table {
  width: 95%; /* Solo ocupa el ancho necesario según el contenido */
  /* margin: 0 auto; Centra la tabla dentro del contenedor */
  /* border-collapse: collapse; */
}

.bar-chart-container {
  height: 230px; /* Altura fija para el gráfico */
  margin: 0; /* Centra el gráfico */
  width: 95%; /* Adapta el ancho al contenido */
}


</style>
