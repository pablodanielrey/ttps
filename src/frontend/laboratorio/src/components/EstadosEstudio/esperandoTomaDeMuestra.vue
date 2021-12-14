<template>
  <b-container>
    <div>
      <ValidationObserver ref="detailMuestra">
        <b-card header="Ingrese los datos de toma de muestra">
          <div class="counter" v-if="!pasoDiaTurno()">
            Quedan {{ counter }}  dias para cargar los datos de toma de muestra
          </div>
          <br />
          <b-row>
            <b-col lg="5" md="5" sm="10">
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
            <b-col lg="1"></b-col>
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
import EstudiosService from "@/services/EstudiosService.js";

export default {
  components: {},

  props: {
    estudio: {
      type: Object,
    },
  },
  created() {
    console.log(this.estudio)
     let fecha = new Date(this.estudio.ultimo_estado.turno.inicio);
    this.counter = new Date();
    this.counter= this.difference(fecha.getDate(),this.counter.getDate())
  },
  data() {
    return {
      freezer: 1,
      mililitros: 5,
      counter: 0,
    };
  },

  methods: {
    difference(fechaAlta, diaHoy) {      
      let xtotal=30
    return xtotal - (diaHoy - fechaAlta)     
    },
    pasoDiaTurno(){
      let fechaTurno = new Date(this.estudio.ultimo_estado.turno.inicio);
      console.log(fechaTurno < new Date())
      if (fechaTurno < new Date()){
        return false
      }
      return true
    },
    async guardarDatos() {
      try {
        let result = await this.$refs.detailMuestra.validate();
        if (result) {
          let datosMuestra = {
            estudio_id: this.estudio.id,
            freezer: this.freezer,
            mililitros: this.mililitros,
            fecha_muestra: new Date(),
          };
          console.log(datosMuestra);
          let response = await EstudiosService.actualizarUltimoEstado(
            datosMuestra
          );
          console.log(response);
          this.$root.$bvToast.toast("Se ingresaron los datos de la muestra", {
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
          "no se pudieron guardar los datos de la muestra, intente nuevamente",
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

