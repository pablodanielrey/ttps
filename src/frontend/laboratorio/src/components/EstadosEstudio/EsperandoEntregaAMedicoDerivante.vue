<template>
  <b-container>
    <div>
      <h3>Descargar resultado para enviarle al medico derivante</h3>
      <div>
        <b-button
          title="Enviado a medico derivante"
          variant="outline-success"
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
    </div>
    {{this.estudio}}
  </b-container>
</template>

<script>
import jsPDF from "jspdf"; 
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
    async obtenerDetalleEstudio() {
      try {
        let response = await EstudiosService.obtenerEstudio(this.estudioId);
        console.log(response);
        this.estudio = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async obtenerDetalleEstados() {
      try {
        let response = await EstudiosService.obtenerEstudio(this.estudioId);
        console.log(response);
        this.estudio = response.data;
      } catch (error) {
        console.log(error);
      }
    },
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
      let pdfName = 'informeEstudio'; 
      var doc = new jsPDF();
      doc.text("Informe de estudio:", 10, 10);
      doc.text("Paciente  " + this.estudio.paciente.apellido +' '+ this.estudio.paciente.nombre, 30, 20);
      //doc.text("Dni:  " + this.estudio.paciente.dni, 40, 30);
      doc.text("Diagnostico previo:  " + this.estudio.diagnostico.nombre, 40, 50);
      doc.text("Medico Derivante:  " + this.estudio.medico_derivante.apellido +' '+ this.estudio.medico_derivante.nombre +' lic: '+ this.estudio.medico_derivante.licencia,40, 60);
      doc.text("Tipo de estudio:  " + this.estudio.tipo.nombre, 40, 70);
      //doc.text("Medico Informante:  " + this.estudio.medico_informante.nombre, 40, 70);
      //fecha de elaboracion deinforme
      //resultado
      // descripcion resultado
      //doc.text("Resultado:  " + this.estudio.diagnostico.nombre, 40,70);
      doc.save(pdfName + ".pdf");
    },
  },
  async siguienteEstado() {
    try {
      let datosConsentimiento = {
        estudio_id: this.estudio.id,
        fecha_enviado: new Date(),
      };       
      let response = await EstudiosService.actualizarUltimoEstado(
        datosConsentimiento
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
  computed: {},
  mounted() {
  },
};
</script>

<style>
</style>