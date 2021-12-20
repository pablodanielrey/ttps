<template>
  <b-container fluid>
    <div v-if="loading">
      <b-spinner> </b-spinner>
      <h4>Listado de Estudios</h4>
    </div>
    <div v-else>
      <b-col lg="4" class="my-1">
        <b-input-group size="sm">
          <b-form-input
            id="filter-input"
            v-model="filter"
            type="search"
            placeholder="Buscar por nombre de paciente,medico derivante u diagnostico"
          ></b-form-input>

          <b-input-group-append>
            <b-button :disabled="!filter" @click="filter = ''">Buscar</b-button>
          </b-input-group-append>
        </b-input-group>
      </b-col>
      <b-table
        show-empty
        empty-text="El sistema no posee estudios cargados"
        :items="items"
        :fields="fields"
        :filter="filter"
        :current-page="currentPage"
        :per-page="perPage"
        @filtered="onFiltered"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
      >
        <template v-slot:cell(estados)="row">
          {{ obtenerUltimoEstado(row.item) }}
        </template>
        <template v-slot:cell(fecha)="row">
          {{ armarFecha(row.item) }}
        </template>

        <template v-slot:cell(acciones)="row">
          <b-button @click="detalleEstudio(row.item)" variant="outline-white">
            <b-icon icon="file-earmark-person-fill" variant="info"> </b-icon>
          </b-button>
          <div v-if="esUltimoEstado(row.item)">
            <b-button
              @click="siguienteEstado(row.item)"
              variant="outline-white"
              title="Siguiente estado"
            >
              <b-icon icon="arrow-right-square" variant="info"> </b-icon>
            </b-button>
          </div>
          <b-button
            title="Anular estudio por falta de comprobante de pago"
            variant="outline-white"
            v-if="checkComprobantePago(row.item)"
            @click="anularEstudioFaltaComprobante(row.item)"
          >
            <b-icon icon="x-circle" fill variant="danger"> </b-icon>
          </b-button>
          <b-button
            title="Volver a seleccion de turno, falta de datos en la muestra"
            variant="outline-white"
            v-if="checkFaltaDatosMuestra(row.item)"
            @click="anularEstudioFaltaDatosMuestra(row.item)"
            ><b-icon icon="x-circle" fill variant="danger"> </b-icon>
          </b-button>
        </template>
      </b-table>

      <b-row>
        <b-col>
          <b-form-select
            style="width: 150px"
            id="per-page-select"
            v-model="perPage"
            :options="pageOptions"
            size="sm"
          ></b-form-select>
        </b-col>
        <b-col>
          <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
          ></b-pagination>
        </b-col>
        <br />
      </b-row>
    </div>
  </b-container>
</template>

