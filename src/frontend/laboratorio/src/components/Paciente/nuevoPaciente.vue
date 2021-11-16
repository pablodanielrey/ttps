<template>
  <b-container>
    <div v-if="loading">
      <b-spinner> </b-spinner>
    </div>
    <div v-else>
      <b-row class="pb-2">
        <b-col class="text-center pt-3">
          <p class="h3 text-center"><strong> Paciente</strong></p>
        </b-col>
      </b-row>

      <!--     <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <p class="h5"><strong>Usuario Logueado:</strong>{{ usuario }}</p>
      </b-col>
    </b-row>
 -->
      <ValidationObserver ref="detailsPaciente">
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
        <b-card header="Datos personales">
          <b-row>
            <b-col lg="3" md="3">
              <b-form-group
                id="Nombre-label"
                label="Nombre :"
                label-for="Nombre"
              >
                <ValidationProvider
                  :name="'Nombre '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="Nombre del paciente"
                    v-model="paciente.nombre"
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
            <b-col lg="3" md="3" sm="10">
              <b-form-group
                id="Apellido-label"
                label="Apellido :"
                label-for="Apellido"
              >
                <ValidationProvider
                  :name="'Apellido '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="Apellido del paciente"
                    v-model="paciente.apellido"
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
            <b-col lg="2" md="2">
              <b-form-group id="dni-label" label="DNI:" label-for="DNI">
                <ValidationProvider
                  :name="'DNI '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    type="number"
                    placeholder="DNI"
                    v-model="paciente.dni"
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
                id="Direccion-label"
                label="Direccion :"
                label-for="Direccion"
              >
                <ValidationProvider
                  :name="'Direccion '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="Direccion del paciente"
                    v-model="paciente.direccion"
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
            <b-col lg="3" md="2">
              <b-form-group
                id="nacimiento-label"
                label="Fecha Nacimiento :"
                label-for="Fecha Nacimiento"
              >
                <ValidationProvider
                  :name="'Fecha-Nacimiento '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    locale="es-AR"
                    type="date"
                    v-model="paciente.fecha_nacimiento"
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
            <b-col lg="4" md="4">
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
                    placeholder="Telefono"
                    v-model="paciente.telefono"
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
                    v-model="paciente.email"
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
            <b-col lg="3" md="3">
              <b-form-group id="os-label" label="Obra Social:" label-for="os">
                <ValidationProvider :name="'os '" v-slot="{ errors, valid }">
                  <b-form-select
                    :options="getObrasSociales"
                    v-model="paciente.obra_social"
                    :state="errors[0] ? false : valid ? true : null"
                  ></b-form-select>
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
                id="numeroOS-label"
                label="Numero de afiliado:"
                label-for="numeroOS"
              >
                <ValidationProvider
                  :name="'numeroOS '"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="Numero de afiliado"
                    type="number"
                    v-model="paciente.numero_afiliado"
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
          </b-row> </b-card
        ><br />
        <b-card header="Historia clinica">
          <b-row>
            <b-col>
              <b-form-group
                id="historiaclinica-label"
                label-for="observaciones"
              >
                <ValidationProvider
                  :name="'historiaclinica '"
                  v-slot="{ errors, valid }"
                >
                  <vue-editor
                    :state="errors[0] ? false : valid ? true : null"
                    v-model="paciente.historia_clinica"
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
      </ValidationObserver>

      <b-row class="pb-2">
        <b-col class="text-center pt-3">
          <b-button
            v-if="!this.editar"
            variant="success"
            @click="crearPaciente()"
            >Crear Paciente
          </b-button>
          <b-button
            v-if="this.editar"
            variant="success"
            @click="editarPaciente()"
            >Editar Paciente
          </b-button>
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>


<script>
import LoginService from "@/services/LoginService";
import PacientesService from "@/services/PacientesService";
import ObrasSocialesService from "@/services/ObrasSocialesService";
import axios from "axios";
import { VueEditor } from "vue2-editor";
export default {
  components: {
    VueEditor,
  },

  props: {
    paciente: {
      type: Object,
      default: function () {
        return {
          nombre: "",
          apellido: "",
          dni: null,
          obra_social: null,
          email: null,
          fecha_nacimiento: null,
          historia_clinica: null,
          telefono: null,
        };
      },
    },
    editar: {
      type: Boolean,
      return: false,
    },
  },
  created() {
    console.log(this.paciente);
  },
  data() {
    return {
      alerts: [],
      loading: true,
      obras_sociales: [],
    };
  },

  methods: {
    async editarPaciente() {
      console.log("edit");
    },
    async crearPaciente() {
      try {
        let result = await this.$refs.detailsPaciente.validate();
        console.log(result);
        let r = await PacientesService.crearPaciente(this.paciente);
        if (r.status == 200) {
          this.$root.$bvToast.toast("Se creo con exito el paciente", {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          });
          this.$router.push({
            name: "listaPacientes",
          });
        }
      } catch (err) {
        console.log(err);
      }
    },
    async obtenerObrasSociales() {
      try {
        const response = await ObrasSocialesService.obtenerObrasSociales();
        this.obras_sociales = response.data;
      } catch (err) {
        console.log(err);
      }
    },
  },
  computed: {
    usuario: function () {
      return LoginService.getApiToken().usuario;
    },
    getObrasSociales() {
      let obras_sociales = this.obras_sociales.map((e) => ({
        value: e.id,
        text: e.nombre,
      }));
      obras_sociales.push({
        value: null,
        text: "-Seleccione la obra social -",
        disabled: true,
      });
      return obras_sociales;
    },
  },

  mounted() {
    axios
      .all([this.obtenerObrasSociales()])
      .then(() => {
        this.loading = false;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

