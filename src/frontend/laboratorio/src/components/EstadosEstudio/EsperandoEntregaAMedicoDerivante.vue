<template>
  <b-container>
    <h3>Descargar resultado para enviarle al medico derivante</h3>
    <b-button
      title="Enviado a medico derivante"
      variant="outline-success"
      @click="bajarInforme()"
    >
      <b-icon icon="share" aria-hidden="true"></b-icon
    ></b-button>
  </b-container>
</template>

<script>
import { jsPDF } from "jspdf";
/*  
import EstudiosService from "@/services/EstudiosService.js";
 */
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
  created() {},
  methods: {
    async bajarInforme() {
      /*     try {
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
        } */
      console.log(this.estudio);
      const doc = new jsPDF({});
      doc.text(
        "Estudio del paciente  " + this.estudio.paciente.apellido +' '+ this.estudio.paciente.nombre,
        30,
        20
      );
      doc.addFont("bromellonavidadregular", "bromellonavidadregular", "normal");
      doc.setFont("bromellonavidadregular");
      doc.setFontSize(13);
            doc.text("Dni:  " + this.estudio.paciente.dni, 40, 30);

      doc.text("Tipo de estudio:  " + this.estudio.tipo.nombre, 40, 50);
      
      doc.text("Diagnostico:  " + this.estudio.diagnostico.nombre, 40, 60);
      doc.text("Resultado:  " + this.estudio.diagnostico.nombre, 40,70);

      doc.save("InformeDelEstudio.pdf");
    },
  },
  computed: {},
  mounted() {},
};
</script>

<style>
</style>