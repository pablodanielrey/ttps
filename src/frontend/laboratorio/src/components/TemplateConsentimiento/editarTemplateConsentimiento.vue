<template>
  <b-container>
    <div>
      <b-card header="Template Consentimiento informado">
        <div>
          <div>
            <b-button variant="success" @click="verTemplate()"
              >Descargar actual
            </b-button>
          </div>
          <div>
            <ValidationObserver ref="detailsTemplate">
              <b-form-group
                id="pdf-label"
                label="Cargar nuevo:"
                label-for="pdf"
              >
                <ValidationProvider :name="'pdf '" v-slot="{ errors }">
                  <b-form-file
                    v-model="file1"
                    :state="Boolean(file1)"
                    @change="obtenerPDF($event, file1)"
                    accept="application/pdf"
                    placeholder="Seleccione un nuevo Template para Consentimiento informado..."
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
            <b-button variant="success" @click="guardarTemplate()"
              >Guardar
            </b-button>
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