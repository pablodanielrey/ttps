<template>
  <b-container>
    <div>
      <ValidationObserver ref="detailsExtraccion">
        <b-card header="Retiro de extraccion">           
          <b-row>           
            <b-col lg="7" md="7" sm="10">
              <b-form-group
                id="retiro-label"
                label="Nombre del retirante de la muestra:"
                label-for="retiro"
              >
                <ValidationProvider
                  :name="'retiro '"
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
          <b-row>
            <b-col class="text-center pt-3">
              <b-button
                title="Siguiente estado"
                variant="outline-success"
                @click="siguienteEstado()"
              >
                Enviar</b-button>
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

  props: {},
  created() {},
  data() {
    return {
      retiro: null,
     
    };
  },

  methods: {},
  computed: {},

  mounted() {},
};
</script>

