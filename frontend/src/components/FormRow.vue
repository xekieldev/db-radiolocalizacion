<script setup>

</script>

<template>
  <div class="form-row-container">
    <slot />
  </div>
</template>

<style scoped>
.form-row-container {
  display: flex;
  flex-direction: row;
  gap: 10px; 
}

</style>
