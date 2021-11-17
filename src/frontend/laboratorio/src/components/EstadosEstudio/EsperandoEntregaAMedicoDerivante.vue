<template>
  <b-container>
    <h3>Descargar resultado para enviarle al medico derivante</h3>
    <b-button title="Enviado a medico derivante" variant="outline-success" @click="bajarInforme()">
      <b-icon icon="share" aria-hidden="true"></b-icon
    ></b-button>
  </b-container>
</template>

<script>
/* import { jsPDF } from "jspdf";
 */
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
        fecha_entrega:new Date()
    };
  },
  created() {},
  methods: {
    async bajarInforme() {
        try {
          let datos={
              fecha_entrega:this.fecha_entrega,
              estudio_id:this.estudio.id
          }
          let response = await EstudiosService.actualizarUltimoEstado(
            datos
          );          
            this.$root.$bvToast.toast("se envio al medico derivante", {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "success",
            });
            this.$router.push({
              name: "listaEstudios",
            });
          
          console.log(response);
        } catch (err) {
          console.log(err);
          this.$root.$bvToast.toast(
            "ocurrio un error mientras se enviaba al medico derivante",
            {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "danger",
            }
          );
        }

   /*    const doc = new jsPDF({
       
      });
      doc.text("Estudio del paciente  "+this.estudio.paciente.apellido, 30, 10);
      doc.text("Resultado!"+this.estudio., 40, 10);
      doc.save("InformeDelEstudio.pdf"); */
    },
  },
  computed: {},
  mounted() {},
};
</script>

<style>
</style>