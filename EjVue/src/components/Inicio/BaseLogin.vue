<template>
  <div class="contenedor1">
    <div class="wrapper1">
      <b-row class="h-100 justify-content-center align-items-center">
        <b-col sm="10" md="8" xl="4" class="base-box m-2">
          <router-view class="content1" />
        </b-col>
      </b-row>
    </div>
  
  </div>
</template>

<script>


export default {
  name: "BaseLogin",
  components: {},
  computed: {

  },
  methods: {
 

   
  },
  mounted() {
 
  },
};
</script>

<style scoped>
</style>