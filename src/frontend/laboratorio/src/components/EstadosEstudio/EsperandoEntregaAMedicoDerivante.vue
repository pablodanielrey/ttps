<template>
  <b-container>
    <div>
      <b-card header="Estudio esperando ser entregado al medico derivante">
      <div>
        <b-button
          title="Descargar para enviar a medico derivante"
          variant="outline-info"
          @click="bajarInforme()"
        >
          <b-icon icon="share" aria-hidden="true"></b-icon
        ></b-button>
      </div>
      <br/>
      <div>
        <b-button variant="success" @click="siguienteEstado()"
          > Finalizar estudio
        </b-button>
      </div>
      </b-card>
    </div>

  </b-container>
</template>

<script>

import EstudiosService from "@/services/EstudiosService.js";

export default {
  components: {},
  props: {
    estudio: {
      type: Object,
    },
  },
  data() {
    return {
      fecha_entrega: new Date(),
    };
  }, 
  created() {
    console.log(this.estudio)
  },
  methods: {  
    async bajarInforme() {
      console.log(this.estudio);     
    },
    async siguienteEstado() {
      try {
        let datosFinales = {
          estudio_id: this.estudio.id,
          resourcetype: this.estudio.ultimo_estado.resourcetype,
          fecha_enviado: new Date(),
        };       
        let response = await EstudiosService.actualizarUltimoEstado(
          datosFinales,
          this.estudio.ultimo_estado.id
        );
        console.log(response);
        this.$router.push({
          name: "listaEstudios",
        });
      } catch (error) {
        console.log(error);
        this.$root.$bvToast.toast(
          "ocurrio un error mientras continuaba ",
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
  computed: {},
  mounted() {
  },
};
</script>

<style>
</style>