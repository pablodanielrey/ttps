<template>
  <b-container>
    <div>
      <b-card header="Consentimiento informado firmado por el paciente">
        <b-row>
          <b-col lg="5" md="5" class="text-center pt-3">
            <ValidationObserver ref="detailsConsentimiento">
              <b-form-group
                id="pdf-label"
                label="Ingrese el consentimiento firmado:"
                label-for="pdf"
              >
                <ValidationProvider    :rules="'required'" :name="'consentimiento informado '" v-slot="{ errors,valid }">
                  <b-form-file
                    v-model="file1"
                    :state="errors[0] ? false : valid ? true : null"
                    @change="obtenerPDF($event, file1)"
                    accept="application/pdf"
                    placeholder="Ingrese el consentimiento firmado..."
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
export default {
  components: {},

  props: {
    idEstudio: {
      type: String,
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
    countUp() {
      this.counter -= 1;
    },
    async guardarConsentimiento() {
      let result = await this.$refs.detailsConsentimiento.validate();
      if (result){
        let datosConsentimiento = {
        estudio: this.idEstudio,
        consentimiento: this.consentimiento,
      };
      console.log(datosConsentimiento);
      }
   
    },
  },
  computed: {},

  mounted() {},
};
</script>

