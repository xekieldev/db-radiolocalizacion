<script setup>
import { useApi } from '../composables/api'
import { onBeforeMount, reactive, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useTerritory } from '../composables/territory'
import Mapa from '../components/MapMain.vue'
import DisplayRow from '../components/DisplayRow.vue'
import PropValue from '../components/PropValue.vue'
import Heading from '../components/Heading.vue'
import MyButton from '../components/MyButton.vue'


const { getNonIonizingRadiation, getAllTechnicians } = useApi()
const { currentRoute } = useRouter()
const router = useRouter()
const route = useRoute()
const { getNameByCode } = useTerritory()


const currentPath = ref('')


function goBack() {  
  router.back()

}

const nirMeasurement = reactive({})
const technicians = reactive({})
const techniciansValues = reactive({})

onBeforeMount(async () => {
  console.log(currentRoute.value.params.id)
  
    const response = await getNonIonizingRadiation(currentRoute.value.params.id)
    console.log(response)
    
    const techResponse = await getAllTechnicians()
    Object.assign(nirMeasurement, response)
    Object.assign(technicians, response.technicians)
    Object.assign(techniciansValues, techResponse)
//     station.provincia = getNameByCode("province", response.station.provincia)
//     station.localidad = getNameByCode("city", response.station.localidad)    
})



</script>
<template>
  <heading>
    Mediciones de RNI
  </heading>

  <div class="container">
    <display-row> 
      <prop-value
        class="prop"
        label="id"
        :value="nirMeasurement.id"
      />
      <prop-value
        class="prop"
        label="Expediente"
        :value="nirMeasurement.expediente"
      />
    </display-row>
    <display-row> 
      <prop-value
        class="prop"
        label="Área"
        :value="nirMeasurement.area"
      />
      <prop-value
        class="prop"
        label="Fecha y hora"
        :value="nirMeasurement.fecha + ' ' + nirMeasurement.hora"
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
     
    </display-row>
    <display-row>
      <prop-value
        v-for="value, index in technicians"
        :key="value"
        class="prop technicians"
        label="Técnico"
        :value=" technicians[index].apellido + ', ' + technicians[index].nombre"
      />
    </display-row>
  </div>
  
</template>

<style scoped>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* text-transform: uppercase; */
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


</style>