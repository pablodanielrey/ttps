<template>
  <b-container>
    <div v-if="loading">
      <b-spinner> </b-spinner>
    </div>
    <div v-else>
      <b-row class="pb-2">
        <b-col class="text-center pt-3">
          <p class="h3 text-center"><strong> Crear un nuevo Estudio</strong></p>
        </b-col>
      </b-row>

      <b-row class="pb-2">
        <b-col class="text-center pt-3">
          <p class="h5"><strong>Usuario Logueado:</strong>{{ usuario }}</p>
        </b-col>
      </b-row>

      <ValidationObserver ref="detailsEstudio">
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
        <b-card header="Datos Estudio">
          <b-row>
            <b-col lg="5" md="5" sm="10">
              <b-form-group
                id="paciente-label"
                label="Paciente:"
                label-for="Paciente"
              >
                <ValidationProvider
                  :name="'Paciente '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <v-select
                  
                    @input="cambiarPaciente()"
                    placeholder="Seleccione un paciente  "
                    v-model="estudio.paciente"
                    :options="getOptionsPacientes"
                    :value="pacienteSelected"
                    :sercheable="true"
                    responsive="sm"
                    size="sm"
                    lenguage="en-US"
                    :state="errors[0] ? false : valid ? true : null"
                  ></v-select>
                     <p
                      style="color: red; font-size: 10px"
                      v-if="estudio.paciente == '' || estudio.paciente== null "
                    >
                      Se debe seleccionar un paciente
                    </p>
                  <b-form-invalid-feedback
                    v-for="error in errors"
                    :key="error.key"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </ValidationProvider>
              </b-form-group>
            </b-col>
            <b-col lg="5" md="5" sm="10">
              <b-form-group
                id="medico-label"
                label="Medico derivante:"
                label-for="Medico"
              >
                <ValidationProvider
                  :name="'Medico '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="medico derivante"
                    v-model="estudio.medico_derivante"
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
                id="estudio-label"
                label="Tipo de Estudio:"
                label-for="estudio"
              >
                <ValidationProvider :name="'os '" v-slot="{ errors, valid }"  :rules="'required'">
                  <b-form-select
                    :options="getTipoEstudios"
                    v-model="estudio.tipo_estudio"
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
            <b-col lg="3" md="2">
              <b-form-group
                id="nacimiento-label"
                label="Fecha Alta :"
                label-for="Fecha Alta"
              >
                <ValidationProvider
                  :name="'Fecha-alta '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    locale="es-AR"
                    type="date"
                    v-model="estudio.fecha_alta"
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
                id="pdf-label"
                label="Presupuesto del estudio:"
                label-for="pdf"
              >
                <ValidationProvider :name="'pdf '" v-slot="{ errors }">
                  <b-form-file
                    v-model="file1"
                    :state="Boolean(file1)"
                    @change="obtenerPDF($event, file1)"
                    accept="application/pdf"
                    placeholder="Seleccione el presupuesto..."
                    drop-placeholder="Drop file here..."                   
                     browse-text="Buscar"
                  ></b-form-file>
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
        <b-card header="Diagnostico presuntivo">
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
                    v-model="estudio.diagnostico"
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
          <b-button variant="success" @click="crearEstudio()"
            >Crear Estudio
          </b-button>          
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>


<script>
import LoginService from "@/services/LoginService";
import ObrasSocialesService from "@/services/ObrasSocialesService";
import axios from "axios";
import PacientesService from "@/services/PacientesService.js";
import EstudiosService from "@/services/EstudiosService.js";
import { VueEditor } from "vue2-editor";

export default {
  components: { VueEditor },

  props: {},
  created() {},
  data() {
    return {
      pacienteSelected: null,
      estudios: [],
      pacientes: [],
      file1: [],
      alerts: [],
      loading: true,
      estudio: {
        paciente: "",
        medico_derivante: "",
        tipo_estudio: null,
        fecha_alta: null,
        diagnostico_presuntivo: null,
        diagnostico: null,
        presupuesto: null,
      },
    };
  },

  methods: {
    cambiarPaciente() {
      console.log(this.estudio);
    },
    async crearEstudio() {
      try {
        let result = await this.$refs.detailsEstudio.validate();
        console.log(this.estudio);
        if (result) {
          let r = await EstudiosService.crearEstudio(this.estudio);
          console.log(r);
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
    async obtenerPacientes() {
      try {
        let response = await PacientesService.obtenerPacientes();
        this.pacientes = response.data;
      } catch (err) {
        console.log(err);
      }
    },
    async obtenerEstudios() {
      try {
        let response = await EstudiosService.obtenerEstudios();
        this.estudios = response.data;
      } catch (err) {
        console.log(err);
      }
    },

    obtenerPDF(event) {
     const file = event.target.files[0];
        this.createBase64(file);
        console.log( this.estudio)
    },
    createBase64(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.estudio.presupuesto=  e.target.result;
      };
      reader.readAsDataURL(file);
    },   
  },
  computed: {
    usuario: function () {
      return LoginService.getApiToken().usuario;
    },
    getTipoEstudios() {
      let estudios = this.estudios.map((e) => ({
        value: e.id,
        text: e.nombre,
      }));
      estudios.push({
        value: null,
        text: "-Seleccione un estudio -",
        disabled: true,
      });
      return estudios;
    },
    getOptionsPacientes() {
      let pacientes = this.pacientes.map((e) => ({
        id: e.id,
        label: e.nombre + " " + e.apellido,
      }));
      return pacientes;
    },
  },

  mounted() {
    axios
      .all([
        this.obtenerObrasSociales(),
        this.obtenerPacientes(),
        this.obtenerEstudios(),
      ])
      .then(() => {
        this.loading = false;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

