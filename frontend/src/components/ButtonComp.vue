<script setup>

</script>

<template>
  <div class="button-container">
    <slot class="content"/>
  </div>
</template>

<style scoped>
.button-container{
  /* background-color: red; */
  display: flex;
  justify-content: center;
  padding: 5px 10px;
  border: 1px solid rgb(0, 123, 255);
  font-weight: 500;  
  border-radius: 20px;
  width: fit-content;
}

.content {
  color: white;
}

</style>
