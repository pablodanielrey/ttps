<template>
  <b-container>
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
        <b-col lg="5" md="5" sm="10">
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
              <b-form-invalid-feedback v-for="error in errors" :key="error.key">
                {{ error }}
              </b-form-invalid-feedback>
            </ValidationProvider>
          </b-form-group>
        </b-col>

        <b-col lg="5" md="5" sm="10">
          <b-form-group
            id="medico-label"
            label="Medico Informante:"
            label-for="Medico Informante"
          >
            <ValidationProvider
              :name="'Medico '"
              :rules="'required'"
              v-slot="{ errors, valid }"
            >
              <b-form-input
                placeholder="medico Informante"
                v-model="resultado.medico_informante"
                :state="errors[0] ? false : valid ? true : null"
              ></b-form-input>
              <b-form-invalid-feedback v-for="error in errors" :key="error.key">
                {{ error }}
              </b-form-invalid-feedback>
            </ValidationProvider>
          </b-form-group>
        </b-col>
      </b-row>
      <b-row>
        <b-col lg="3" md="2">
          <b-form-group
            id="nacimiento-label"
            label="Fecha Alta :"
            label-for="Fecha Informe"
          >
            <ValidationProvider
              :name="'Fecha-alta '"
              :rules="'required'"
              v-slot="{ errors, valid }"
            >
              <b-form-input
                locale="es-AR"
                type="date"
                v-model="resultado.fecha_informe"
                :state="errors[0] ? false : valid ? true : null"
              ></b-form-input>
              <b-form-invalid-feedback v-for="error in errors" :key="error.key">
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
              id="historiaclinica-label"
              label-for="Informe del resultado"
            >
              <ValidationProvider
                :name="'historiaclinica '"
                v-slot="{ errors, valid }"
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
  },
  data() {
    return {
      retiro: null,
      alerts: [],
      resultado: {
        resultado: null,
        medico_informante: null,
        fecha_informe: new Date().format("YYYY-MM-DD"),
        informe: null,
      },
    };
  },
  methods: {
    async guardarDatos() {
      try {
        let result = await this.$refs.detailsResultado.validate();
        if (result) {
            console.log(this.estudio)
            let datos={
                estudio_id: this.estudio.id,
                fecha_informe: new Date(this.resultado.fecha_informe),
                medico_informante : this.resultado.medico_informante,
                resultado : this.resultado.resultado,
                informe: this.resultado.informe
            }
            console.log(datos)
         let response = await EstudiosService.actualizarUltimoEstado(
            datos
          );
                console.log(response)

        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style>
</style>