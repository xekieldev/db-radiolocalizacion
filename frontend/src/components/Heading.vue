<script setup>

</script>

<template>
  <div class="heading-container">
    <slot />
  </div>
</template>

<style scoped>
.heading-container{
  /* background-color: red; */
  display: flex;
  font-size: 25px;
  font-weight: 500;
  justify-content: center;
  width: 100%;
  flex-direction: row;
  padding: 5px;
  margin: 10px;
  
}

</style>
