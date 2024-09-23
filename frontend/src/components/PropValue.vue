<script setup>

defineProps({
  
  label: String,
  value: [Number, String, Array],

  }
)
</script>

<template>
  <div class="container">
    <div class="label">
      {{ label }}
    </div>
    <div class="value">
      {{ value }}
    </div>
  </div>
</template>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
  gap: 5px;
  
}
.label{
  width: 100%;
  background-color: #C6C6C6;
  color: #0B1742;
  padding: 5px;
  font-weight: 700;
  text-align: center;
  border-radius: 10px 0 0;
}
.value{
  text-align: center;
}

</style>
