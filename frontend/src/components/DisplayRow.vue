<script setup>

</script>

<template>
  <div class="container1">
    <slot />
  </div>
</template>

<style scoped>
.container1{
  /* background-color: red; */
  display: flex;
  flex-direction: row;
  gap: 5px;
  width: 100%;
  flex-wrap: wrap;
  justify-content: space-around;

  
}

</style>