<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="wrapper">
    <header>
      <img
        alt="Vue logo"
        class="logo"
        src="@/assets/logo.svg"
        width="125"
        height="125"
      >
      <nav>
        <RouterLink to="/">
          Home
        </RouterLink>
        <RouterLink to="/about">
          About
        </RouterLink>
        <RouterLink to="/form">
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
        </RouterLink>
        <RouterLink to="/list">
          List
        </RouterLink>
        <RouterLink to="/tech">
          Tech
        </RouterLink>
      </nav>
    </header>

    <RouterView />
  </div>
</template>


<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;

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
  font-size: 12px;
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
