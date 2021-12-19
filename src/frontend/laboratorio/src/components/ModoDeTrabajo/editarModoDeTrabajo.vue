<template>
  <b-container>
    <div>
      <b-card header="Modo de Trabajo">
        <div>
          <div>
            <input type="radio" id="uno" value="Uno" v-model="picked">
                <label for="uno">Uno</label>
            <input type="radio" id="Dos" value="Dos" v-model="picked">
                <label for="Dos">Dos</label>
            <br>
            <span>Eligió: {{ picked }}</span>
          </div>
        </div>
      </b-card>
    </div>
  </b-container>
</template>


<script>
import TemplateConsentimientoService from "@/services/TemplateConsentimiento.js";

export default {
  mounted() {},

  components: {},
  props: {
    templateConsentimiento: {
      type: Object,
    },
  },
  created() {},
  data() {
    return {
      file1: [],
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
    async guardarTemplate() {
      let result = await this.$refs.detailsTemplate.validate();
      if (result) {
        try {
          let datosTemplate = this.archivo;
          console.log(datosTemplate);
          await TemplateConsentimientoService.editarTemplateConsentimiento(
            datosTemplate
          );

          this.$root.$bvToast.toast("Se agrego el template", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
        } catch (err) {
          console.log(err);
          this.$root.$bvToast.toast(
            "ocurrio un error mientras agregaba el archivo",
            {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "danger",
            }
          );
        }
      }
    },
    async verTemplate() {
      try {
        let response =
          await TemplateConsentimientoService.obtenerTemplateConsentimiento();
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {},
};
</script>

<style>
</style>