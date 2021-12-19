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
    <line-chart
      v-if="loading"
      :chartData="this.dataDemoraTiempo"
      :options="this.chartOptions"
    />
  </div>
</template>

<script>
import LineChart from "@/services/estadisticasService/LineChart.js";
import BarChart from "@/services/estadisticasService/BarChart.js";
import ReportesService from "@/services/ReportesService.js";
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
      dataDemoraTiempo: {
        labels: [    "Enero",
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
          "Diciembre",],
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
        let response = await ReportesService.obtenerEstudiosPorMesAño();
        console.log(response)
        this.armarDatos(response.data);
      } catch (error) {
        console.log(error);
      }
    },
    async obtenerEstudiosPorTipo() {
      try {
        let response = await ReportesService.obtenerEstudiosPorTipo();
        this.armarDatosTipoEstudios(response.data);
        BarChart.value.chartInstance.zoom(1.01);
      } catch (error) {
        console.log(error);
      }
    },
    async demoraEstudiosProcesamiento() {
      try {
        let response = await ReportesService.demoraEstudiosProcesamiento();
        console.log(response);
        this.armarDatosTiempo(response.data)
      } catch (error) {
        console.log(error);
      }
    },
    armarDatosTipoEstudios(data) {
      let dataTipos = [];
      for (let index = 0; index < Object.values(data).length; index++) {
        this.dataTipoEstudios.labels.push(data[index].tipo);
        dataTipos.push(data[index].cantidad);
      }
      this.dataTipoEstudios.datasets.push({
        label: "Tipos de estudio",
        backgroundColor: [
          "#77CEFF",
          "#0079AF",
          "#123E6B",
          "#97B0C4",
          "#A5C8ED",
        ],
        data: dataTipos,
      });
    },
    armarDatosTiempo(datos) {    
      console.log( datos.datos[12].procesados)
      let data = [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, datos.datos[12].tardanza_segundos];

      this.dataDemoraTiempo.datasets.push({
        label: "Tiempo demora estudios",
        backgroundColor: " 	#6495ED ",
        data: data
      });
    },

    armarDatos(datos) {
      console.log(datos)
      let data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      datos.forEach((e) => {
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
      .all([
        this.obtenerEstudiosPorMesAño(),
        this.obtenerEstudiosPorTipo(),
        this.demoraEstudiosProcesamiento(),
      ])
      .then(() => {
        this.loading = true;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>