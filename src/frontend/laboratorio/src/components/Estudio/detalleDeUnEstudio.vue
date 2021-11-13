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
        <b-col> <strong> Estado : </strong>Resultado Entregado</b-col>
      </b-row>
      <b-row>
        <b-col class="text-center pt-3">
          <h4>Acciones</h4>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-button
            title="Descargar Presupuesto"
            variant="outline-primary"
            download="presupuesto.pdf"
          >
            <b-icon icon="download" aria-hidden="true"></b-icon> <br
          /></b-button>
        </b-col>
        <b-col lg="3" md="3" sm="10">
          <b-button
            variant="outline-primary"
            @click="ingresarComprobante()"
            title="Ingresar comprobante de  pago"
          >
            Ingresar comprobante</b-button
          >
        </b-col>
        <b-col>
          <b-button
            title="Bajar consentimiento informado"
            variant="outline-primary"
            @click="bajarConsentimiento()"
          >
            <b-icon icon="download" aria-hidden="true"></b-icon
          ></b-button>
        </b-col>
        <b-col lg="3" md="3" sm="10">
          <b-button
            title="Enviar consentimiento informado"
            variant="outline-primary"
          >
            Enviar Consentimiento</b-button
          >
        </b-col>
      </b-row>
      <b-row>
        <br />
        <b-col lg="3" md="3" sm="10">
          <b-button
            title="Bajar consentimiento informado"
            variant="outline-primary"
            @click="seleccionarTurno()"
          >
            Seleccionar turno</b-button
          >
        </b-col>
        <b-col>
          <b-button
            lg="3"
            md="3"
            sm="10"
            title="Bajar consentimiento informado"
            variant="outline-primary"
          >
            Ingresar muestra</b-button
          >
        </b-col>
        <b-col>
          <b-button
            title="Persona que retiro muestra"
            variant="outline-primary"
            @click="bajarConsentimiento()"
          >
            Retiro muestra</b-button
          >
        </b-col>
        <b-col>
          <b-button
            title="Informe de resultados"
            variant="outline-primary"
            @click="cargarResultado()"
          >
            Informe Resultados</b-button
          >
        </b-col>
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
    },
  },
  data() {
    return {
      perPage: 4,
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
    console.log(this.estudio);
  },

  methods: {
    ingresarComprobante() {
      console.log(this.estudio);
      this.$router.push({
        name: "esperandoComprobantePago",
        params: {
          estudio: this.estudio,
        },
      });
    },
    seleccionarTurno() {
      console.log("Turno");
      console.log(this.estudio);
      this.$router.push({
        name: "seleccionTurno",
        params: {
          estudio: this.estudio,
        },
      });
    },
    verEstudios(item) {
      console.log(item);
      this.itemsEst = item.estudios;
      this.$refs["my-modal"].show();
    },
    cargarResultado() {
      this.$refs["modalResultado"].show();
    },
  },

  computed: {},

  mounted() {},
};
</script>

<style>
</style>

