export default {
    login(usuario, clave) {
        console.log('almacenando ' + usuario + ' y su clave')
        window.localStorage.setItem('credenciales', JSON.stringify({
            'usuario': usuario,
            'clave': clave
        }));
    },
    getApiToken() {
        let credenciales = JSON.parse(window.localStorage.getItem('credenciales'));
       
        return credenciales
    }
}