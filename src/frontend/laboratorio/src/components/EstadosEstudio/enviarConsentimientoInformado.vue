<template>
  <b-container>
    <div>
      <b-card
        header="Descargar resultado en formato pdf de estudio para entregarlo a medico derivante"
      >
        <a
          title="Bajar consentimiento informado"
          variant="outline-success"
          @click="bajarConsentimiento()"
          download="consentimiento.pdf"
          :href="this.estudio.estados[0].comprobante"
        >
          <b-icon icon="download" aria-hidden="true"></b-icon
        ></a>
        <br />
      </b-card>
    </div>
  </b-container>
</template>


<script>
import EstudiosService from "@/services/EstudiosService.js";

export default {
  components: {},

  props: {
    estudio: {
      type: Object,
    },
  },
  created() {
    console.log(this.estudio)
  },
  data() {
    return {};
  },

  methods: {
    async bajarConsentimiento() {
      try {
        let datosConsentimiento = {
          estudio_id: this.estudio.id,
          fecha_enviado: new Date(),
        };
        console.log(datosConsentimiento);
        let response = await EstudiosService.actualizarUltimoEstado(
          datosConsentimiento
        );
        console.log(response);
        this.$root.$bvToast.toast("Se descargo el consentimiento ", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "success",
        });
        this.$router.push({
          name: "listaEstudios",
        });
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast(
          "ocurrio un error mientras descargaba el consentimiento",
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

