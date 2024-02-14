<script setup>

const props = defineProps({
  
  label: String,
  value: [Number, String, Array],

  }
)
</script>

<template>
  <div class="container">
    <div class="label">{{ label }}</div>
    <div class="value">{{ value }}</div>
  </div>
</template>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
  gap: 5px;
  
}
.label{
  /* display: flex; */
  width: 100%;
  background-color: #cbcdce;
  color: #0e0e0e;
  padding: 5px;
  font-weight: 700;
  text-align: center;
  border-radius: 10px 0 0;
}


</style>
