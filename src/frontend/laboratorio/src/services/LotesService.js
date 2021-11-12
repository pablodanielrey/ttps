import Api from "@/services/Api"

const API_URL = '/lotes_api/'

export default {
    obtenerEstudios() {
        return Api().get(API_URL + "estudios/")
    },

    obtenerLotes() {
        // return Api().get(API_URL + 'lotes/')
        return new Promise((r,) => {
            r([
                {
                    'id': '1',
                    'numero': 1,
                    'fecha': '04-04-2021',
                    'estudios': [
                        {
                            'nombre': "Hernandez Juan",
                            'medico_derivante':"Cote Patricio",
                            'tipo':'Genoma mitocondrial completo',
                            'id': 'sadsddsfsd',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Perez Juan",
                            'medico_derivante':"Lopez Patricio",
                            'tipo':'Genoma mitocondrial completo',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Ponce Juliana",
                            'medico_derivante':"Cote Patricio",
                            'tipo':'Carrier de enfermedades monogénicas recesivas',

                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Nicolas Pereyra",
                            'medico_derivante':"Cote Patricio",
                            'tipo':'Genoma mitocondrial',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Simonetti Juan",
                            'medico_derivante':"Cote Patricio",
                            'tipo':'Genoma mitocondrial completo',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Hernandez Juan",
                            'medico_derivante':"Cote Patricio",
                            'tipo':'Genoma mitocondrial completo',
                            'fecha_alta': new Date()
                            
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Heraldez Juan",
                            'medico_derivante':"Cote Patricio",
                            'tipo':'Genoma mitocondrial completo',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Diaz Juan",
                            'medico_derivante':"Cote Patricio",
                            'tipo':'Genoma mitocondrial completo',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Hernandez Juan",
                            'medico_derivante':"Cote Patricio",
                            'tipo':'Genoma mitocondrial completo',
                            'fecha_alta': new Date()
                        },
                        {
                            'id': 'sadsddsfsd',
                            'nombre': "Hernandez Juan",
                            'medico_derivante':"Joselo Fernadez",
                            'tipo':'Genoma mitocondrial completo',
                            'fecha_alta': new Date()
                        }
                    ]
                },
                {
                    'id': '2',
                    'numero': 3,
                    'fecha': '15-05-2021',
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
                    'id': '3',
                    'numero': 3,
                    'fecha': '11-09-2021',
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
                    'id': '4',
                    'numero': 4,
                    'fecha': '04-10-2021',
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
                    'id': '7',
                    'numero': 7,
                    'fecha': '10-10-2021',
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
                    'id': '10',
                    'numero': 6,
                    'fecha': '10-11-2021',
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


            ]);
        });
    }
  
    
}