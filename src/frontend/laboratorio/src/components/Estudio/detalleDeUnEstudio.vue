<template>
  <b-container class="bv-example-row">
    <div v-if="loading">
      <b-spinner> </b-spinner>
    </div>
    <div v-else>    

      <b-card :header="estudio.paciente.apellido +' '+ estudio.paciente.nombre "  header-text-variant="white"
        align="center" header-bg-variant="secondary" title="Datos del estudio" :sub-title="'Creado '+ estudio.fecha_alta  ">
        <br>
        <b-card-text>
          <b-row>
           
            <b-col>
              <b> Medico Derivante: </b>
              {{ estudio.medico_derivante.apellido }}
              {{ estudio.medico_derivante.nombre }} 
            </b-col>
            <b-col> <b> Tipo de estudio: </b>{{ estudio.tipo.nombre }} </b-col>
          </b-row>
          <br>
          <b-row>
            <b-col>
              <b> Diagnostico Presuntivo: </b>{{ estudio.diagnostico.nombre }}
              <br
            /></b-col>
            <b-col>
            <strong> Estado actual: </strong
            >{{ obtenerUltimoEstado() }}</b-col
          >
          </b-row>
        </b-card-text>
      </b-card>

      <b-row>
        <b-col v-if="this.estudio.estados[3] != undefined">
          <h5>
            <div v-if="this.estudio.estados[3].turno != null">
              <strong> Turno:</strong>
              {{ mostrarFecha(this.estudio.estados[3].turno.inicio) }}

              <li>
                Inicio
                {{ mostrarminutos(this.estudio.estados[3].turno.inicio) }}
              </li>
              <li>
                Fin: {{ mostrarminutos(this.estudio.estados[3].turno.fin) }}
              </li>
            </div>
          </h5>
        </b-col>
        <b-col v-if="this.estudio.estados[4] != undefined">
          <h5>
            <div v-if="this.estudio.estados[4].freezer != null">
              <strong> Extraccion:</strong>
              <li>Frezeer: {{ this.estudio.estados[4].freezer }}</li>
              <li>Mililitros: {{ this.estudio.estados[4].mililitros }}</li>
            </div>
          </h5></b-col
        >
      </b-row>
      <b-row>
        <h5>
          <b-col v-if="this.estudio.estados[5] != undefined"
            ><div v-if="this.estudio.estados[5].extracionista != null">
              <strong> Persona que retiro la muestra: </strong
              >{{ this.estudio.estados[5].extracionista }}
            </div>
          </b-col>
        </h5>
      </b-row>
      <b-row>
        <h5>
          <b-col v-if="this.estudio.estados[6] != undefined">
            <div v-if="this.estudio.estados[6].numero_lote != null">
              <strong> Procesado en lote: </strong
              >{{ this.estudio.estados[6].numero_lote }}
            </div></b-col
          >
        </h5>
      </b-row>
      <b-row>
        <h5>
          <b-col v-if="this.estudio.estados[7] != undefined">
            <div v-if="this.estudio.estados[7].numero_lote != null">
              <strong> Informe redactado por: </strong
              >{{ this.estudio.estados[7].numero_lote }}
            </div></b-col
          >
        </h5>
      </b-row>
      <b-row>
        <b-col v-if="this.estudio.paciente.historia_clinica != null">
          <p><strong> Historia clinica: </strong></p>
          <a
            @click="verHistoria()"
            title="ver Historia clinica"
            variant="outline-success"
          >
            <b-icon icon="eye" variant="info"> </b-icon
          ></a>
        </b-col>
        <b-col>
          <p>Presupuesto:</p>
          <a
            title="Descargar Presupuesto"
            variant="outline-success"
            download="presupuesto.pdf"
            @click="bajarPresupuesto()"
          >
            <b-icon icon="download" variant="info"> </b-icon
          ></a>
        </b-col>
        <b-col v-if="this.estudio.estados[0].comprobante != undefined">
          <p>Comprobante:</p>
          <a
            v-if="this.estudio.estados[0] != undefined"
            title="Descargar Comprobante de pago"
            variant="outline-success"
            download="pago.pdf"
            @click="bajarPago()"
          >
            <b-icon icon="download" variant="info"> </b-icon
          ></a>
        </b-col>
        <b-col v-if="this.estudio.estados[3] != undefined">
          <p>Consentimiento:</p>
          <a
            title="Descargar consentimiento firmado"
            variant="outline-success"
            download="consentimiento.pdf"
            @click="bajarConsentimiento()"
          >
            <b-icon icon="download" variant="info"> </b-icon
          ></a>
        </b-col>
      </b-row>

      <b-modal
        size="xl"
        ref="modalResultado"
        title="Cargar resultados del lote"
        ok-only
      >
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
          <b-row>
            <b-col lg="5" md="5" sm="10">
              <b-form-group
                id="Resuttado-label"
                label="Resultado:"
                label-for="Resultado"
              >
                <ValidationProvider
                  :name="'Resultado '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="Resultado"
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

            <b-col lg="5" md="5" sm="10">
              <b-form-group
                id="medico-label"
                label="Medico Informante:"
                label-for="Medico Informante"
              >
                <ValidationProvider
                  :name="'Medico '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    placeholder="medico Informante"
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
                label="Fecha Alta :"
                label-for="Fecha Informe"
              >
                <ValidationProvider
                  :name="'Fecha-alta '"
                  :rules="'required'"
                  v-slot="{ errors, valid }"
                >
                  <b-form-input
                    locale="es-AR"
                    type="date"
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

          <b-card header="Informe del resultado">
            <b-row>
              <b-col>
                <b-form-group
                  id="historiaclinica-label"
                  label-for="Informe del resultado"
                >
                  <ValidationProvider
                    :name="'historiaclinica '"
                    v-slot="{ errors, valid }"
                  >
                    <vue-editor
                      :state="errors[0] ? false : valid ? true : null"
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
      </b-modal>
      <div v-if="this.estudio.paciente.historia_clinica != null">
        <b-modal ref="modalHistoriaCLinica" ok-only title="Historia clinica">
          <div
            v-html="this.estudio.paciente.historia_clinica.historia_clinica"
          ></div>
        </b-modal>
      </div>
    </div>
  </b-container>
