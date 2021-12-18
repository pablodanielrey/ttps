<template>
  <div>
    <div class="wrapper">
      <Menu />
 
      <router-view />
    </div>
    <footer>
      <b-navbar class="navbar"> </b-navbar>
    </footer>
  </div>
</template>

<script>
import Menu from "@/components/Home/menu.vue";

export default {
  name: "Container",
  components: {
    Menu,
  },
  data() {
    return {};
  },
  props: {},
  methods: {},
};
</script>

<style>
html,
body {
  width: auto !important;
  overflow-x: hidden !important;
}
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");
body {
  font-family: "Montserrat", sans-serif !important;
  background-color: white;
}
.wrapper {
  min-height: calc(100vh - 60px);
  background-color: #ededed;
}
footer {
  height: 50 px;
  line-height: 50px;
  margin-top: 11 px;
}
#navbar{
  background-color: #ededed;

}
</style>
