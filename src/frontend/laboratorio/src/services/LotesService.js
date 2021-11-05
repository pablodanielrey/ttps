import Api from "@/services/Api"

const API_URL = '/lotes_api/'

export default {
    obtenerEstudios() {
        return Api().get(API_URL + "estudios/")
        // return new Promise(() => {
        //     return {

        //     };
        // })
    },

    obtenerLotes() {
        // return Api().get(API_URL + 'lotes/')
        return new Promise((r,) => {
            r([
                {
                    'id': 'sdfdfdsfds',
                    'numero': 1234,
                    'estudios': [
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        }
                    ]
                },
                {
                    'id': '34ff3f',
                    'numero': 1234,
                    'estudios': [
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        }
                    ]
                },
                {
                    'id': 'sdfdf43543f34gh34gdsfds',
                    'numero': 1234,
                    'estudios': [
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        }
                    ]
                }


            ]);
        });
    }
  
    
}