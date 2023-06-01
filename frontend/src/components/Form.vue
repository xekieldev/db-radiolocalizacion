<script setup>
import FormRow from './FormRow.vue'
import { ref, unref, watch } from 'vue'
import { useTerritory } from '../composables/territory'

const emit = defineEmits(['onSubmit'])
const props = defineProps({
  context: String,
  title: String,
})
function submitHandler(fields) {
  emit('onSubmit', fields)
}

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

const values = ref({ province: 0, city: 0 })

const { provinces, cities, getProvinceCities } = useTerritory()

watch(values, (newValue, oldValue) => {
  getProvinceCities(newValue.province)
  if (newValue.province != oldValue.province) {
    newValue.city = unref(cities)[0].value
  }
})

console.log(provinces)
console.log(cities)


</script>

<template>

  <h2>{{title}}</h2>
  <form-kit type="form" @submit="submitHandler" submit-label="Cargar" v-model="values">
    <form-kit type="select" label="Localidad" name="localidad" :options="cities" validation="required| text" />
    <form-kit type="select" label="Provincia" name="provincia" :option="provinces" validation="required| text" />
    <!-- <form-row>
      <form-kit type="text" label="Expediente" name="expediente" :validation="[['required'], ['matches', /^EX-\d{4}-\d{6,10}-\s{2,3}-[A-Z]{3,7}-[A-Z]{3,10}#[A-Z]{2,8}$/,
        /^IF-\d{4}-\d{8}-[A-Z]{3}-[A-Z]{5}#[A-Z]{6}$/,/^NO-\d{4}-\d{8}-[A-Z]{3,8}-[A-Z]{3,10}#?[A-Z]{6}?$/,/^[A-Z]{5,20}\s?E?\s?\s\d{1,8}\/\d{4}$/,/^A\s{1}definir$/]]"
        validation-visibility="live" />
    </form-row>
    <form-row>
      <form-kit type="date" label="Fecha" name="fecha" />
      <form-kit type="time" label="Hora" name="hora" />
      <form-kit type="select" label="CCTE/Área" name="area" :options="area" />
    </form-row>
    <form-row>
      <form-kit type="text" label="Servicio" name="servicio" />
      <form-kit type="number" label="Frecuencia" name="frecuencia" step="0.001" validation-visibility="live" v-if="props.context === 'Radiolocalizacion'"/>
      <form-kit type="text" label="Clase de Emisión" name="claseEmision" />
      <form-kit type="text" label="Señal distintiva/Identificación" name="claseEmision" />
    </form-row>
    <form-row>
      <form-kit type="select" v-model="values" label="Localidad" name="localidad" :options="cities" validation="required| text" />
      <form-kit type="select" v-model="values" label="Provincia" name="provincia" :option="provinces" validation="required| text" />
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
      <form-kit type="text" label="Polarización" name="polarizacion" />
      <form-kit type="text" label="Cantidad" name="cantidad" />
      <form-kit type="text" label="Altura Media" name="altura" />

    </form-row>
    <form-row>
      <form-kit type="text" label="Tipo de Vínculo" name="tipoVinculo" />
      <form-kit type="text" label="Frecuencia Vínculo" name="frecuenciaVinc" />
      <form-kit type="text" label="Sistema Irradiante" name="irradianteVinc" />
      <form-kit type="text" label="Polarización" name="polarizacionVinc" />

    </form-row>
 -->
  </form-kit>
  <p>Value: {{ values }}</p>
</template>

  
<style>

</style>
  