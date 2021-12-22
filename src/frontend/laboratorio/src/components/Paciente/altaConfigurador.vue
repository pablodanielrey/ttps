<template>
  <b-container>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <p class="h3 text-center">
          <strong v-if="!editar"> Crear un configurador</strong>
            <strong v-if="editar"> Editar configurador</strong>
        </p>
      </b-col>
    </b-row>

    <ValidationObserver ref="datosConfigurador">
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
      <b-card header="Datos del configurador">
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
                  v-model="configurador.nombre"
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
                  v-model="configurador.apellido"
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
                  v-model="configurador.usuario.username"
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
                  v-model="configurador.usuario.password"
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
                  v-model="configurador.email"
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
    configurador: {
      type: Object,
      default: function () {
        return {
          nombre: "",
          apellido: null,
          usuario: {
            username: null,
            password: null
          },
          email: null
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
        let result = await this.$refs.datosConfigurador.validate();
        if (result) {
     
          await PacientesService.crearConfigurador(this.configurador);
    

          this.$root.$bvToast.toast("Se creo con exito el configurador", {
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
          "NO se pudo crear el configurador, el usuario ya existe",
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
        let result = await this.$refs.datosConfigurador.validate();
        if (result) {
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
          "No se pudo editar el configurador",
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

