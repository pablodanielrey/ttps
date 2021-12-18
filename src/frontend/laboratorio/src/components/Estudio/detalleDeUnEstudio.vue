<template>
  <b-container class="bv-example-row">
    <div v-if="loading">
      <b-spinner> </b-spinner>
    </div>
    <div v-else>
      <b-card
        :header="estudio.paciente.apellido + ' ' + estudio.paciente.nombre"
        header-text-variant="white"
        align="center"
        header-bg-variant="secondary"
        title="Datos del estudio"
        :sub-title="'Creado ' + estudio.fecha_alta"
      >
        <br />
        <b-card-text>
          <b-row>
            <b-col>
              <b> Medico Derivante: </b>
              {{ estudio.medico_derivante.apellido }}
              {{ estudio.medico_derivante.nombre }}
            </b-col>
            <b-col> <b> Tipo de estudio: </b>{{ estudio.tipo.nombre }} </b-col>
          </b-row>
          <br />
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
          <b-row
            ><b-col>
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
              <p><strong>Presupuesto:</strong></p>
              <a
                title="Descargar Presupuesto"
                variant="outline-success"
                download="presupuesto.pdf"
                @click="bajarPresupuesto()"
              >
                <b-icon icon="download" variant="info"> </b-icon
              ></a>
            </b-col>
          </b-row>
        </b-card-text>
      </b-card>
      <b-row>
        <div v-for="estado in estados" :key="estado.id">
          
          <b-row >
             <b-card-group deck>
            <b-col cols="10" md="auto" >
              <b-card
              deck
                v-if="estado.resourcetype == 'EsperandoComprobanteDePago'"
                header="Comprobante pago"
                header-text-variant="white"
                align="center"
                header-bg-variant="secondary"
              >
                <br />
                <b-card-text>
                  <strong> Fecha envio:</strong>
                  {{ mostrarFecha(estado.fecha) }}
                  <a
                    v-if="estado.combrobante != null"
                    title="Descargar Comprobante de pago"
                    variant="outline-success"
                    download="pago.pdf"
                    @click="bajarPago()"
                    ><br />
                    <b-icon icon="download" variant="info"> </b-icon
                  ></a>
                  <br />
                </b-card-text>
              </b-card>
            </b-col>
            <b-col cols="12" md="auto">
              <b-card
                v-if="estado.resourcetype == 'EnviarConsentimientoInformado'"
                header="Consentimiento Informado"
                header-text-variant="white"
                align="center"
                header-bg-variant="secondary"
              >
                <br />
                <b-card-text>
                  <strong> Fecha envio:</strong>
                  {{ mostrarFecha(estado.fecha_enviado) }}
                  <a
                    v-if="estado.consentimiento != null"
                    title="Descargar consentimiento firmado"
                    variant="outline-success"
                    download="consentimiento.pdf"
                    @click="bajarConsentimiento()"
                    ><br />
                    <b-icon icon="download" variant="info"> </b-icon
                  ></a>
                  <br />
                </b-card-text>
              </b-card>
            </b-col>
             </b-card-group>
          </b-row>
          <b-row>
            <b-col cols="12" md="auto">
              <b-card
                v-if="
                  estado.resourcetype ==
                  'EsperandoSeleccionDeTurnoParaExtraccion'
                "
                header="Turnos"
                header-text-variant="white"
                align="center"
                header-bg-variant="secondary"
              >
                <br />
                <b-card-text>
                  <div v-if="estado.turno != null">
                    <strong> Turno:</strong>
                    {{ mostrarFecha(estado.turno.inicio) }}

                    <li>
                      Inicio
                      {{ mostrarminutos(estado.turno.inicio) }}
                    </li>
                    <li>Fin: {{ mostrarminutos(estado.turno.fin) }}</li>
                  </div>
                  <br />
                </b-card-text>
              </b-card>
            </b-col>
          </b-row>
          <b-card
            v-if="estado.resourcetype == 'EsperandoTomaDeMuestra'"
            header="Toma de muestra"
            header-text-variant="white"
            align="center"
            header-bg-variant="secondary"
          >
            <br />
            <b-card-text>
              <div>
                <strong> Fecha:</strong>
                {{ mostrarFecha(estado.fecha_muestra) }}

                <li>
                  Frezeer:
                  {{ estado.freezer }}
                </li>
                <li>Mililitros: {{ estado.mililitros }}</li>
                <li>Expiro: {{ expiroToma(estado.expirado) }}</li>
              </div>
              <br />
            </b-card-text>
          </b-card>
        </div>

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
import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";
export default {
  name: "detalleDeEstudio",

  components: {},
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
      estados: [],
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

        this.estados = this.ordenarEstados(response.data.estados);
      } catch (error) {
        console.log(error);
      }
    },
    ordenarEstados(estados) {
      estados.sort(function (a, b) {
        if (a.resourcetype > b.resourcetype) {
          return 1;
        }
        if (a.resourcetype < b.resourcetype) {
          return -1;
        }
        // a must be equal to b
        return 0;
      });
      return estados;
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
    expiroToma(toma) {
      return toma == true ? "Si" : "No";
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

