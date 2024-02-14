<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="wrapper">
    <header>
      <img
        alt="ENACOM logo"
        class="logo"
        src="../../img/Logo.png"
        width="100"
        height="100"
      >
      <nav>
        <RouterLink to="/">
          Home
        </RouterLink>
        <!-- <RouterLink to="/form">
          Form
        </RouterLink>
        <RouterLink to="/map">
          Map
        </RouterLink>
        <RouterLink to="/rloc">
          Rloc
        </RouterLink>
        <RouterLink to="/loc">
          Loc
        </RouterLink> -->
        <RouterLink to="/list">
          Listado
        </RouterLink>
        <!-- <RouterLink to="/tech">
          Tech
        </RouterLink> -->
        <RouterLink to="/list_technicians">
          Técnicos
        </RouterLink>
        <RouterLink to="/about">
          About
        </RouterLink>
      </nav>
    </header>

    <RouterView />
  </div>
</template>


<style scoped>
.wrapper {
  /* display: flex;
  flex-direction: column; */
  width: 900px;
  margin: 0 auto;

}

header {
  display: flex;
  flex-direction: row;

}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 15px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}
</style>
