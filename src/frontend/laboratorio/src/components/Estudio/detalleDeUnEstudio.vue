<template>
  <b-container class="bv-example-row">
    <div v-if="loading">
      <b-spinner> </b-spinner>
    </div>
    <div v-else>    
          <b-col class="text-left">
                <router-link to="/listaEstudios"
                  ><b-icon icon="arrow-left-circle"></b-icon
                ></router-link>
              </b-col>   
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
              v-if="estado.resourcetype == 'EsperandoConsentimientoInformado'"
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
                v-if="estado.resourcetype == 'AnuladorPorFaltaDePago'"
                header="Estudio anulado por falta de pago"
                header-text-variant="white"
                align="center"
                header-bg-variant="danger"
              >
                <br />
                <b-card-text>
                  <b-alert show variant="danger"
                    >Atencion! este estudio fue anulado por falta de
                    pago</b-alert
                  >
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
                    <small v-if="estado.turno.cancelado != null" id="turnoCancelado">Este turno fue cancelado</small> 
                    <b-button variant="outline-danger" @click="cancelarTurno(estado.turno.id)" v-if="verificarCancelar(estado)">Cancelar</b-button>
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

                    <li v-if="estado.freezer != null">
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
                    <strong>Url : </strong>                
                     <a :href="estado.resultado_url "  target="_blank"> <b-icon icon="link" variant="info"> </b-icon>Click para Acceder a el informe!</a>
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
                      @click="bajarInforme()"
                      title="ver Informe del resultado"
                      variant="outline-success"
                    >
                      <b-icon icon="download" variant="info"> </b-icon
                    ></a>
                  </div>
                  <div v-else>
                    <small>
                      Esperando que el medico informante carge los datos</small
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
                header="Estudio entregado"
                header-text-variant="white"
                align="center"
                header-bg-variant="success"
              >
                <br />
                <b-card-text>
                  <div v-if="estado.fecha != null">
                    <strong> Fecha :</strong>
                    {{ mostrarFecha(estado.fecha) }}
                    <br />
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
                v-if="estado.resourcetype == 'EstadoVirtualEsperandoResultado'"
                header="Entrega del estudio"
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
                    <strong v-if="estado.numero_lote  != null"> Numero de lote :</strong>
                    {{ estado.numero_lote }}
                    <br />
                    <strong v-if="estado.informe  != null"> Informe :
                   <a
                      @click="bajarInforme()"
                      title="ver Informe del resultado"
                      variant="outline-success"
                    >
                      <b-icon icon="download" variant="info"> </b-icon
                    ></a></strong>
                    <br />
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
            v-html="this.estudio.paciente.historia_clinica"
          ></div>
        </b-modal>
      </div>
   
    </div>
 
  </b-container>
</template>

<script>
import EstudiosService from "@/services/EstudiosService.js";
import TurnosService from "@/services/TurnosService.js";
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
    } 
  },

  methods: {
    verificarCancelar(estado){     
      return ((new Date(estado.turno.inicio) > new Date()) && (estado.turno.cancelado == null) && (estado.fecha_muestra == null))

    },
   async cancelarTurno(turno){
      try {
       
        let response = await TurnosService.cancelarTurno(turno);       
        if (response.status == 200){
          this.obtenerDetalleEstudio()
            this.$root.$bvToast.toast(
            "Usted cancelo el turno",
            {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "info",
            }
          );
        }
        

      } catch (error) {
        console.log(error)
          this.$root.$bvToast.toast(
            "No puede cancelar el turno ",
            {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "danger",
            }
          );
      }

    },
    async obtenerDetalleEstudio() {
      try {
        let response = await EstudiosService.obtenerEstudio(this.estudioId);  
        this.estudio = response.data;
        this.estados = this.ordenarEstados(response.data.estados);
      } catch (error) {
        console.log(error);
      }
    },
    ordenarEstados(estados) {
      estados.sort(function (a, b) {
        if (a.fecha > b.fecha) {
          return 1;
        }
        if (a.fecha < b.fecha) {
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
    async bajarInforme() {
      try {
     await EstudiosService.descargarInformeDeResultado(
          this.estudio.id
        );
      } catch (error) {
        console.log(error);
      }
    },
    async bajarPresupuesto() {
      try {
         await EstudiosService.descargarPresupuesto(
          this.estudioId
        );
      } catch (error) {
        console.log(error);
      }
    },
    async bajarPago() {
      try {
        await EstudiosService.descargarPago(this.estudioId);
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
#turnoCancelado{
 color: red;
}
</style>

