<template>
  <div class="container" id="app">
    <navbar></navbar>
    <text-areas-wrapper></text-areas-wrapper>
  </div>
</template>

<script>
import NavBar from "./components/NavBar";
import TextAreasWrapper from "./components/TextAreasWrapper";

export default {
  name: "app",
  components: {
    navbar: NavBar,
    TextAreasWrapper: TextAreasWrapper
  }
};
</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Eczar);
@import url(https://fonts.googleapis.com/css?family=Work+Sans);

body {
  font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  font-size: 140%;
  background: #ffffff;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Eczar", sans-serif;
}
</style>



