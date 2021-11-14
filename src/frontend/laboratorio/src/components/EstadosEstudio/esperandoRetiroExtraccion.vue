<template>
  <b-container>
    <div>
      <ValidationObserver ref="detailsExtraccion">
        <b-card header="Ingrese quien realizo el retiro de extraccion">
          <b-row>
            <b-col lg="7" md="7" sm="10">
              <b-form-group
                id="retiro-label"
                label="Nombre de la persona que retiro la muestra:"
                label-for="retiro"
              >
                <ValidationProvider
                  :name="'retiro extraccion '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="Ingrese el nombre y apellido de la persona que retiro la muestra"
                    v-model="retiro"
                    :state="errors[0] ? false : valid ? true : null"
                  ></b-form-input>
                  <b-form-invalid-feedback
                    v-for="error in errors"
                    :key="error.key"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </ValidationProvider>
              </b-form-group>
            </b-col>
          </b-row>
          <b-row class="pb-2">
            <b-col class="text-center pt-3">
              <b-button variant="success" @click="guardarDatos()"
                >Guardar
              </b-button>
            </b-col>
          </b-row>
        </b-card>
      </ValidationObserver>
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
      retiro: null,
    };
  },

  methods: {
    async guardarDatos() {
      let result = await this.$refs.detailsExtraccion.validate();
      if (result) {
        let retiroExtraccion = {
          estudio: this.idEstudio,
          nombreRetiro: this.retiro,
        };
        console.log(retiroExtraccion);
      }
    },
  },
  computed: {},

  mounted() {},
};
</script>

