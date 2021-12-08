<template>
  <div class="container">
    <line-chart
      v-if="loading"
      :chartData="this.datacollection"
      :options="this.chartOptions"
    />
  </div>
</template>

<script>
import LineChart from "@/services/estadisticasService/LineChart.js";
import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";

export default {
  name: "LineChartContainer",
  components: { LineChart },
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
      chartOptions: {
       responsive: true, maintainAspectRatio: false
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
    armarDatos(datos) {
      console.log("datacollection", this.datacollection);
      let data = [0,0,0,0,0,0,0,0,0,0,0];
      datos.Estudios.forEach((e) => {
          console.log(e.count)
        data[e.month-1]=e.count;
      });
      console.log(data);
      this.datacollection.datasets.push({         
          label: 'Estudios en el año',
          backgroundColor: ' 	#6495ED ',
          data:data
       
      })



    },
  },
  mounted() {
    axios
      .all([this.obtenerEstudiosPorMesAño()])
      .then(() => {
        this.loading = true;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>