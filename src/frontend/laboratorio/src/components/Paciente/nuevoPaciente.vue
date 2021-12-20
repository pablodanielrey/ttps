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
      <b-alert v-if="this.showError" show variant="danger">{{
        this.error
      }}</b-alert>
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
            <b-col lg="6" md="6">
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
            <b-col lg="6" md="6" sm="10">
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
            <b-col lg="4" md="4">
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
                    @click="esMayor()"
                    id="nacimiento-n"
                    v-model="paciente.fecha_nacimiento"
                    required
                    :state="errors[0] ? false : valid ? true : null"
                    type="date"
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

          <div v-if="esMayor()">
            <b-row>
              <b-col lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Numero de Telefono:"
                  label-for="input-2"
                >
                  <b-form-input
                    type="text"
                    v-model="paciente.telefono"
                    placeholder="Ingrese Telefono"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col lg="4" md="4">
                <b-form-group
                  id="input-group-2"
                  label="Direccion de Email:"
                  label-for="input-2"
                >
                  <b-form-input
                    v-model="paciente.email"
                    placeholder="Ingrese Email"
                    required
                    type="email"
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>
            <b-row>
              <b-col lg="8" md="4">
                <b-form-group
                  id="input-group-2"
                  label="Direccion:"
                  label-for="input-2"
                >
                  <b-form-input
                    v-model="paciente.direccion"
                    placeholder="Ingrese Calle"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>
          </div>
          <div v-else class="rounded">
            <h6>
              <b> Datos del tutor </b>
            </h6>
            <hr />
            <br />
            <b-row
              ><br />
              <b-col lg="6">
                <b-form-group label="Nombre del tutor :">
                  <b-form-input
                    v-model="paciente.tutor.tutor.nombre"
                    type="text"
                    placeholder="Ingrese Nombre del tutor"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col lg="6">
                <b-form-group
                  id="input-group-2"
                  label="Apellido del tutor :"
                  label-for="input-2"
                >
                  <b-form-input
                    v-model="paciente.tutor.tutor.apellido"
                    placeholder="Ingrese apellido del tutor"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>
            <b-row>
              <b-col lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Telefono deltutor:"
                  label-for="input-2"
                >
                  <b-form-input
                    type="text"
                    v-model="paciente.tutor.tutor.telefono"
                    placeholder="Ingrese Telefono del tutor"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col lg="4">
                <b-form-group
                  id="input-group-2"
                  label="Email del tutor:"
                  label-for="input-2"
                >
                  <b-form-input
                    v-model="paciente.tutor.tutor.email"
                    placeholder="Ingrese Email del tutor"
                    required
                    type="email"
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col lg="8">
                <b-form-group
                  id="input-group-2"
                  label="Direccion:"
                  label-for="input-2"
                >
                  <b-form-input
                    v-model="paciente.tutor.tutor.direccion"
                    placeholder="Ingrese la direccion"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>
          </div>
          <h6>
            <b> Datos de la obra social </b>
          </h6>
          <hr />
          <b-row>
            <b-col lg="4" md="4">
              <b-form-group id="os-label" label="Obra Social:" label-for="os">
                <ValidationProvider :name="'os '" v-slot="{ errors, valid }">
                  <b-form-select
                    @change="cambioOs()"
                    :options="getObrasSociales"
                    v-model="paciente.obra_social.obra_social.id"
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

            <b-col lg="5" md="5">
              <b-form-group
                id="numeroOS-label"
                label="Numero de afiliado:"
                label-for="numeroOS"
              >
                <ValidationProvider
                  :rules="required"
                  :name="'numeroOS '"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="Numero de afiliado"
                    type="text"
                    v-model="paciente.obra_social.numero_afiliado"
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
                    required
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
          direccion: null,
          obra_social: {
            obra_social: {
              id: null,
              nombre: "test",
            },
            numero_afiliado: null,
          },
          tutor: {
            tutor: {
              nombre: null,
              apellido: null,
              email: null,
              telefono: null,
              direccion: null,
            },
          },
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
  data() {
    return {
      alerts: [],
      loading: true,
      obras_sociales: [],
      required: "",
      showError: false,
      error: null,
    };
  },
  created() {
    console.log("created");
    if (this.editar) {
      console.log("editar");
      this.verificarSiTieneOS();
    }
    console.log(this.paciente);
  },

  methods: {
    verificarSiTieneOS() {
      if (this.paciente.obra_social == null) {
        this.paciente.obra_social = this.paciente.obra_social = {
          obra_social: {
            id: null,
            nombre: "test",
          },
          numero_afiliado: null,
        };
      }
    },
    cambioOs() {
      this.required = "required";
    },
    esMayor() {
      let hoy = new Date();
      let cumpleanos = new Date(this.paciente.fecha_nacimiento);
      let edad = hoy.getFullYear() - cumpleanos.getFullYear();
      let m = hoy.getMonth() - cumpleanos.getMonth();
      if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
        edad--;
      }
      return edad > 17 ? true : false;
    },

    async editarPaciente() {
      try {
        let result = await this.$refs.detailsPaciente.validate();
        if (result) {
          let datos = this.armarArray();

          let r = await PacientesService.editarPaciente(datos);
          if (r.status == 200) {
            this.$root.$bvToast.toast("Se edito con exito el paciente", {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "success",
            });
            this.$router.push({
              name: "listaPacientes",
            });
          }
        }
      } catch (err) {
        console.log(err);
        this.$root.$bvToast.toast("No se pudo editar el paciente", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "danger",
        });
      }
    },
    armarDireccion(calle, numero, piso) {
      return calle + " " + numero + " " + piso;
    },
    async crearPaciente() {
      console.log(this.paciente);
      try {
        let result = await this.$refs.detailsPaciente.validate();
        if (result) {
          let datos = this.armarArray();
          console.log("datos");
          console.log(datos);
            let r = await PacientesService.crearPaciente(datos);
          console.log(r); 

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
      } catch (error) {
        this.showError = true;
        this.error += error.response.data.email != null ? error.response.data.email : '';
        this.error += error.response.data.dni  != null ? error.response.data.dni : '';
        this.error += error.response.data.historia_clinica != null ? error.response.data.historia_clinica : '';
        console.log(error.response);
      }
    },

    armarArray() {
      let os = {};
      let datos = {};
      os = {
        obra_social: {
          obra_social: {
            id: this.paciente.obra_social.obra_social.id,
            nombre: "test",
          },
          numero_afiliado: this.paciente.obra_social.numero_afiliado,
        },
      };
      if (this.esMayor()) {
        datos = {
          nombre: this.paciente.nombre,
          apellido: this.paciente.apellido,
          dni: this.paciente.dni,
          fecha_nacimiento: this.paciente.fecha_nacimiento,
          direccion: this.paciente.direccion,
          email: this.paciente.email,
          historia_clinica: this.paciente.historia_clinica,
          telefono: this.paciente.telefono,
        };
      } else {
        datos = {
          nombre: this.paciente.nombre,
          apellido: this.paciente.apellido,
          dni: this.paciente.dni,
          fecha_nacimiento: this.paciente.fecha_nacimiento,
          historia_clinica: this.paciente.historia_clinica,
          tutor: {
            tutor: {
              nombre: this.paciente.tutor.tutor.nombre,
              apellido: this.paciente.tutor.tutor.apellido,
              email: this.paciente.tutor.tutor.email,
              telefono: this.paciente.tutor.tutor.telefono,
              calle: this.paciente.tutor.tutor.calle,
              numero: this.paciente.tutor.tutor.numero,
              piso: this.paciente.tutor.tutor.piso,
              direccion: this.paciente.tutor.tutor.direccion,
            },
          },
        };
      }
      if (this.paciente.obra_social.numero_afiliado != null) {
        datos = {
          ...datos,
          ...os,
        };
      }
      return datos;
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

