<template>
<b-container>
    <br />
    <h4>Listado de Lotes</h4>

    <b-table striped hover :items="items"></b-table>

</b-container>
</template>

<script>
import LotesService from "@/services/LotesService.js";
import axios from "axios";
export default {
    name: "CargarResultadoLote",

    components: {},
    props: {},

    data() {
        return {
            items: [],
        };
    },

    created() {
        console.log(this.paciente);
    },

    methods: {
        formatear_lista(e) {
            return {
              id: e.id,
              numero: e.numero,
              estudios: e.estudios.reduce((a,) => 1+a, 0)
            };
        },
        async obtenerLotes() {
            try {
                let response = await LotesService.obtenerLotes();
                console.log(response);
                this.items = response.map(this.formatear_lista)
                console.log(this.items);
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
