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

      <!--       <b-row class="pb-2">
        <b-col class="text-center pt-3">
          <p class="h5"><strong>Usuario Logueado:</strong>{{ usuario }}</p>
        </b-col>
      </b-row> -->

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
                    v-if="estudio.paciente == '' || estudio.paciente == null"
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
                id="MedicoDerivante-label"
                label="Medico Derivante:"
                label-for="medico"
              >
                <ValidationProvider
                  :name="'Medico derivante '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <v-select
                    placeholder="Seleccione un medico derivante  "
                    v-model="estudio.medico_derivante"
                    :options="getOptionsMedicoDerivante"
                    :value="medicoDerivanteSelected"
                    :sercheable="true"
                    responsive="sm"
                    size="sm"
                    lenguage="en-US"
                    :state="errors[0] ? false : valid ? true : null"
                  ></v-select>
                  <p
                    style="color: red; font-size: 10px"
                    v-if="
                      estudio.medico_derivante == '' ||
                      estudio.medico_derivante == null
                    "
                  >
                    Se debe seleccionar un medico derivante
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
          </b-row>
          <b-row>
            <b-col lg="5" md="5">
              <b-form-group
                id="estudio-label"
                label="Tipo de Estudio:"
                label-for="estudio"
              >
                <ValidationProvider
                  :name="'Tipo de estudio '"
                  v-slot="{ errors, valid }"
                  :rules="'required'"
                >
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
                label-for="Presupuesto del estdio"
              >
                <ValidationProvider
                  :rules="'required'"
                  :name="'Presupuesto del estdio '"
                  v-slot="{ errors }"
                >
                  <b-form-file
                    v-model="file1"
                    :state="errors[0] ? false : valid ? true : null"
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

            <b-col lg="5" md="5" sm="10">
              <b-form-group
                id="diagnostico-label"
                label="Diagnostico:"
                label-for="diagnostico"
              >
                <ValidationProvider
                  :name="'diagnostico '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <v-select
                    @input="cambiarDiagnostico()"
                    placeholder="Seleccione un diagnostico  "
                    v-model="estudio.diagnostico"
                    :options="getOptionsDiagnosticos"
                    :value="diagnosticoSelected"
                    :sercheable="true"
                    responsive="sm"
                    size="sm"
                    lenguage="en-US"
                    :state="errors[0] ? false : valid ? true : null"
                  ></v-select>
                  <p
                    style="color: red; font-size: 10px"
                    v-if="
                      estudio.diagnostico == '' || estudio.diagnostico == null
                    "
                  >
                    Se debe seleccionar un diagnostico
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
          </b-row>
        </b-card>
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
                    v-model="estudio.diagnostico_presuntivo"
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
          <b-button variant="outline-success" @click="crearEstudio()" id="btnAgrandar"
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
  components: {
    VueEditor,
  },

  props: {},
  created() {},
  data() {
    return {
      valid: null,
      pacienteSelected: null,
      medicoDerivanteSelected: null,
      diagnosticoSelected: null,
      estudios: [],
      pacientes: [],
      medicosDerivantes: [],
      diagnosticosLista: [],
      file1: [],
      alerts: [],
      loading: true,
      historiaClinicaPaciente: null,
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
      this.obtenerHistoriaClinicaPaciente();
    },
    cambiarDiagnostico() {
      console.log(this.estudio);
    },
    async crearEstudio() {
      try {
        let result = await this.$refs.detailsEstudio.validate();
        console.log(this.estudio);
        if (result) {
          let r = await EstudiosService.crearEstudio(this.estudio);
          console.log(r.status);
          if (r.status == 200) {
            this.$root.$bvToast.toast("Se creo con exito el estudio", {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "success",
            });
            this.$router.push({
              name: "listaEstudios",
            });
          }
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

    async obtenerMedicosDerivantes() {
      try {
        let response = await PacientesService.obtenerMedicosDerivantes();
        this.medicosDerivantes = response.data;
        console.log(this.medicosDerivantes);
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
    async obtenerHistoriaClinicaPaciente() {
      console.log(this.estudio.paciente.id);
      try {
        let response = await PacientesService.obtenerPaciente(
          this.estudio.paciente.id
        );
        this.estudio.diagnostico_presuntivo = response.data.historia_clinica;
        console.log(response.data);
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
    async obtenerDiagnosticos() {
      try {
        let response = await EstudiosService.obtenerDiagnosticos();
        this.diagnosticosLista = response.data;
      } catch (err) {
        console.log(err);
      }
    },

    obtenerPDF(event) {
      const file = event.target.files[0];
      this.createBase64(file);
      console.log(this.estudio);
    },
    createBase64(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.estudio.presupuesto = e.target.result;
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
    getOptionsMedicoDerivante() {
      let pacientes = this.medicosDerivantes.map((e) => ({
        id: e.id,
        label: e.nombre + " " + e.apellido,
      }));
      return pacientes;
    },
    getOptionsDiagnosticos() {
      let diagnosticosLista = this.diagnosticosLista.map((e) => ({
        id: e.id,
        label: e.nombre,
      }));
      return diagnosticosLista;
    },
  },

  mounted() {
    axios
      .all([
        this.obtenerObrasSociales(),
        this.obtenerPacientes(),
        this.obtenerEstudios(),
        this.obtenerDiagnosticos(),
        this.obtenerMedicosDerivantes(),
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
<style scoped>
#btnAgrandar{
         width: 250px
}
</style>
