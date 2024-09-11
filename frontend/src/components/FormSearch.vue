<script setup>
import FormRow from './FormRow.vue'
import MyButton from '../components/MyButton.vue';
import { ref } from 'vue'

const emits = defineEmits(['onSubmit'])
const searchText = ref('')

function submitHandler() {
  emits('onSubmit', searchText.value)
}

const props = defineProps({
  searchText: String,
  placeholder: String,
})
</script>

<template>
  <form-kit
  type="form"
  :actions="false"
  @submit="submitHandler"
  >
    <div class="form-search-container">
      <form-row class="search-bar">
        <form-kit
          v-model="searchText"
          outer-class="field-text-search"
          type="search"
          name="searchInput"
          :placeholder="placeholder"
          style="height: 35px;"
        />
        <my-button
          class="senary right search-btn"
          label="Buscar"
          @on-tap="submitHandler"
      />
      </form-row>
    </div>
  </form-kit>
</template>

<style scoped>
.form-search-container {
  display: flex;
  flex-direction: row;
  gap: 10px; 
  /* margin: 0 10px; */
  
}
.field-text-search {
  display: flex;
  /* https://stackoverflow.com/questions/30684759/flexbox-how-to-get-divs-to-fill-up-100-of-the-container-width-without-wrapping */
  flex: 0 0 80%;
  margin: 0;
  margin-left: 5px;
  background-color: white;
}
.search-btn {
  background-color: white;
  height: 100%;
}



</style>
