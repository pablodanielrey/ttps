<template>
  <b-container>
    <div>
      <b-card
        header="Descargar Template de consentimiento informado en formato pdf"
      >
        <div>
          <b-button id="btnConsentimiento" variant="outline-primary" @click="verTemplate()" title="Descargar consentimiento">
            <b-icon icon="cloud-download" variant="outline-primary"> </b-icon>
          </b-button>
      
          <b-button variant="success" @click="siguienteEstado()"
            >Siguiente
          </b-button>
        </div>
      </b-card>
    </div>
  </b-container>
</template>


<script>
import EstudiosService from "@/services/EstudiosService.js";
import TemplateConsentimientoService from "@/services/TemplateConsentimiento.js";

export default {
  components: {},

  props: {
    estudio: {
      type: Object,
    },
  },
  created() {},
  data() {
    return {};
  },

  methods: {
    async verTemplate() {
      try {
        let response =
          await TemplateConsentimientoService.obtenerTemplateConsentimiento();
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async siguienteEstado() {
      try {
        let datosConsentimiento = {
          estudio_id: this.estudio.id,
          fecha_enviado: new Date(),
        };
        let response = await EstudiosService.actualizarUltimoEstado(
          datosConsentimiento
        );
        console.log(response);
        this.$router.push({
          name: "listaEstudios",
        });
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast("ocurrio un error mientras continuaba ", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "danger",
        });
      }
    },
  },
  computed: {},

  mounted() {},
};
</script>
<style scoped>
#btnConsentimiento{
  margin: 30px
}
</style>
