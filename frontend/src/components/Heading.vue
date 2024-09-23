<script setup>

</script>

<template>
  <div class="heading-container">
    <slot />
  </div>
</template>

<style scoped>
.heading-container{
  display: flex;
  font-size: 25px;
  font-weight: 500;
  color: #0B1742;
  justify-content: center;
  width: 100%;
  flex-direction: row;
  padding: 5px;
  margin-bottom: 10px; 
}

</style>
