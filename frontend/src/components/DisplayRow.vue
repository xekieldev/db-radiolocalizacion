<script setup>

</script>

<template>
  <div class="container-display-row">
    <slot />
  </div>
</template>

<style scoped>
.container-display-row{
  display: flex;
  flex-direction: row;
  gap: 5px;
  width: 100%;
  flex-wrap: wrap;
  justify-content: space-around;

  
}

</style>