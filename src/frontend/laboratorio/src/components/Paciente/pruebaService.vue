<template>
    <button v-on:click="buscar">buscar</button>
</template>

<script>

import PacienteService from '@/services/PacientesService'

export default {
    name: 'Buscar',
    pops: {},
    data() {
        return {
        }
    },
    methods: {
        buscar: function() {
            PacienteService.obtenerPacientes()
        }
    }
    
}
</script>

<style>

</style>