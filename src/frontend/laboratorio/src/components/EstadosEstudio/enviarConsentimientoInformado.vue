<template>
  <b-container>
    <div>
      <b-card
        header="Descargar Template de consentimiento informado en formato pdf"
      >
        <div>
           <b-button variant="danger" v-if=" hasRol('Empleados')" @click="volverComprobanteInvalido()"
            >Comprobante invalido
          </b-button>
          <b-button
            id="btnConsentimiento"
            variant="outline-primary"
            @click="verTemplate()"
            title="Descargar consentimiento"
          >
            <b-icon icon="cloud-download" variant="outline-primary"> </b-icon>
          </b-button>

          <b-button variant="success" v-if=" hasRol('Empleados')" @click="siguienteEstado()"
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
import { mapGetters} from "vuex";
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
    
          await TemplateConsentimientoService.obtenerTemplateConsentimiento(this.estudio.id);
        
      } catch (error) {
        console.log(error);
      }
    },
    async volverComprobanteInvalido(){
      try {
         let datos = {
          estudio_id: this.estudio.id,
          comprobante_invalido: true,
          resourcetype: this.estudio.ultimo_estado.resourcetype,
        };
      await EstudiosService.actualizarUltimoEstado(
          datos,
          this.estudio.ultimo_estado.id
        );
        this.$root.$bvToast.toast("Se cancelo el comprobante de pago", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
        this.$router.push({
          name: "listaEstudios",
        });

        
      } catch (error) {
          this.$root.$bvToast.toast(
          "ocurrio un error mientras volvia atras el comprobante",
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
        this.$root.$bvToast.toast(
          "ocurrio un error mientras continuaba con el siguiente estado.  "+error.response.data.detail,
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }
    },
    tienePermisos(){      
      this.permisos = window.localStorage.getItem("permisos");
      return this.permisos
    
    }
  },
  computed: {
    ...mapGetters(["hasRol"]),

  },
  mounted() {},
};
</script>
<style scoped>
#btnConsentimiento {
  margin: 30px;
}
</style>
