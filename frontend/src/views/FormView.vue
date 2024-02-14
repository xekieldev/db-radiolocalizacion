<script setup>
import { useApi } from '../composables/api'
import FormRow from '../components/FormRow.vue'
import Mapa from '../components/MapMain.vue'


const submitHandler = async (fields) => {
  console.log(fields)
  const api = useApi()
  const all = await api.list()
  console.log(all)
  api.create(fields)

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
  <form-kit
    type="form"
    @submit="submitHandler"
  >
    <form-row>
      <form-kit
        type="text"
        label="Expediente"
        name="expediente"
        :validation="[['required'], ['matches', /^EX-\d{4}-\d{8}-\s{2}-[A-Z]{3}-[A-Z]{5}#[A-Z]{6}$/,
                                     /^IF-\d{4}-\d{8}-[A-Z]{3}-[A-Z]{5}#[A-Z]{6}$/,/^NO-\d{4}-\d{8}-[A-Z]{3,8}-[A-Z]{3,10}#?[A-Z]{6}?$/]]"
        validation-visibility="live"
      />
    </form-row>
    <form-row>
      <form-kit
        type="date"
        label="Fecha"
        name="fecha"
      />
      <form-kit
        type="time"
        label="Hora"
        name="hora"
      />
      <form-kit
        type="select"
        label="CCTE/Área"
        name="area"
        :options="area"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Servicio"
        name="servicio"
      />
      <form-kit
        type="number"
        label="Frecuencia"
        name="frecuencia"
        step="0.001"
        validation-visibility="live"
      />
      <form-kit
        type="text"
        label="Clase de Emisión"
        name="claseEmision"
      />
      <form-kit
        type="text"
        label="Señal distintiva/Identificación"
        name="claseEmision"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Localidad"
        name="localidad"
        validation="required| text"
      />
      <form-kit
        type="text"
        label="Provincia"
        name="provincia"
        validation="required| text"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Domicilio"
        name="domicilio"
        validation="required| text"
      />
      <form-kit
        type="number"
        label="Latitud"
        name="latitud"
        validation="required| number"
      />
      <form-kit
        type="number"
        label="Longitud"
        name="longitud"
        validation="required| number"
      />
    </form-row>
    <form-row>
      <form-kit
        type="textarea"
        label="Observaciones"
        name="observaciones"
      />
    </form-row>

    <form-row>
      <form-kit
        type="text"
        label="Sistema Irradiante"
        name="irradiante"
      />
      <form-kit
        type="text"
        label="Polarización"
        name="polarizacion"
      />
      <form-kit
        type="text"
        label="Cantidad"
        name="cantidad"
      />
      <form-kit
        type="text"
        label="Altura Media"
        name="altura"
      />
    </form-row>
    <form-row>
      <form-kit
        type="text"
        label="Tipo de Vínculo"
        name="tipoVinculo"
      />
      <form-kit
        type="text"
        label="Frecuencia Vínculo"
        name="frecuenciaVinc"
      />
      <form-kit
        type="text"
        label="Sistema Irradiante"
        name="irradianteVinc"
      />
      <form-kit
        type="text"
        label="Polarización"
        name="polarizacionVinc"
      />
    </form-row>
  </form-kit>
  <mapa :position="[47.313220, -1.319482]" />
</template>

  
<style>
@media (min-width: 1024px) {
  .form {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }

  /* input[name="expediente"] {
    display: flex;
    background-color: aquamarine;
  } */
}
</style>
  