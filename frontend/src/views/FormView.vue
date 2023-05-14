<script setup>
import { useApi } from '../composables/api'
import FormRow from '../components/FormRow.vue'

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
  <form-kit type="form" @submit="submitHandler">
    <form-row>
      <form-kit type="text" label="Expediente" name="expediente" validation="required| text"
        validation-visibility="live" />
    </form-row>
    <form-row>
      <form-kit type="date" label="Fecha" name="fecha" />
      <form-kit type="time" label="Hora" name="hora" />
      <form-kit type="select" label="CCTE/Área" name="area" :options="area" />
    </form-row>
    <form-row>
      <form-kit type="text" label="Servicio" name="servicio" />
      <form-kit type="number" label="Frecuencia" name="frecuencia" step="0.001" validation-visibility="live" />
      <form-kit type="text" label="Clase de Emisión" name="claseEmision" />
      <form-kit type="text" label="Señal distintiva/Identificación" name="claseEmision" />
    </form-row>
    <form-row>
      <form-kit type="text" label="Localidad" name="localidad" />
      <form-kit type="text" label="Provincia" name="provincia" />
    </form-row>
    <form-row>
      <form-kit type="text" label="Domicilio" name="domicilio" />
      <form-kit type="number" label="Latitud" name="latitud" />
      <form-kit type="number" label="Longitud" name="longitud" />

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

  </form-kit>
</template>

  
<style>
@media (min-width: 1024px) {
  .form {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}</style>
  