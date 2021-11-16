<template>
  <div>
  <b-navbar type="dark" variant="dark">
    <b-navbar-nav>
      <b-nav-item :to="{ name: '' }">Home</b-nav-item>
      <b-nav-item-dropdown text="Pacientes" right>
        <b-dropdown-item  :to="{ name: 'listaPacientes' }">Listar</b-dropdown-item>
        <b-dropdown-item :to="{ name: 'paciente' }">nuevo</b-dropdown-item>      
      </b-nav-item-dropdown>

      <b-nav-item-dropdown text="Estudios" right>
        <b-dropdown-item :to="{ name: 'listaEstudios' }">Listar</b-dropdown-item>
        <b-dropdown-item :to="{ name: 'nuevoEstudio' }">Nuevo</b-dropdown-item>
      </b-nav-item-dropdown>
  
     <b-nav-item-dropdown text="Lotes" right>
        <b-dropdown-item :to="{ name: 'cargarResultadoLote' }">Listar</b-dropdown-item>
        <b-dropdown-item :to="{ name: 'crearLote' }">Nuevo</b-dropdown-item>
      </b-nav-item-dropdown>
          <b-nav-item-dropdown text="Turnos ocupados" right>
        <b-dropdown-item :to="{ name: 'turnosOcupados' }">Listar</b-dropdown-item>
      </b-nav-item-dropdown>
      
    </b-navbar-nav>
  </b-navbar>
  <br>
</div>
</template>

<script>
export default {

}
</script>

<style>

</style>