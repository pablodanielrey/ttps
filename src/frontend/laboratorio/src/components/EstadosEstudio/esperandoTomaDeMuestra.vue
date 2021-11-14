<template>
  <b-container>
    <div>
      <ValidationObserver ref="detailMuestra">
        <b-card header="Ingrese los datos de la toma de muestra">
          <div class="counter">
            Quedan 20 dias para cargar los datos de la toma de muestra
          </div>
          <br />
          <b-row>
            <b-col lg="3" md="3" sm="10">
              <b-form-group
                id="mililitros-label"
                label="Cantidad de mililitros:"
                label-for="mililitros"
              >
                <ValidationProvider
                  :name="'mililitros '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="Ingrese los mililitros"
                    v-model="mililitros"
                    type="range"
                    min="5"
                    max="12.5"
                    step="0.1"
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
              <div class="mt-2">Cantidad: {{ mililitros }}</div>
            </b-col>
            <b-col lg="3" md="3" sm="10">
              <b-form-group
                id="freezer-label"
                label="Numero de freezer:"
                label-for="freezer"
              >
                <ValidationProvider
                  :name="'freezer '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    type="number"
                    min="1"
                    placeholder="Ingrese el freezer"
                    v-model="freezer"
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
      freezer: 1,
      mililitros: 5,
    };
  },

  methods: {
    guardarDatos() {
        let datosMuestra={
          idEstudio:this.idEstudio,
          freezer:this.freezer,
          mililitros:this.mililitros
        }
        console.log(datosMuestra)
    },
  },
  computed: {},

  mounted() {},
};
</script>

