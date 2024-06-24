<script setup>
defineProps({
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
  <div
    class="my-button-container"
    :class="{ primary: type === 'primary', secondary: type === 'secondary', tertiary: type === 'tertiary', quaternary: type === 'quaternary', quinary: type === 'quinary', senary: type === 'senary', center: align === 'center', right: align === 'right' }"
    @click="handleClick"
  >
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
  text-align: center;
  align-items: center;
}
.quaternary:hover {
  background-color: #426aaf;
  color: white;
}
.quinary {
  border: 1px solid #b522ba;
  font-weight: 500;  
  color: #b522ba;
}
.quinary:hover {
  background-color: #b522ba;
  color: white;
}
.senary {
  border: 1px solid #fa8900;
  font-weight: 500;  
  color: #fa8900;
}
.senary:hover {
  background-color: #fa8900;
  color: white;
}
.center {
  margin: 0 auto;
}

.right {
  align-self: flex-end;
}

</style>