</template>

<script>
import { VueEditor } from "vue2-editor";
import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";
export default {
  name: "detalleDeEstudio",

  components: { VueEditor },
  props: {
    estudioId: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      loading: true,
      perPage: 4,
      ultimoEstado: null,
      itemsEst: [],
      alerts: [],
      fieldsEst: [
        { key: "nombre", label: "Nombre", class: "text-center p2" },

        {
          key: "medico_derivante",
          label: "Medico derivante",
          class: "text-center p2",
        },
        { key: "tipo", label: "Tipo Estudio", class: "text-center p2" },
      ],
      pageOptions: [4, 10, 15],
      filter: null,
      currentPage: 1,
      totalRows: 1,
      items: [],
      fields: [
        { key: "id", label: "Numero", class: "text-center p2" },

        { key: "fecha", label: "Fecha Creacion", class: "text-center p2" },

        { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
    };
  },

  created() {
    if (this.estudioId == null) {
      this.$router.push({
        name: "listaEstudios",
      });
    } else {
      console.log(this.estudioId);
    }
  },

  methods: {
    async obtenerDetalleEstudio() {
      try {
        let response = await EstudiosService.obtenerEstudio(this.estudioId);
        console.log(response);
        this.estudio = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    mostrarminutos(fecha) {
      return new Date(fecha).formatTime();
    },
    mostrarFecha(fecha) {
      return new Date(fecha).format("DD-MM-YYYY");
    },
    obtenerUltimoEstado() {
      let nameEstado = this.estudio.ultimo_estado.resourcetype;
      nameEstado = nameEstado.replace(/([a-z])([A-Z])/g, "$1 $2");
      nameEstado = nameEstado.replace(/([A-Z])([A-Z][a-z])/g, "$1 $2");
      return nameEstado;
    },
    verHistoria() {
      this.$refs["modalHistoriaCLinica"].show();
    },
    async bajarPresupuesto() {
      try {
        let response = await EstudiosService.descargarPresupuesto(
          this.estudioId
        );
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async bajarPago() {
      try {
        let response = await EstudiosService.descargarPago(this.estudioId);
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async bajarConsentimiento() {
      try {
        let response = await EstudiosService.descargarConsentimiento(
          this.estudioId
        );
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },

  computed: {},

  mounted() {
    axios
      .all([this.obtenerDetalleEstudio()])
      .then(() => {
        this.loading = false;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
</style>

