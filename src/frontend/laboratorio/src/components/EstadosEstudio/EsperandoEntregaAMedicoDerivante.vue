<template>
  <b-container>
      <h3> Descargar resultado para enviarle al medico derivante</h3>
  </b-container>
</template>

<script>

import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";
import PacientesService from "@/services/PacientesService.js";
export default {
  components: {  },
  props: {
    estudio: {
      type: Object,
    },
  },
  data() {
    return {
      medicosInformantes: [],
      loading: true,
      retiro: null,
      urlRestultado: null,
      alerts: [],
      resultado: {
        resultado: null,
        medico_informante: null,
        fecha_informe: new Date().format("YYYY-MM-DD"),
        informe: null,
      },
    };
  },
  created() {},
  methods: {
    async obtenerMedicosInformantes() {
      try {
        const response = await PacientesService.obtenerMedicosInformantes();
        this.medicosInformantes = response.data;
        console.log(this.medicosInformantes);
      } catch (err) {
        console.log(err);
      }
    },
    async guardarDatos() {
      try {
        let result = await this.$refs.detailsResultado.validate();
        if (result) {
         
          let datos = {
            estudio_id: this.estudio.id,
            fecha_informe: new Date(this.resultado.fecha_informe),
            medico_informante: this.resultado.medico_informante,
            resultado: this.resultado.resultado,
            informe: this.resultado.informe,
          };
           console.log(datos)
          let response= await EstudiosService.actualizarUltimoEstado(datos);
          console.log(response)
          this.$root.$bvToast.toast(
            "Se guardo de forma correcta el resultado del informe",
            {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "success",
            }
          );
          this.$router.push({
            name: "listaEstudiosEsperandoInforme",
          });
        }
      } catch (error) {
        console.log(error)
        this.$root.$bvToast.toast(
          "ocurrio un error mientras guardaba los resultados " + error.response,
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
  computed: {
    getMedicosInformantes() {
      let medicos = this.medicosInformantes.map((e) => ({
        value: e.id,
        text: e.nombre,
      }));
      medicos.push({
        value: null,
        text: "-Seleccione un medico -",
        disabled: true,
      });
      return medicos;
    },
  },
  mounted() {
    axios
      .all([this.obtenerMedicosInformantes()])
      .then(() => {
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