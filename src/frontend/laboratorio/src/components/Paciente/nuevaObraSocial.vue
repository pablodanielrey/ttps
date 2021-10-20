<template>
  <b-container>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <p class="h3 text-center"><strong>Crear una nueva Obra Social</strong></p>
      </b-col>
    </b-row>

    <ValidationObserver ref="detalleObraSocial">
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
      <b-card header="Datos Obra Social">
        <b-row>
          <b-col lg="3" md="3">
            <b-form-group id="Nombre-label" label="Nombre :" label-for="Nombre">
              <ValidationProvider
                :name="'Nombre '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  placeholder="Nombre de la Obra Social"
                  v-model="obraSocial.nombre"
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
          <b-col lg="2" md="2">
            <b-form-group
              id="telefono-label"
              label="Telefono:"
              label-for="Telefono"
            >
              <ValidationProvider
                :name="'Telefono '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  type="number"
                  placeholder="Telefono"
                  v-model="obraSocial.telefono"
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
          <b-col lg="3" md="3">
            <b-form-group
              id="email-label"
              label="Direccion de correo electronico:"
              label-for="email"
            >
              <ValidationProvider
                :name="'email '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  type="email"
                  placeholder="Direccion de email"
                  v-model="obraSocial.email"
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
      </b-card
      >
    </ValidationObserver>

    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <b-button variant="success" @click="crearObraSocial()"
          >Crear Obra Social
        </b-button>
      </b-col>
    </b-row>
  </b-container>
</template>


<script>

import PacientesService from '@/services/PacientesService'

export default {
  components: {
  },

  props: {},
  data() {
    return {
      alerts: [],
      obraSocial: {}
    };
  },
  methods: {
    async crearObraSocial() {
      let result = await this.$refs.detalleObraSocial.validate();
      console.log(result)
      console.log(this.obraSocial)
      let r = await PacientesService.crearObraSocial(this.obraSocial)
      console.log(r)
    }
  },
  computed: {},
};
</script>

