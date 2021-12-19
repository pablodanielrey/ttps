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
      <b-container fluid class="text-center">
     
          <div v-for="estado in estados" :key="estado.id">
   
              <b-card-group deck>             
                <b-card
                
                  v-if="estado.resourcetype == 'EsperandoComprobanteDePago'"
                  header="Comprobante pago"
                  header-text-variant="white"
                  align="center"
                  header-bg-variant="secondary"
                >
                  <b-card-text>
                    <strong> Fecha envio:</strong>
                    {{ mostrarFecha(estado.fecha) }}
                    <a
                      v-if="estado.comprobante != null"
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
            
                <b-card
                
                  v-if="
                    estado.resourcetype == 'EsperandoConsentimientoInformado'
                  "
                  header="Consentimiento Informado"
                  header-text-variant="white"
                  align="center"
                  header-bg-variant="secondary"
                >
                  <b-card-text>
                    <strong> Fecha :</strong>
                    {{ mostrarFecha(estado.fecha) }}
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
         
              </b-card-group>
            <b-card-group deck>
              <b-col>
                <b-card
                  deck
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
                    <div v-else>
                      <small> No selecciono turno</small>
                    </div>
                    <br />
                  </b-card-text>
                </b-card>
              </b-col>
            </b-card-group>
            <b-card-group deck>
              <b-col>
                <b-card
                  deck
                  v-if="estado.resourcetype == 'EsperandoTomaDeMuestra'"
                  header="Toma de muestra"
                  header-text-variant="white"
                  align="center"
                  header-bg-variant="secondary"
                >
                  <br />
                  <b-card-text>
                    <div v-if="estado.mililitros != null">
                      <strong> Fecha:</strong>
                      {{ mostrarFecha(estado.fecha_muestra) }}

                      <li>
                        Frezeer:
                        {{ estado.freezer }}
                      </li>
                      <li>Mililitros: {{ estado.mililitros }}</li>
                      <li>Expiro: {{ expiroToma(estado.expirado) }}</li>
                    </div>
                    <div v-else>
                      <small> No se cargaron los datos de la muestra</small>
                    </div>
                    <br />
                  </b-card-text>
                </b-card>
              </b-col>
            </b-card-group>
            <b-card-group deck>
              <b-col>
                <b-card
                  deck
                  v-if="estado.resourcetype == 'EsperandoRetiroDeExtaccion'"
                  header="Retiro de la extraccion"
                  header-text-variant="white"
                  align="center"
                  header-bg-variant="secondary"
                >
                  <br />
                  <b-card-text v-if="estado.fecha_retiro != null">
                    <div>
                      <strong> Fecha de retiro:</strong>
                      {{ mostrarFecha(estado.fecha_retiro) }}
                      <br />
                      <strong>Extraccionista:</strong>
                      {{ estado.extracionista }}
                    </div>
                    <br />
                  </b-card-text>
                </b-card>
              </b-col>
            </b-card-group>
            <b-card-group deck>
              <b-col>
                <b-card
                  deck
                  v-if="
                    estado.resourcetype ==
                    'EsperandoLoteDeMuestraParaProcesamientoBiotecnologico'
                  "
                  header="Retiro de la extraccion"
                  header-text-variant="white"
                  align="center"
                  header-bg-variant="secondary"
                >
                  <br />
                  <b-card-text>
                    <div v-if="estado.numero_lote != null">
                      <strong> Fecha :</strong>
                      {{ mostrarFecha(estado.fecha) }}
                      <br />
                      <strong>Procesado en el lote:</strong>
                      {{ estado.numero_lote }}
                    </div>
                    <div v-else>
                      <small> El estudio no se proceso en ningun lote</small>
                    </div>
                    <br />
                  </b-card-text>
                </b-card>
              </b-col>
            </b-card-group>
            <b-card-group deck>
              <b-col>
                <b-card
                  deck
                  v-if="
                    estado.resourcetype ==
                    'EsperandoProcesamientoDeLoteBiotecnologico'
                  "
                  header="Resultado del lote"
                  header-text-variant="white"
                  align="center"
                  header-bg-variant="secondary"
                >
                  <br />
                  <b-card-text>
                    <div v-if="estado.fecha_resultado != null">
                      <strong> Fecha :</strong>
                      {{ mostrarFecha(estado.fecha_resultado) }}
                      <br />
                      <strong>Url:</strong>
                      {{ estado.resultado_url }}
                    </div>
                    <div v-else>
                      <small> No se cargo la url del resultado</small>
                    </div>
                    <br />
                  </b-card-text>
                </b-card>
              </b-col>
            </b-card-group>
            <b-card-group deck>
              <b-col>
                <b-card
                  deck
                  v-if="
                    estado.resourcetype == 'EsperandoInterpretacionDeResultados'
                  "
                  header="Resultado del medico informante"
                  header-text-variant="white"
                  align="center"
                  header-bg-variant="secondary"
                >
                  <br />
                  <b-card-text>
                    <div v-if="estado.fecha_informe != null">
                      <strong> Fecha :</strong>
                      {{ mostrarFecha(estado.fecha_informe) }}
                      <br />
                      <strong>Resultado:</strong>
                      {{ estado.resultado }}
                      <br />
                      <strong>Medico:</strong>
                      {{ estado.medico_informante.nombre }}
                      {{ estado.medico_informante.apellido }}
                      <br />
                      <p><strong>Informe: </strong></p>
                      <a
                        @click="verInforme(estado.informe)"
                        title="ver Informe del resultado"
                        variant="outline-success"
                      >
                        <b-icon icon="eye" variant="info"> </b-icon
                      ></a>
                    </div>
                    <div v-else>
                      <small>
                        Esperando que el medico informante carge los
                        datos</small
                      >
                    </div>
                    <br />
                  </b-card-text>
                </b-card>
              </b-col>
            </b-card-group>
            <b-card-group deck>
              <b-col>
                <b-card
                  deck
                  v-if="estado.resourcetype == 'ResultadoDeEstudioEntregado'"
                  header="Estudio finalizado"
                  header-text-variant="white"
                  align="center"
                  header-bg-variant="secondary"
                >
                  <br />
                  <b-card-text>
                    <div v-if="estado.fecha != null">
                      <strong> Fecha :</strong>
                      {{ mostrarFecha(estado.fecha) }}
                      <br />
                      Aca deberia descargar informe final
                    </div>

                    <br />
                  </b-card-text>
                </b-card>
              </b-col>
            </b-card-group>
          </div>
      </b-container>
      <div v-if="this.estudio.paciente.historia_clinica != null">
        <b-modal ref="modalHistoriaCLinica" ok-only title="Historia clinica">
          <div
            v-html="this.estudio.paciente.historia_clinica.historia_clinica"
          ></div>
        </b-modal>
      </div>
      <div v-if="this.informeVer != null">
        <b-modal ref="modalInforme" ok-only title="Informe del resultado">
          <div v-html="this.datosInforme"></div>
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
      informeVer: false,
      datosInforme: [],
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
    verInforme(informe) {
      this.informeVer = true;
      this.datosInforme = informe;
      console.log(informe);
      this.$refs["modalInforme"].show();
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

