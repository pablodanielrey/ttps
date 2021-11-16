<template>
<b-container>
    <br />
  
 <b-card header=" Listado de Lotes">
    <b-table striped hover :items="items" :fields="fields">
          <template v-slot:cell(acciones)="item">
      
          <b-button
            title="Ver estudios"
            variant="outline-primary"
            @click="verEstudios(item.item)"
          >
           Estudios
          </b-button>
             <b-button
            title="URL"
            variant="outline-success"
               @click="cargarResultado()"
          >
           Cargar Resultado
          </b-button>
          <!-- <b-button @click="seleccionTurno(row.item.id)">
            seleccionar turno
          </b-button> -->

      </template>
    </b-table>
    <div>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
        ></b-pagination>
      </b-col>
      </b-row>
    </div>
 </b-card>
     <b-modal 
     size="xl"
      ref="my-modal" 
      title="Estudios del lote 1" 
      ok-only     
      >
         <b-table
      :items="itemsEst"
      :fields="fieldsEst"
   
    >   

    </b-table>

          
      </b-modal>
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
import LotesService from "@/services/LotesService.js";
import axios from "axios";
import { VueEditor } from "vue2-editor";


export default {
    name: "CargarResultadoLote",

 components: { VueEditor },
    props: {},

    data() {

        return {
          alerts:[],
              perPage: 4,
              itemsEst: [],
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
     
    },

    methods: {
        verEstudios(item){
            console.log(item)
            this.itemsEst=item.estudios
                  this.$refs["my-modal"].show();
        },
        cargarResultado(){
                   this.$refs["modalResultado"].show();
        },
        formatear_lista(e) {
            return {
              id: e.id,
              numero: e.numero,
              fecha:e.fecha,
              estudios: e.estudios.reduce((a,) => 1+a, 0)
            };
        },
        async obtenerLotes() {
            try {
                let response = await LotesService.obtenerLotes();
                console.log(response);
                this.items = response
  
            } catch (err) {
                console.log(err);
            }
        }
    },

    computed: {

    },

    mounted() {
        axios
            .all([this.obtenerLotes()])
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
