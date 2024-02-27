<script setup>
import { ref } from 'vue';

// const primary = ref(true)


const props = defineProps({
  label: String,
  type: String,
  align: String,
})

const emit = defineEmits([
  'onTap',
])

function handleClick() {
  emit('onTap')
}

</script>

<template>
  <div class="my-button-container" @click="handleClick" :class="{ primary: type === 'primary', secondary: type === 'secondary', tertiary: type === 'tertiary', quaternary: type === 'quaternary'}, { center: align === 'center', right: align === 'right' }">
    {{ label }}
  </div>
</template>

<style scoped>
.my-button-container{
  display: flex;
  justify-content: center;
  padding: 5px 10px;
  border-radius: 20px;
  width: fit-content;
  cursor: pointer;
  text-decoration: none;
}

.primary {
  border: 1px solid #007BFF;
  font-weight: 500;  
  color: #007BFF;  
}

.primary:hover {
  background-color: #007BFF;
  color: white;
}
.secondary {
  border: 1px solid #28A745;
  font-weight: 500;  
  color: #28A745
}
.secondary:hover {
  background-color: #28A745;
  color: white;
}
.tertiary {
  border: 1px solid #DC3545;
  font-weight: 500;  
  color: #DC3545;
}
.tertiary:hover {
  background-color: #DC3545;
  color: white;
}

.quaternary {
  border: 1px solid #426aaf;
  font-weight: 500;  
  color: #426aaf; 
  height: 60px;
  width: 350px;
  /* line-height: 30px; */
  text-align: center;
  align-items: center;
  /* padding-top: 18px; */
}
.quaternary:hover {
  background-color: #426aaf;
  color: white;
}

.center {
  margin: 0 auto;
}

.right {
  align-self: flex-end;
}

</style>
