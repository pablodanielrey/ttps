<template>
  <b-container>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <p class="h3 text-center">
          <strong  v-if="!editar">Crear una nueva Obra Social</strong>
            <strong  v-if="editar">Editar Obra Social</strong>
        </p>
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
          <b-col lg="5" md="5">
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

          <b-col lg="5" md="5">
            <b-form-group
              id="telefono-label"
              label="Telefono:"
              label-for="Telefono"
            >
              <ValidationProvider
                :name="'telefono'"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  type="tel"
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
          <b-col lg="5" md="5">
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
      </b-card>
    </ValidationObserver>

    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <b-button variant="success" @click="crearObraSocial()" v-if="!editar"
          >Crear Obra Social
        </b-button>
         <b-button variant="success" @click="editarObraSocial()" v-if="editar"
          >Editar Obra Social
        </b-button>
      </b-col>
    </b-row>
  </b-container>
</template>


<script>
import ObrasSocialesService from "@/services/ObrasSocialesService";

export default {
  components: {},

  props: {
     obraSocial: {
      type: Object,
      default: function () {
        return {
          nombre: "",
          email:null,
          telefono: null,

        };
      },
    },
    editar: {
      type: Boolean,
      return: false,
    },
  },
  data() {
    return {
      alerts: [],
      
    };
  },
  created (){
    console.log(this.obraSocial)
  },
  methods: {
    async crearObraSocial() {
      try {
        let result = await this.$refs.detalleObraSocial.validate();
        if (result) {
          console.log(this.obraSocial);
          let r = await ObrasSocialesService.crearObraSocial(this.obraSocial);
          console.log(r);
        }
        this.$root.$bvToast.toast("Se creo con exito la obra social", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "success",
        });
        this.$router.push({
              name: "listaObrasSociales",
            });
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast("No se pudo crear la obra social", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "danger",
        });
      }
    },
    async editarObraSocial(){
      
       try {
        let result = await this.$refs.detalleObraSocial.validate();
        if (result) {
          console.log(this.obraSocial);
          let r = await ObrasSocialesService.editarObraSocial(this.obraSocial);
          console.log(r);
        }
        this.$root.$bvToast.toast("Se edito con exito la obra social", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "success",
        });
        this.$router.push({
              name: "listaObrasSociales",
            });
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast("NO se pudo editar la obra social", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "danger",
        });
      }
    }
  },
  computed: {},
};
</script>