<script>
import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";
export default {
  name: "listaEstudios",

  components: {},
  props: {},

  data() {
    return {
      perPage: 30,
      sortBy: "fecha",
      sortDesc: false,
      pageOptions: [30, 10, 15, 40],
      filter: null,
      currentPage: 1,
      loading: true,
      totalRows: 1,
      fields: [
        {
          key: "paciente.nombre",
          label: "Nombre",
          class: "text-center p2",
        },
        {
          key: "paciente.apellido",
          label: "Apellido",
          class: "text-center p2",
          sortable: true,
        },
        {
          key: "medico_derivante.apellido",
          label: "Medico derivante",
          class: "text-center p2",
         
        },
        {
          key: "diagnostico.nombre",
          label: "Diagnostico",
          class: "text-center p2",
        },
        {
          key: "tipo.nombre",
          label: "Tipo Estudio",
          class: "text-center p2",
        },
        {
          key: "estados",
          label: "Estado",
          class: "text-center p2",
        },
        {
          key: "fecha",
          label: "Fecha",
          class: "text-center p2",
        },

        {
          key: "acciones",
          label: "Acciones",
          class: "text-center p2",
        },
      ],
      items: [],
    };
  },

  created() {},
  methods: {
    armarFecha(estado) {
      return new Date(estado.ultimo_estado.fecha).format("DD-MM-YYYY HH:MM");
    },
    obtenerUltimoEstado(estudio) {
      let nameEstado = estudio.ultimo_estado.resourcetype;
      nameEstado = nameEstado.replace(/([a-z])([A-Z])/g, "$1 $2");
      nameEstado = nameEstado.replace(/([A-Z])([A-Z][a-z])/g, "$1 $2");
      return nameEstado;
    },
    esUltimoEstado(estudio) {
      let ultimoEstado = estudio.ultimo_estado;
      return ultimoEstado.resourcetype == "ResultadoDeEstudioEntregado"
        ? false
        : true;
    },
    async obtenerListaEstudios() {
      try {
        let response = await EstudiosService.obtenerListaEstudios();
        this.items = this.ordenarEstudiosFecha(response.data);
      } catch (err) {
        console.log(err);
      }
    },
    ordenarEstudiosFecha(estudios){
      estudios.sort(function (a, b) {
        if (a.ultimo_estado.fecha < b.ultimo_estado.fecha) {
          return 1;
        }
        if (a.ultimo_estado.fecha > b.ultimo_estado.fecha) {
          return -1;
        }
        return 0;
      });
      return estudios;

    },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    detalleEstudio(estudio) {
      this.$router.push({
        name: "detalleDeEstudio",
        params: {
          estudioId: estudio.id,
        },
      });
    },
    siguienteEstado(estudio) {
      this.$router.push({
        name: estudio.ultimo_estado.resourcetype,
        params: {
          estudio: estudio,
        },
      });
    },
    checkComprobantePago(estudio) {
      if (estudio.ultimo_estado.resourcetype != "EsperandoComprobanteDePago") {
        return false;
      }
      let hoy = new Date();
      let fechaCreacioncomprobante = new Date(estudio.ultimo_estado.fecha);
      let difference = Math.abs(hoy - fechaCreacioncomprobante);
      let days = difference / (1000 * 3600 * 24);
      if (days > 30) {
        return true;
      }
      return false;
    },
    checkFaltaDatosMuestra(estudio) {
      if (estudio.ultimo_estado.resourcetype != "EsperandoTomaDeMuestra") {
        return false;
      }
      let hoy = new Date();
      let fechaCreacioncomprobante = new Date(
        estudio.ultimo_estado.turno.inicio
      );
      let difference = Math.abs(hoy - fechaCreacioncomprobante);
      let days = difference / (1000 * 3600 * 24);
      if (days > 30) {
        return true;
      }
      return false;
    },
    async anularEstudioFaltaDatosMuestra(estudio) {
      try {
        let datosComprobante = {
          estudio_id: estudio.id,
          expirado: true,
          resourcetype: estudio.ultimo_estado.resourcetype,
        };
        await EstudiosService.actualizarUltimoEstado(
          datosComprobante,
          estudio.ultimo_estado.id
        );
        this.$root.$bvToast.toast(
          "Usted volvio a la seleccion de turno porque no cargo los datos",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          }
        );
        this.obtenerListaEstudios();
      } catch (error) {
        this.$root.$bvToast.toast(
          "ocurrio un error mientras anulaba el estudio, por favor vuelva a intentar",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }
    },
    async anularEstudioFaltaComprobante(estudio) {
      try {
        let datosComprobante = {
          estudio_id: estudio.id,
          fecha_procesado: new Date(),
          resourcetype: estudio.ultimo_estado.resourcetype,
        };
        await EstudiosService.actualizarUltimoEstado(
          datosComprobante,
          estudio.ultimo_estado.id
        );
        this.$root.$bvToast.toast(
          "Usted anulo el estudio por que no se subio el comprobante de pago,quedo inhabilitado para poder continuar",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "success",
          }
        );
        this.obtenerListaEstudios();
      } catch (error) {
        this.$root.$bvToast.toast(
          "ocurrio un error mientras anulaba el estudio, por favor vuelva a intentar",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }
    },
  },
  mounted() {
    axios
      .all([this.obtenerListaEstudios()])
      .then(() => {
        this.totalRows = this.items.length;
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
