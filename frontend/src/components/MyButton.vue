<script setup>
const props = defineProps({
  label: String,
})

const emit = defineEmits([
  'onTap',
])

function handleClick() {
  emit('onTap')
}

</script>

<template>
  <div class="my-button-container" @click="handleClick">
    {{ label }}
  </div>
</template>

<style scoped>
.my-button-container{
  display: flex;
  justify-content: center;
  padding: 5px 10px;
  border: 1px solid rgb(0, 123, 255);
  font-weight: 500;  
  border-radius: 20px;
  width: fit-content;
  cursor: pointer;
  color: rgb(0, 123, 255);
  text-decoration: none;
  font-weight: 500; 
}

</style>
