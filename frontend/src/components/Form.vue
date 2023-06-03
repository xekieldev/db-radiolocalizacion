<script setup>
import FormRow from './FormRow.vue'
import { ref, unref, watch, reactive } from 'vue'
import { useTerritory } from '../composables/territory'

const emit = defineEmits(['onSubmit'])
const props = defineProps({
  context: String,
  title: String,
})
function submitHandler(fields) {
  emit('onSubmit', fields)
}
const tipoVinculo = [{
  value: 'Radioeéctrico',
  label: 'Radioeléctrico'
}, {
  value: 'Físico',
  label: 'Físico'
}]

const tipoPolarizacion = [{
  value: 'Vertical',
  label: 'Vertical'
}, {
  value: 'Horizontal',
  label: 'Horizontal'
}, {
  value: 'Circular',
  label: 'Circular'
}
]

const area = [{
  value: 'AGCCTYL',
  label: 'AGCCTYL'
},
{
  value: 'Buenos Aires',
  label: 'Buenos Aires'
},
{
  value: 'Cordoba',
  label: 'Córdoba'
},
{
  value: 'Salta',
  label: 'Salta'
},
{
  value: 'Posadas',
  label: 'Posadas'
},
{
  value: 'Neuquen',
  label: 'Neuquén'
},
{
  value: 'Comodoro Rivadavia',
  label: 'Com. Rivadavia'
}]

const province = ref("54")
const city = ref("06021010000")
const { provinces, cities, getProvinceCities } = useTerritory()

watch(province, (newValue, oldValue) => {
  getProvinceCities(newValue)
  if (newValue != oldValue) {
    city.value = cities.value[0]
  }
})
const values = { province, city }

</script>

<template>
  <h2>{{ title }}</h2>
  <form-kit type="form" @submit="submitHandler" submit-label="Cargar">
    <form-row>
      <form-kit type="text" label="Expediente" name="expediente" :validation="[['required'], ['matches', /^EX-\d{4}-\d{6,10}-\s{2,3}-[A-Z]{3,7}-[A-Z]{3,10}#[A-Z]{2,8}$/,
        /^IF-\d{4}-\d{8}-[A-Z]{3}-[A-Z]{5}#[A-Z]{6}$/,
        /^NO-\d{4}-\d{8}-[A-Z]{3,8}-[A-Z]{3,10}#?[A-Z]{6}?$/,
        /^[A-Z]{5,20}\s?E?\s?\s\d{1,8}\/\d{4}$/,
        /^A\s{1}definir$/]]" validation-visibility="live" />
    </form-row>
    <form-row>
      <form-kit type="date" label="Fecha" name="fecha" />
      <form-kit type="time" label="Hora" name="hora" />
      <form-kit type="select" label="CCTE/Área" name="area" :options="area" />
    </form-row>
    <form-row>
      <form-kit type="text" label="Servicio" name="servicio" validation-label="servicio"
        validation-visibility="live" />
      <form-kit type="number" label="Frecuencia" name="frecuencia" step="0.001" validation-visibility="live"
        v-if="props.context === 'Radiolocalizacion'" />
      <form-kit type="text" label="Clase de Emisión" name="claseEmision" />
      <form-kit type="text" label="Señal distintiva/Identificación" name="claseEmision" />
    </form-row>
    <form-row>
      <form-kit type="select" label="Provincia" v-model="province" name="province" :options="provinces"
        validation="required| text" />
      <form-kit type="select" label="Localidad" v-model="city" name="city" :options="cities"
        validation="required| text" />
    </form-row>
    <form-row>
      <form-kit type="text" label="Domicilio" name="domicilio" validation="required| text" />
      <form-kit type="number" label="Latitud" name="latitud" validation="required| number" />
      <form-kit type="number" label="Longitud" name="longitud" validation="required| number" />

    </form-row>
    <form-row>
      <form-kit type="textarea" label="Observaciones" name="observacionesDom" />
    </form-row>

    <form-row>
      <form-kit type="text" label="Sistema Irradiante" name="irradiante" />
      <form-kit type="select" label="Polarización" name="polarizacion" :options="tipoPolarizacion"/>
      <form-kit type="text" label="Cantidad" name="cantidad" />
      <form-kit type="text" label="Altura Media" name="altura" />

    </form-row>
    <form-row>
      <form-kit type="select" label="Tipo de Vínculo" name="tipoVinculo" :options="tipoVinculo" />
      <form-kit type="text" label="Frecuencia Vínculo" name="frecuenciaVinc" step="0.001" validation-visibility="live"/>
      <form-kit type="text" label="Sistema Irradiante" name="irradianteVinc" />
      <form-kit type="select" label="Polarización" name="polarizacionVinc" :options="tipoPolarizacion"/>

    </form-row>

  </form-kit>
  <p>Value: {{ values }}</p>
</template>

  
<style></style>
  