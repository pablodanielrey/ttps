<template>
  <b-container>
    <div>
      <b-card
        header="Descargar Template de consentimiento informado en formato pdf"
      >
        <div>
          <b-button
            id="btnConsentimiento"
            variant="outline-primary"
            @click="verTemplate()"
            title="Descargar consentimiento"
          >
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
          resourcetype: this.estudio.ultimo_estado.resourcetype,
          fecha_enviado: new Date(),
          resourcetype: this.estudio.ultimo_estado.resourcetype,
        };
        let response = await EstudiosService.actualizarUltimoEstado(
          datosConsentimiento,
          this.estudio.ultimo_estado.id
        );
          this.$root.$bvToast.toast("Se descargo el consentimiento y el estudio continua al proximo estado", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
        console.log(response);
        this.$router.push({
          name: "listaEstudios",
        });
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast(
          "ocurrio un error mientras Continuaba al siguiente estado ",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }
    },
  },
  computed: {},

  mounted() {},
};
</script>
<style scoped>
#btnConsentimiento {
  margin: 30px;
}
</style>
