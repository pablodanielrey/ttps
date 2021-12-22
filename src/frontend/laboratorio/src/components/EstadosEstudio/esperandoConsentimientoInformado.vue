<template>
  <b-container>
    <div>
      <b-card header="Consentimiento informado firmado por el paciente">
        <b-row>
          <b-col class="text-center pt-3">
            <ValidationObserver ref="detailsConsentimiento">
              <b-form-group id="pdf-label" label-for="pdf">
                <ValidationProvider
                  :rules="'required'"
                  :name="'consentimiento informado '"
                  v-slot="{ errors, valid }"
                >
                  <b-form-file
                    v-model="file1"
                    :state="errors[0] ? false : valid ? true : null"
                    @change="obtenerPDF($event, file1)"
                    accept="application/pdf"
                    placeholder="Seleccione el consentimiento informado.."
                    browse-text="Buscar"
                  ></b-form-file>
                  <b-form-invalid-feedback
                    v-for="error in errors"
                    :key="error.key"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </ValidationProvider>
              </b-form-group>
            </ValidationObserver>
          </b-col>
        </b-row>
        <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-button variant="success" @click="guardarConsentimiento()"
              >Guardar
            </b-button>
          </b-col>
        </b-row>
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
  created() {},
  data() {
    return {
      file1: [],
      consentimiento: null,
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
        this.consentimiento = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async guardarConsentimiento() {
      try {
        let result = await this.$refs.detailsConsentimiento.validate();
        if (result) {
          let datosConsentimiento = {
            estudio_id: this.estudio.id,
            resourcetype: this.estudio.ultimo_estado.resourcetype,

            consentimiento: {
              contenido: this.consentimiento,
            },
          };
          let response = await EstudiosService.actualizarUltimoEstado(
            datosConsentimiento,
            this.estudio.ultimo_estado.id
          );
          console.log(response);
          this.$root.$bvToast.toast("Se ingreso el consentimiento firmado", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
          this.$router.push({
            name: "listaEstudios",
          });
        }
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast(
          "Ocurrio un error mientras ingresaba el consentimiento firmado,verifique el modo de operacion",
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

