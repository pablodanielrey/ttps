<template>
  <b-container>

    <div>
      <h4>Resultados del informe</h4>
      <b-col lg="5" md="7" sm="10">
            <a :href="this.urlResultado "  target="_blank"> <b-icon icon="link" variant="info"> </b-icon>Click para Acceder a el informe!</a>
            </b-col>
      <ValidationObserver ref="detailsResultado">
        <b-form-group>
          <b-alert
            v-for="alert in alerts"
            dismissible
            v-bind:key="alert.key"
            show
            :variant="alert.variant"
            >{{ alert.message }}</b-alert
          >
        </b-form-group>
        <b-row>
          <b-col lg="5" md="7" sm="10">
            <b-form-group
              id="Resuttado-label"
              label="Resultado:"
              label-for="Resultado"
            >
              <ValidationProvider
                :name="'Resultado '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  placeholder="Resultado"
                  v-model="resultado.resultado"
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
        <b-card header="Informe del resultado">
          <b-row>
            <b-col>
              <b-form-group
                id="informe-label"
                label-for="Informe del resultado"
              >
                <ValidationProvider
                  :name="'informe '"
                  v-slot="{ errors, valid }"
                  :rules="'required'"
                >
                  <vue-editor
                    :state="errors[0] ? false : valid ? true : null"
                    v-model="resultado.informe"
                  ></vue-editor>
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
        </b-card>
        <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-button variant="success" @click="guardarDatos()"
              >Guardar
            </b-button>
          </b-col>
        </b-row>
      </ValidationObserver>
    </div>
     <b-col class="text-left">
                <router-link to="/listaEstudiosEsperandoInforme"
                  ><b-icon icon="arrow-left-circle"></b-icon
                ></router-link>
              </b-col>
  </b-container>
</template>


<script>
import { VueEditor } from "vue2-editor";
import EstudiosService from "@/services/EstudiosService.js";

export default {
  components: { VueEditor },
  props: {
    estudio: {
      type: Object,
    },
     urlResultado: {
      type: String,
    },
  },
  data() {
    return {
      alerts: [],
      resultado: {
        resultado: null,
        fecha_informe: new Date().format("YYYY-MM-DD"),
        informe: null,
      },
    };
  },

  methods: {
    resultadoUrl(){
      return this.urlResultado
    },
  
    async guardarDatos() {
      try {
        
        let result = await this.$refs.detailsResultado.validate();
        if (result) {
          let datos = {
            estudio_id: this.estudio.id,
            resourcetype: this.estudio.ultimo_estado.resourcetype,
            fecha_informe: new Date(),          
            resultado: this.resultado.resultado,
            informe: this.resultado.informe,
          };
           console.log(datos)
          let response= await EstudiosService.actualizarUltimoEstado(datos,this.estudio.ultimo_estado.id);
          console.log(response)
          this.$root.$bvToast.toast(
            "Se guardo de forma correcta el resultado del informe",
            {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "success",
            }
          );
          this.$router.push({
            name: "listaEstudiosEsperandoInforme",
          });
        }
      } catch (error) {
        console.log(error)
        this.$root.$bvToast.toast(
          "ocurrio un error mientras guardaba los resultados " + error.response,
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
  computed: {
  
  },
  mounted() {
    
  },
};
</script>

<style>
</style>