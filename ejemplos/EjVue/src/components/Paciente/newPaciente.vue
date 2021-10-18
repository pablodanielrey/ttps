<template>
  <b-container>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <p class="h3 text-center"><strong> Crear un nuevo paciente</strong></p>
      </b-col>
    </b-row>

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
            <b-form-group id="Nombre-label" label="Nombre :" label-for="Nombre">
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
                  v-model="paciente.apellidos"
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
                  v-model="paciente.nacimiento"
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
                  :options="optionsOS"
                  v-model="selectedOS"
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
                  v-model="paciente.numeroOS"
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
            <b-form-group id="historiaclinica-label" label-for="observaciones">
              <ValidationProvider
                :name="'historiaclinica '"
                v-slot="{ errors, valid }"
              >
                <vue-editor
                  :state="errors[0] ? false : valid ? true : null"
                  v-model="paciente.historia"
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
        <b-button variant="success" @click="crearPaciente()"
          >Crear Paciente
        </b-button>
      </b-col>
    </b-row>
  </b-container>
</template>


<script>
import { VueEditor } from "vue2-editor";
export default {
  components: {
    VueEditor,
  },

  props: {},
  data() {
    return {
      alerts: [],
      paciente: [],
      selectedOS: null,
      optionsOS: [
        { value: null, text: "Seleccione una obra social" },
        { value: "Osde", text: "Osde" },
        { value: "Medife", text: "Medife" },
        { value: "Ioma", text: "Ioma" },
        { value: "Galeno", text: "Galeno" },
        { value: "Swiss Medical", text: "Swiss Medical" },
      ],
    };
  },
  methods: {
    async crearPaciente(){
      let result = await this.$refs.detailsPaciente.validate();
      console.log(result)

      console.log(this.paciente)
    }
  },
  computed: {},
};
</script>

