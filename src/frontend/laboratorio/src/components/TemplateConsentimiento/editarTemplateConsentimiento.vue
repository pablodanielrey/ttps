<template>
  <b-container>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <p class="h3 text-center">
          <strong>Template Consentimiento Informado</strong>
        </p>
      </b-col>
    </b-row>
      <b-col>
        <p>Archivo:</p>
        <a
          title="Descargar Template Consentimiento Informado"
          variant="outline-success"
          download="consentimiento.pdf"
        >
          <b-icon icon="download" variant="info"> </b-icon
        ></a>
      </b-col>
    

    
  </b-container>
</template>


<script>
//import TemplateConsentimientoService from "@/services/TemplateConsentimiento.js";

export default {
  components: {},
  props: {
    templateConsentimiento: {
      type: Object,
      default: null,
    }
  },
  created() {},
  data() {
    return {
      archivo: null,
    };
  },

  methods: {
    obtenerPDF(event) {
      const file = event.target.files[0];
      this.createBase64(file);
    },
    createBase64(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.archivo = e.target.result;
      };
      reader.readAsDataURL(file);
    },  
  },
  computed: {},

  mounted() {},
};
</script>

<style>
</style>