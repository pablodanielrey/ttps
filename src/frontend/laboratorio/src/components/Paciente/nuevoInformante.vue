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
      <b-card header="Datos del medico informante">
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
                :name="'usuario '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  placeholder="usuario"
                  v-model="medicoInformante.usuario"
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
                  v-model="medicoInformante.clave"
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
        <b-button variant="success" @click="crear()" v-if="!editar">Crear </b-button>
         <b-button variant="success" @click="editarConfigurador()" v-if="editar"
          >Editar 
        </b-button>
      </b-col>
    </b-row>
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
          usuario: null,
          clave: null,
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
  methods: {
    async crear() {
      try {
        let result = await this.$refs.datosInformante.validate();
        if (result) {
          console.log(this.medicoInformante);
          let r = await PacientesService.crearMedicoInformante(this.medicoInformante);
          console.log(r);

          this.$root.$bvToast.toast("Se creo con exito el meidco informante", {
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
        console.log(error);
        this.$root.$bvToast.toast(
          "NO se pudo crear el medico informante, el usuario ya existe",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }
    },
    async editarConfigurador(){
          try {
        let result = await this.$refs.datosInformante.validate();
        if (result) {
          console.log(this.configurador);
          let r = await PacientesService.editarConfigurador(this.configurador);
          console.log(r);

          this.$root.$bvToast.toast("Se edito con exito el configurador", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
          this.$router.push({
            name: "listaConfiguradores",
          });
        }
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast(
          "NO se pudo editar el configurador",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }

    }
  },
  computed: {},
};
</script>

