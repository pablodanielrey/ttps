<template>
  <b-container>
       <b-alert show>El estudio fue entregado al medico derivante</b-alert>
         <div>
            <img
              src="@/assets/resultadovirtual.png"
              class="rounded"
              alt="..."
              id="imgLaboratorio"
              style="width:60%"
            /></div>
       
  </b-container>
</template>

<script>
export default {
  components: {},
  props: {
    estudio: {
      type: Object,
    },
  },
  data() {
    return {
      
    };
  },
  created() {},
  methods: {
  }
}
</script>

<style>

</style>