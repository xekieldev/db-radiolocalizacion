<script setup>
import { RouterView } from 'vue-router'
import BarMenu from './components/Menu.vue'


</script>

<template>
  <div class="wrapper">
    <bar-menu />
    <RouterView />
  </div>
</template>


<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  width: 900px;
  margin: 0 auto;
}

header {
  display: flex;
  flex-direction: row;
  background: linear-gradient(to right, rgba(202, 202, 202, 0), #cacaca, rgba(202, 202, 202, 0));
  width: 100%;
}

nav {
  width: 100%;
  font-size: 15px;
  text-align: left;
  margin-top: 2rem;
  margin-left: 50px;
}

nav a.router-link-exact-active {
  color: #426aaf;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
  color: black;
  text-decoration: none;
  font-weight: 700;
}

nav a:hover {
  color: rgb(255, 136, 0);
}
nav a:first-of-type {
  border: 0;
}

</style>
