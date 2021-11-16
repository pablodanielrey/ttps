<template>
  <b-container class="bv-example-row">
    <br />
    <b-card header="Detalle de un estudio">
      <b-row>
        <b-col
          ><strong> Paciente: </strong> {{ estudio.paciente.apellido }}
          {{ estudio.paciente.nombre }} <br
        /></b-col>
        <b-col>
          <strong> Fecha de alta: </strong>{{ estudio.fecha_alta }} <br
        /></b-col>
      </b-row>
      <b-row>
        <b-col>
          <strong> Medico Derivante: </strong>
          {{ estudio.medico_derivante.apellido }}
          {{ estudio.medico_derivante.nombre }} <br
        /></b-col>

        <b-col>
          <strong> Diagnostico Presuntivo: </strong
          >{{ estudio.diagnostico.nombre }} <br
        /></b-col>
      </b-row>
      <b-row>
        <b-col>
          <strong> Tipo de estudio: </strong>{{ estudio.tipo.nombre }}</b-col
        >
        <b-col> <strong> Estado : </strong>{{ ultimoEstado }}</b-col>
      </b-row>
      <b-row>
        <!--   <b-col lg="3" md="3" sm="7">
          <b-button
            variant="outline-primary"
            @click="ingresarComprobante()"
            title="Ingresar comprobante de  pago"
          >
            Ingresar comprobante</b-button
          >
        </b-col> -->
        <b-col v-if="this.estudio.estados[1].consentimiento != undefined">
          <a
            v-if="this.estudio.estados[1] != undefined"
            title="Descargar consentimiento"
            variant="outline-success"
            download="consentimiento.pdf"
            :href="this.estudio.estados[1].consentimiento"
          >
            <b-icon icon="download" variant="info"> </b-icon
          ></a>
        </b-col>
        <!--     <b-col lg="1" md="3" sm="7">
          <b-button
            title="Cargar consentimiento informado firmado"
            variant="outline-primary"
            @click="cargarConsentimiento()"
          >
            Cargar Consentimiento</b-button
          >
        </b-col> -->

        <!--   <b-col lg="3" md="3" sm="7">
          <b-button
            title="Bajar consentimiento informado"
            variant="outline-primary"
            @click="seleccionarTurno()"
          >
            Seleccionar turno</b-button
          >
        </b-col> -->
        <!--    <b-col>
          <b-button
            lg="3"
            md="3"
            sm="10"
            title="Bajar consentimiento informado"
            variant="outline-primary"
            @click="ingresarMuestra()"
          >
            Ingresar muestra</b-button
          >
        </b-col> -->
        <!--  <b-col>
          <b-button
            title="Persona que retiro muestra"
            variant="outline-primary"
            @click="retiroMuestra()"
          >
            Retiro muestra</b-button
          >
        </b-col> -->
        <!--   <b-col>
          <b-button
            title="Informe de resultados"
            variant="outline-primary"
            @click="cargarResultado()"
          >
            Informe Resultados</b-button
          >
        </b-col> -->
      </b-row>
    </b-card>

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
  </b-container>
</template>

<script>
import { VueEditor } from "vue2-editor";

export default {
  name: "detalleDeEstudio",

  components: { VueEditor },
  props: {
    estudio: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
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
    if (this.estudio == null) {
      this.$router.push({
        name: "listaEstudios",
      });
    } else {
      this.obtenerUltimoEstado();
    }
  },

  methods: {
    obtenerUltimoEstado() {
      let estado = this.estudio.estados.sort(function (a, b) {
        if (a.fecha < b.fecha) {
          return 1;
        }
        if (a.fecha > b.fecha) {
          return -1;
        }
        return 0;
      });
      this.ultimoEstado = estado[0].resourcetype;
      this.ultimoEstado = this.ultimoEstado.replace(/([a-z])([A-Z])/g, "$1 $2");
      this.ultimoEstado = this.ultimoEstado.replace(
        /([A-Z])([A-Z][a-z])/g,
        "$1 $2"
      );
    },
    ingresarComprobante() {
      this.$router.push({
        name: "EsperandoComprobanteDePago",
        params: {
          idEstudio: this.estudio.id,
        },
      });
    },
    ingresarMuestra() {
      this.$router.push({
        name: "EsperandoTomaDeMuestra",
        params: {
          idEstudio: this.estudio.id,
        },
      });
    },
    retiroMuestra() {
      this.$router.push({
        name: "EsperandoRetiroDeExtaccion",
        params: {
          idEstudio: this.estudio.id,
        },
      });
    },
    seleccionarTurno() {
      console.log("Turno");
      console.log(this.estudio);
      this.$router.push({
        name: "EsperandoSeleccionDeTurnoParaExtraccion",
        params: {
          estudio: this.estudio,
        },
      });
    },
    verEstudios(item) {
      this.itemsEst = item.estudios;
      this.$refs["my-modal"].show();
    },
    cargarResultado() {
      this.$refs["modalResultado"].show();
    },
    cargarConsentimiento() {
      this.$router.push({
        name: "EsperandoConsentimientoInformado",
        params: {
          idEstudio: this.estudio.id,
        },
      });
    },
  },

  computed: {},

  mounted() {},
};
</script>

<style>
</style>

