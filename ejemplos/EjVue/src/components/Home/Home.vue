<template>
  <b-container>
    <br />
    <h4>Listado de estudios</h4>

    <b-col lg="4" class="my-1">
      <b-input-group size="sm">
        <b-form-input
          id="filter-input"
          v-model="filter"
          type="search"
          placeholder="Buscar en el listado"
        ></b-form-input>

        <b-input-group-append>
          <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
        </b-input-group-append>
      </b-input-group>
    </b-col>
    <b-table
      :items="items"
      :fields="fields"
      :filter="filter"
      :current-page="currentPage"
      :per-page="perPage"
      @filtered="onFiltered"
    >
      <template v-slot:cell(acciones)="row">
        <b-button title="Cambiar estado" variant="outline-success">
          <b-icon icon="arrow-clockwise" aria-hidden="true"></b-icon
        ></b-button>

        <b-button
          title="Descargar factura"
          variant="outline-primary"
          v-if="row.item.estado == 'Esperando comprobante pago'"
        >
          <b-icon icon="arrow-down-circle" aria-hidden="true"></b-icon
        ></b-button>

        <b-button
          v-if="row.item.estado == 'Enviar consentimiento informado'"
          title="Descargar consentimiento"
          variant="outline-primary"
        >
          <b-icon icon="arrow-down-circle" aria-hidden="true"></b-icon
        ></b-button>
        <b-button
          v-if="
            row.item.estado == 'Esperando seleccion de turno para la extraccion'
          "
          title="Seleccionar turno"
          variant="outline-info"
        >
          <b-icon icon="calendar2-check" aria-hidden="true"></b-icon
        ></b-button>
      </template>
    </b-table>

    <b-row>
      <b-col  md="1" >
        <b-form-select
          id="per-page-select"
          v-model="perPage"
          :options="pageOptions"
          size="sm"
        ></b-form-select>
      </b-col>
      <b-col class="text-center">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
        ></b-pagination>
      </b-col>
      <br />
    </b-row>
  </b-container>
</template>


<script>
export default {
  name: "Home",

  components: {},
  props: {},

  data() {
    return {
      perPage: 5,
      pageOptions: [5, 10, 15],
      filter: null,
      currentPage: 1,
      totalRows: 1,
      fields: [
        "nombre",
        "numero_afiliado",
        "diagnostico",
        "obra_social",
        "estado",
        "acciones",
      ],
      items: [
        {
          nombre: "Juan perez",
          numero_afiliado: 2004506759,
          diagnostico: "Dickerson",
          obra_social: "Osde",
          estado: "Esperando comprobante pago",
        },
        {
          nombre: "Juan",
          numero_afiliado: 21,
          diagnostico: "Larsen",
          obra_social: "osde",
          estado: "Esperando comprobante pago",
        },
        {
          nombre: "Juan",
          numero_afiliado: 89,
          diagnostico: "Geneva",
          obra_social: "Medife",
          estado: "Enviar consentimiento informado",
        },
        {
          nombre: "Juan",
          numero_afiliado: 38,
          diagnostico: "Jami",
          obra_social: "osde",
          estado: "Esperando comprobante pago",
        },
        {
          nombre: "Nicolas",
          numero_afiliado: 38,
          diagnostico: "Jami",
          obra_social: "osde",
          estado: "Esperando consentimiento informado",
        },
        {
          nombre: "Agustina",
          numero_afiliado: 38213123123,
          diagnostico: "Jami",
          obra_social: "osde",
          estado: "Esperando seleccion de turno para la extraccion",
        },
      ],
    };
  },
  mounted() {
    this.totalRows = this.items.length;
  },
  created() {},
  methods: {
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
  },
};
</script>


<style>
</style>