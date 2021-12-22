<template>
  <b-container>
    <br />
    <h4>Listado de Estudios esperando interpretacion de resultados e informes</h4>

    <b-col lg="4" class="my-1">
      <b-input-group size="sm">
        <b-form-input
          id="filter-input"
          v-model="filter"
          type="search"
          placeholder="Buscar en el listado"
        ></b-form-input>

        <b-input-group-append>
          <b-button :disabled="!filter" @click="filter = ''">Buscar</b-button>
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
      <template v-slot:cell(acciones)>
      
          <b-button
            title="Descargar Presupuesto"
            variant="outline-primary"
            
            @click="cargarResultado"
          >
            Ingresar Resultado
          </b-button>
          <!-- <b-button @click="seleccionTurno(row.item.id)">
            seleccionar turno
          </b-button> -->

      </template>
    </b-table>

    <b-row>
      <b-col md="1">
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


                <b-modal 
          size="xl"
            ref="modalResultado" 
            title="Cargar resultados del Estudio" 
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
import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";
import { VueEditor } from "vue2-editor";
export default {
  name: "ListaPacientes",

  components: {VueEditor},
  props: {},

  data() {
    return {
      perPage: 4,
      pageOptions: [4, 10, 15],
      filter: null,
      currentPage: 1,
      totalRows: 1,
      fields: [
        { key: "paciente.nombre", label: "Nombre", class: "text-center p2" },
          { key: "paciente.apellido", label: "Apellido", class: "text-center p2" },
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
        { key: "tipo.nombre", label: "Tipo Estudio", class: "text-center p2" },
        
        { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
      items: [],
    };
  },


  methods: {
    async obtenerListaEstudios() {
      try {
        let response = await EstudiosService.obtenerListaEstudios();
        this.items = response.data;
      } catch (err) {
        console.log(err);
      }
    },
     cargarResultado(){
                   this.$refs["modalResultado"].show();
        },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    seleccionTurno(estudio) {
      this.$router.push({
        name: "seleccionTurno",
        params: { estudio: estudio },
      });
    },
  },
  mounted() {
    axios
      .all([this.obtenerListaEstudios()])
      .then(() => {
        this.totalRows = this.items.length;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>


<style>
</style>