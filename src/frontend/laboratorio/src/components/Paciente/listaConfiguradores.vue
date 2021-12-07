<template>
  <b-container >
    <div v-if="loading">
      <b-spinner> </b-spinner>

      <h4>Listado de Configuradores</h4>
    </div>
    <div v-else>
      <b-col lg="4" class="my-1">
        <b-input-group size="sm">
          <b-form-input
            id="filter-input"
            v-model="filter"
            type="search"
            placeholder="Buscar por nombre "
          ></b-form-input>

          <b-input-group-append>
            <b-button :disabled="!filter" @click="filter = ''">Buscar</b-button>
          </b-input-group-append>
        </b-input-group>
      </b-col>
      <b-table
      show-empty
        empty-text="Todavia no hay usuarios configuradores"
        :items="items"
        :fields="fields"
        :filter="filter"
        :current-page="currentPage"
        :per-page="perPage"
        @filtered="onFiltered"
      >
        
        <template v-slot:cell(acciones)="row">        
          <b-button
            @click="editar(row.item)"
            variant="outline-success"
            title="Editar"
          >
            <b-icon
              icon="arrow-repeat"
              variant="success"
            >
            </b-icon>
          </b-button>
          <b-button
            @click="siguienteEstado(row.item)"
            variant="outline-danger"
            title="Eliminar"
          >
            <b-icon icon="trash" variant="danger"> </b-icon>
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
import PacientesService from "@/services/PacientesService.js";
import axios from "axios";
export default {
  name: "PacientesService",

  components: {},
  props: {},

  data() {
    return {
      perPage: 10,
      pageOptions: [4, 10, 15],
      filter: null,
      currentPage: 1,
      loading: true,
      totalRows: 1,
      fields: [
        { key: "nombre", label: "Nombre", class: "text-center p2" },
           {
          key: "apellido",
          label: "Apellido",
          class: "text-center p2",
        },
        {
          key: "usuario",
          label: "Usuario",
          class: "text-center p2",
        },
     
     
        { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
      items: [],
    };
  },

  created() {},
  methods: {
    async siguienteEstado(configurado){
        console.log(configurado)
        try {
        let response = await PacientesService.deleteConfigurador(configurado);
       this.$root.$bvToast.toast("Se elimino el configurador", {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "success",
            });
        console.log(response)
        this.obtenerConfiguradores()
     
      } catch (err) {
        console.log(err);
           this.$root.$bvToast.toast("No se pudo eliminar ", {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "danger",
            });
      }

    },
    async obtenerConfiguradores() {
      try {
        let response = await PacientesService.obtenerConfiguradores();
        this.items = response.data; 
        console.log(this.items)
     
      } catch (err) {
        console.log(err);
      }
    },
     editar(configurador) {
      this.$router.push({
        name: "configuradores",
        params: {
          configurador: configurador,
          editar: true,
        },
      });
    },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    detalleEstudio(estudio) {
      console.log(estudio);
      this.$router.push({
        name: "configuradores",
        params: {
          estudio: estudio,
        },
      });
    },   
  },
  mounted() {
    axios
      .all([this.obtenerConfiguradores()])
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