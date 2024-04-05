<template>
  <router-view />
</template>

<style lang="scss">
html,
body,
#app {
  background-image: url("./assets/background.png");
  font-family: Cublic, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-attachment: fixed;
  background-position: center center;
  background-size: cover;
  height: 100%;
  width: 100%;
  padding: 0rem;
  margin: 0rem;
  overflow: hidden;

  @font-face {
    font-family: 'Cublic';
    src: url('./assets/cublic.woff');
  }
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}</style>
