<template>
  <b-container>
    <div>
   
      <ValidationObserver ref="detailsConsentimiento">
        <b-col lg="5" md="5">
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
                placeholder="Ingrese el consentimiento..."
                drop-placeholder="Drop file here..."
              ></b-form-file>
              <b-form-invalid-feedback v-for="error in errors" :key="error.key">
                {{ error }}
              </b-form-invalid-feedback>
            </ValidationProvider>
          </b-form-group>
        </b-col>
      </ValidationObserver>
      <b-col lg="5" md="5">
        <b-button
          title="Siguiente estado"
          variant="outline-success"
          @click="siguienteEstado()"
        >
          <b-icon icon="arrow-repeat" aria-hidden="true"></b-icon
        ></b-button>
      </b-col>
     
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

