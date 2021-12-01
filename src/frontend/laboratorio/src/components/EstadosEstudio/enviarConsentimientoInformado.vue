<template>
  <b-container>
    <div>
      <b-card
        header="Descargar consentimiento informado en formato pdf"
      >
        <a
          title="Bajar consentimiento informado"
          variant="outline-success"
          @click="descargarConsentimiento()"
          download="consentimiento.pdf"        
        >
          <b-icon icon="download" aria-hidden="true"></b-icon
        ></a>
        <br/>
             <b-button variant="success" @click="siguienteEstado()"
              >Siguiente
            </b-button>
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
    async descargarConsentimiento(){
      try {        
        let response = await EstudiosService.obtenerConsentimientoInformado(
          this.estudio.id
        );
        console.log(response)
      } catch (error) {
        this.$root.$bvToast.toast(
          "ocurrio un error mientras descargaba el consentimiento, por favor vuelva a intentar",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );

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
        this.$root.$bvToast.toast(
          "ocurrio un error mientras continuaba ",
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

