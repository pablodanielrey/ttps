<template>
  <b-container>
    <div>
            <b-card header="Descargar resultado en formato pdf de estudio para entregarlo a medico derivante">
      <b-button
        title="Bajar consentimiento informado"
        variant="outline-success"
        @click="bajarConsentimiento()"
      >
        <b-icon icon="download" aria-hidden="true"></b-icon
      ></b-button>
      <br>
            </b-card>
    </div>
  </b-container>
</template>


<script>
export default {
  components: {},

  props: {},
  created() {
 
  },
  data() {
    return {
     
    };
  },

  methods: {
    bajarConsentimiento() {},
    
  },
  computed: {},

  mounted() {},
};
</script>

