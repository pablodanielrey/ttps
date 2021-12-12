<template>
  <div class="container">
    <line-chart
      v-if="loading"
      :chartData="this.datacollection"
      :options="this.chartOptions"
    />
    <bar-chart
      v-if="loading"
      :chartData="this.dataTipoEstudios"
      :options="this.chartOptions"
    />
  </div>
</template>

<script>
import LineChart from "@/services/estadisticasService/LineChart.js";
import BarChart from "@/services/estadisticasService/BarChart.js";
import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";

export default {
  name: "LineChartContainer",
  components: { LineChart, BarChart },
  data() {
    return {
      loading: false,
      datacollection: {
        labels: [
          "Enero",
          "Febrero",
          "Marzo",
          "Abril",
          "Mayo",
          "Junio",
          "Julio",
          "Agosto",
          "Septiembre",
          "Octubre",
          "Noviembre",
          "Diciembre",
        ],
        datasets: [],
      },
      dataTipoEstudios: {
        labels: [],
        datasets: [],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  methods: {
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    },
    async obtenerEstudiosPorMesAño() {
      try {
        let response = await EstudiosService.obtenerEstudiosPorMesAño();
        this.armarDatos(response.data);
      } catch (error) {
        console.log(error);
      }
    },
    async obtenerEstudiosPorTipo() {
      try {
        let response = await EstudiosService.obtenerEstudiosPorTipo();
        this.armarDatosTipoEstudios(response.data.Estudios);
      } catch (error) {
        console.log(error);
      }
    },
    armarDatosTipoEstudios(data) {      
      let dataTipos=[]      
      for (let index = 0; index < Object.values(data).length; index++) {
        this.dataTipoEstudios.labels.push(data[index].tipo);
        dataTipos.push(data[index].cantidad)        
      }
       this.dataTipoEstudios.datasets.push({
        label: "Tipos de estudio",
        backgroundColor:  [
            "#77CEFF",
            "#0079AF",
            "#123E6B",
            "#97B0C4",
            "#A5C8ED",
          ],
        data: dataTipos,
      });
    },

    armarDatos(datos) {
      let data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      datos.Estudios.forEach((e) => {
        data[e.month - 1] = e.count;
      });
      this.datacollection.datasets.push({
        label: "Estudios en el año",
        backgroundColor: " 	#6495ED ",
        data: data,
      });
    },
  },
  mounted() {
    axios
      .all([this.obtenerEstudiosPorMesAño(), this.obtenerEstudiosPorTipo()])
      .then(() => {
        this.loading = true;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>