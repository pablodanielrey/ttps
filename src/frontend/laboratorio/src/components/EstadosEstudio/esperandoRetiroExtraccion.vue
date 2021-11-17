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
            <b-col lg="3" md="2">
              <b-form-group
                id="fecha-label"
                label="Fecha retiro :"
                label-for="Fecha retiro"
              >
                <ValidationProvider
                  :name="'Fecha-retiro '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    locale="es-AR"
                    type="date"
                    v-model="fecha_retiro"
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
import EstudiosService from "@/services/EstudiosService.js";

export default {
  components: {},

  props: {
    estudio: {
      type: Object,
    },
  },
  created() {
  
  },
  data() {
    return {
      retiro: null,
      fecha_retiro: new Date().format("YYYY-MM-DD"),
    };
  },

  methods: {
    async guardarDatos() {
      try {
        let result = await this.$refs.detailsExtraccion.validate();
        if (result) {
          let retiroExtraccion = {

            estudio_id: this.estudio.id,
            extracionista: this.retiro,
            fecha_retiro: new Date(this.fecha_retiro),
          };
          console.log(retiroExtraccion);
          let response = await EstudiosService.actualizarUltimoEstado(
            retiroExtraccion
          );
          this.$root.$bvToast.toast(
            "Se ingresaron los datos del retiro de la extraccion",
            {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "success",
            }
          );
          this.$router.push({
            name: "listaEstudios",
          });

          console.log(response);
        }
      } catch (error) {
        this.$root.$bvToast.toast(
          "ocurrio un error mientras ingresaba los datos del retiro de extraccion",
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

