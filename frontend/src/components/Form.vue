<script setup>
import FormRow from './FormRow.vue'

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



</script>

<template>

  <h2>{{title}}</h2>
  <form-kit type="form" @submit="submitHandler" submit-label="Cargar">
    <form-row>
      <form-kit type="text" label="Expediente" name="expediente" :validation="[['required'], ['matches', /^EX-\d{4}-\d{6,10}-\s{2,3}-[A-Z]{3,7}-[A-Z]{3,10}#[A-Z]{2,8}$/,
        /^IF-\d{4}-\d{8}-[A-Z]{3}-[A-Z]{5}#[A-Z]{6}$/,/^NO-\d{4}-\d{8}-[A-Z]{3,8}-[A-Z]{3,10}#?[A-Z]{6}?$/,/^[A-Z]{5,20}\s?E?\s?\s\d{1,8}\/\d{4}$/]]"
        validation-visibility="live" />
    </form-row>
    <form-row>
      <form-kit type="date" label="Fecha" name="fecha" />
      <form-kit type="time" label="Hora" name="hora" />
      <form-kit type="select" label="CCTE/Área" name="area" :options="area" />
    </form-row>
    <!--form-row>
      <form-kit type="text" label="Servicio" name="servicio" />
      <form-kit type="number" label="Frecuencia" name="frecuencia" step="0.001" validation-visibility="live" v-if="props.context === 'Radiolocalizacion'"/>
      <form-kit type="text" label="Clase de Emisión" name="claseEmision" />
      <form-kit type="text" label="Señal distintiva/Identificación" name="claseEmision" />
    </form-row>
    <form-row>
      <form-kit type="text" label="Localidad" name="localidad" validation="required| text" />
      <form-kit type="text" label="Provincia" name="provincia" validation="required| text" />
    </form-row>
    <form-row>
      <form-kit type="text" label="Domicilio" name="domicilio" validation="required| text" />
      <form-kit type="number" label="Latitud" name="latitud" validation="required| number" />
      <form-kit type="number" label="Longitud" name="longitud" validation="required| number" />

    </form-row>
    <form-row>
      <form-kit type="textarea" label="Observaciones" name="observacionesDom" />

    </form-row-->

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

  </form-kit>
</template>

  
<style>

</style>
  