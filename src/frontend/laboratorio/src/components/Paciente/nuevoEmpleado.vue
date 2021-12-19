<template>
  <b-container>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <p class="h3 text-center">
          <strong v-if="!editar"> Crear un empleado</strong>
            <strong v-if="editar"> Editar empleado</strong>
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
      <b-card header="Datos del empleado">
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
                  v-model="empleado.nombre"
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
                  v-model="empleado.apellido"
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
                  v-model="empleado.usuario.username"
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
                  v-model="empleado.usuario.password"
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
         <b-button variant="success" @click="editarempleado()" v-if="editar"
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
    empleado: {
      type: Object,
      default: function () {
        return {
          nombre: "",
          apellido: null,
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
    };
  },
  methods: {
    async crear() {
      try {
        let result = await this.$refs.datosConfigurador.validate();
        if (result) {
          console.log(this.empleado);
          let r = await PacientesService.crearEmpleado(this.empleado);
          console.log(r);

          this.$root.$bvToast.toast("Se creo con exito el empleado", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
          this.$router.push({
            name: "listaEmpleado",
          });
        }
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast(
          "No se pudo crear el empleado, el usuario ya existe",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }
    },
    async editarempleado(){
      try {
        let result = await this.$refs.datosConfigurador.validate();
        if (result) {
          console.log(this.empleado);
          let r = await PacientesService.editarEmpleado(this.empleado);
          console.log(r);

          this.$root.$bvToast.toast("Se edito con exito el empleado", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
          this.$router.push({
            name: "listaEmpleado",
          });
        }
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast(
          "No se pudo editar el empleado",
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

