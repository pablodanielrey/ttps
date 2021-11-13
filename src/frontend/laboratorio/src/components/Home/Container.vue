<template>  
    <div class="wrapper">
      <Menu  />
      <router-view  /> 
  </div>
</template>

<script>

import Menu from "@/components/Home/menu.vue";

export default {
  name: "Container",
  components: {
 Menu
  },
  data() {
    return {  
    
    };
  },
  props: {},
  methods: {  
  },

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
  line-height: 2.5;
}
.wrapper {
  min-height: calc(100vh - 60px);
}

</style>
