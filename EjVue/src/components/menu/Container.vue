<template>
    <div>
        <Menu/>
        <router-view  class="content"        
        />
     
      <Footer class="footer" />
    </div>
</template>

<script>
import Footer from "@/components/menu/Footer.vue";
import Menu from "@/components/menu/Menu.vue";

export default {
  name: "Dashboard",
  components: {
    Menu,
    Footer,
  },
  data() {
    return {};
  },
  computed: {},
  created() {},
  methods: {},
  mounted() {},
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500&display=swap");
body {
  font-family: "Roboto" !important;
  background-color: #ebebeb !important;
  overflow-x: hidden !important;
  height: auto;
}
html {
  position: relative;
  height: 100%;
  overflow-x: hidden !important;
}
small,
p,
h4,
span,
h3,
a,
strong {
  font-family: "Roboto";
}

.box-shadow {
  border-radius: 15px 15px 15px 15px;
  box-shadow: 2px 2px 6px 0px rgba(0, 0, 0, 0.75);
  min-height: calc(100vh * 0.6);
}

.box-shadow-min {
  border-radius: 15px 15px 15px 15px;
  box-shadow: 2px 2px 6px 0px rgba(0, 0, 0, 0.75);
}

.wrapper {
  min-height: calc(100vh - 60px);
}

.label-padding-sm {
  display: inline-block;
  width: 80px;
}

.label-padding {
  display: inline-block;
  width: 160px;
}

.label-padding-tab {
  display: inline-block;
  width: 250px;
}

.footer {
  margin-top: 10px;
  height: 50px;
  line-height: 50px;
  color: white;
  background-color: #ececec;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>

