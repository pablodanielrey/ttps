<template>
  <b-container>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <p class="h3 text-center">
          <strong v-if="!editar"> Crear un medico infomante</strong>
          <strong v-if="editar"> Editar un medico informante</strong>
        </p>
      </b-col>
    </b-row>
      <b-card header="Datos del medico informante">
    <ValidationObserver ref="datosInformante">
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

         <b-alert v-if="this.showError" show variant="danger">{{
          this.error
        }}</b-alert>
        <b-row>
          <b-col lg="5" md="5">
            <b-form-group id="Nombre-label" label="Nombre :" label-for="Nombre">
              <ValidationProvider
                :name="'Nombre '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  placeholder="Nombre"
                  v-model="medicoInformante.nombre"
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
              id="apellido-label"
              label="apellido :"
              label-for="apellido"
            >
              <ValidationProvider
                :name="'apellido '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  placeholder="apellido"
                  v-model="medicoInformante.apellido"
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
              <b-col lg="5" md="5">
            <b-form-group
              id="email-label"
              label="email :"
              label-for="email"
            >
              <ValidationProvider
                :name="'email '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  placeholder="email"
                  v-model="medicoInformante.email"
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
              id="matricula-label"
              label="matricula :"
              label-for="matricula"
            >
              <ValidationProvider
                :name="'matricula '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  placeholder="matricula"
                  v-model="medicoInformante.matricula"
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
          <b-col lg="5" md="5">
            <b-form-group
              id="usuario-label"
              label="usuario:"
              label-for="usuario"
            >
              <ValidationProvider
                :name="'usuario'"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  placeholder="usuario"
                  v-model="medicoInformante.usuario.username"
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
              id="contraseña-label"
              label="contraseña:"
              label-for="contraseña"
            >
              <ValidationProvider
                :name="'contraseña '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  type="password"
                  placeholder="contraseña"
                  v-model="medicoInformante.usuario.password"
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
  
    </ValidationObserver>

    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <b-button variant="success" @click="crear()" v-if="!editar"    style="width: 250px">Crear </b-button>
         <b-button variant="success" @click="editarInformante()" v-if="editar"    style="width: 250px"
          >Editar 
        </b-button>
      </b-col>
    </b-row>
        </b-card>
  </b-container>
</template>


<script>
import PacientesService from "@/services/PacientesService";

export default {
  components: {},

  props: {
    medicoInformante: {
      type: Object,
      default: function () {
        return {
          nombre: "",
          apellido: null,
          email:null,
          matricula:null,
          usuario: {
            username: null,
            password: null
          }
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
        showError: false,
      error: null,
    };
  },
  methods: {
    async crear() {
      try {
        let result = await this.$refs.datosInformante.validate();
        if (result) {
          console.log(this.medicoInformante);
          let r = await PacientesService.crearMedicoInformante(this.medicoInformante);
          console.log(r);

          this.$root.$bvToast.toast("Se creo con exito el medico informante", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
          this.$router.push({
            name: "listaMedicoInformante",
          });
        }
      } catch (error) {
        this.showError = true;
        this.error = "";
        this.error +=
          error.response.data.email != null
            ? "Email: " + error.response.data.email
            : "";
        this.error +=
          error.response.data.usuario != null
            ? "Usuario " + error.response.data.usuario
            : "";
      
      }
    },
    async editarInformante(){
    try {
        let result = await this.$refs.datosInformante.validate();
        if (result) {
          console.log(this.medicoInformante);
          let r = await PacientesService.editarMedicoInformante(this.medicoInformante);
          console.log(r);

          this.$root.$bvToast.toast("Se edito con exito el medico informante", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
          this.$router.push({
            name: "listaMedicoInformante",
          });
        }
      } catch (error) {
            this.showError = true;
        this.error = "";
        this.error +=
          error.response.data.email != null
            ? "Email: " + error.response.data.email
            : "";
        this.error +=
          error.response.data.usuario != null
            ? "Usuario " + error.response.data.usuario
            : "";
      
      }

    }
  },
  computed: {},
};
</script>

