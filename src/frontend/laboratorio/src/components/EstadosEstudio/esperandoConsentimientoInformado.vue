<template>
  <b-container>
    <div>
      <b-card header="Consentimiento informado">
        <b-row>
          <b-col lg="5" md="5" class="text-center pt-3">
            <ValidationObserver ref="detailsConsentimiento">
              <b-form-group
                id="pdf-label"
                label="Ingrese el consentimiento firmado:"
                label-for="pdf"
              >
                <ValidationProvider :name="'pdf '" v-slot="{ errors }">
                  <b-form-file
                    v-model="file1"
                    :state="Boolean(file1)"
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
        <b-row>
          <b-col class="text-center pt-3">
            <b-button
              title="Siguiente estado"
              variant="outline-success"
              @click="siguienteEstado()"
            >
              <b-icon icon="arrow-repeat" aria-hidden="true"></b-icon
            ></b-button>
          </b-col>
        </b-row>
      </b-card>
    </div>
  </b-container>
</template>


<script>
export default {
  components: {},

  props: {},
  created() {},
  data() {
    return {
      file1: [],
    };
  },

  methods: {
    obtenerPDF(event, file) {
      console.log(event, file);
    },
  },
  computed: {},

  mounted() {},
};
</script>

