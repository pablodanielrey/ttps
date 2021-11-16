from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import logging
import datetime
from zoneinfo import ZoneInfo

from estudios import models as estudio_models
from personas import models as persona_models
from turnos import models as turnos_models


def generar_fecha_now():
    return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))

def generar_parametros_de_turnos_por_defecto():

    turnos_models.ParametroDeTurnos.objects.all().delete()

    # inicializo los parámetros de los turnos a una semana antes como ejemplo.
    hoy = datetime.datetime.combine(datetime.date.today(), datetime.time(0)).replace(tzinfo=ZoneInfo('America/Argentina/Buenos_Aires'))
    hace_una_semana = hoy - datetime.timedelta(days=7)

    rangos_de_prueba = [
        {
            'fecha': hace_una_semana,
            'frecuencia': 15,
            'rangos': [(7,12),(14,19)]
        }
    ]


    for r in rangos_de_prueba:
        fecha_valido = r['fecha']
        frecuencia = r['frecuencia']
        pt = turnos_models.ParametroDeTurnos(fecha_valido=fecha_valido)
        pt.save()
        for rinicio, rfin in r['rangos']:
            logging.debug(f'generando rango a partir de : {fecha_valido} de : {rinicio} hasta: {rfin} con la frecuencia: {frecuencia}')
            r = turnos_models.RangoDeTurnos(parametros=pt, hora_inicio=rinicio, hora_fin=rfin, frecuencia=frecuencia)
            r.save()



def generar_fechas_feriados():
    turnos_models.FechasSinTurno.objects.all().delete()
    for feriado in [datetime.date(2021,10,28), datetime.date(2021,11,1), datetime.date(2021,11,3)]:
        turnos_models.FechasSinTurno(fecha=feriado).save()



def generar_lote():
    from personas import models as persona_models

    empleado = persona_models.Persona.objects.all().first()

    tipoe = estudio_models.TiposDeEstudio.objects.all().first()
    diagnostico = estudio_models.Diagnostico.objects.all().first()

    for _ in range(0,20):
        estudio = estudio_models.Estudio(paciente=empleado,  tipo=tipoe, medico_derivante=empleado, diagnostico=diagnostico)
        estudio.save()

        estudio_models.EsperandoRetiroDeExtaccion(persona=empleado, estudio=estudio, extracionista='pepe se la lleva a la muestra', fecha_retiro=generar_fecha_now()).save()
        estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(estudio=estudio, persona=empleado).save()


def generar_estudio_de_muestra():

    empleado = persona_models.Persona.objects.all().first()

    p1 = persona_models.Persona(nombre='Paciente', apellido='Cero', dni='000001', email='paciente@cero.com', telefono='221-1112233', fecha_nacimiento='1980-12-01')
    p1.save()
    mm = persona_models.Persona(nombre='Medi', apellido='Cote', dni='2212211', email='m@hotmail.com', telefono='221-1112233', fecha_nacimiento='1995-06-02')
    mm.save()

    ob_social = persona_models.ObraSocial.objects.all().first()
    obp = persona_models.ObraSocialPersona(persona=p1, obra_social=ob_social, numero_afiliado='afiliate12345')
    obp.save()

    tipoe = estudio_models.TiposDeEstudio.objects.all().first()
    diagnostico = estudio_models.Diagnostico.objects.all().first()
    estudio = estudio_models.Estudio(paciente=p1,  tipo=tipoe, medico_derivante=mm, diagnostico=diagnostico)
    estudio.save()


    estudio_models.EsperandoRetiroDeExtaccion(persona=empleado, estudio=estudio, extracionista='pepe se la lleva a la muestra', fecha_retiro=generar_fecha_now()).save()
    estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(estudio=estudio, persona=empleado).save()
    


    # #estudio_models.EsperandoPresupuesto(persona=empleado, estudio=estudio, presupuesto=10.3).save()
    # #estudio_models.EsperandoFactura(persona=empleado, estudio=estudio, numero='dsaasd324324', monto=10.5).save()
    # #estudio_models.EsperandoFactura(persona=empleado, estudio=estudio, numero='dsaasd324325', monto=11.5, obra_social=ob_social).save()
    # estudio_models.EsperandoComprobanteDePago(persona=empleado, estudio=estudio, comprobante='base64-del-comprobante').save()
    # estudio_models.AnuladorPorFaltaDePago(persona=empleado, estudio=estudio).save()


    # tipoe = estudio_models.TiposDeEstudio.objects.all().first()
    # diagnostico = estudio_models.Diagnostico.objects.all().first()
    # estudio = estudio_models.Estudio(paciente=p1,  tipo=tipoe, medico_derivante=mm, diagnostico=diagnostico)
    # estudio.save()

    # #estudio_models.EsperandoPresupuesto(persona=empleado, estudio=estudio, presupuesto=10.3).save()
    # #estudio_models.EsperandoFactura(persona=empleado, estudio=estudio, numero='dsaasd324325', monto=11.5, obra_social=ob_social).save()
    # estudio_models.EsperandoComprobanteDePago(persona=empleado, estudio=estudio, comprobante='base64-del-comprobante').save()
    # estudio_models.EsperandoConsentimientoInformado(persona=empleado, estudio=estudio, consentimiento='base64-del-consntimiento').save()

    # #estudio_models.EsperandoSeleccionDeTurnoParaExtraccion(persona=empleado, estudio=estudio, turno=generar_fecha_now()).save()
    # estudio_models.EsperandoTomaDeMuestra(persona=empleado, estudio=estudio, expirado=True).save()
    
    # #estudio_models.EsperandoSeleccionDeTurnoParaExtraccion(persona=empleado, estudio=estudio, turno=generar_fecha_now()).save()
    # estudio_models.EsperandoTomaDeMuestra(persona=empleado, estudio=estudio, fecha_muestra=generar_fecha_now(), mililitros=145, freezer=10, expirado=False).save()
    # estudio_models.EsperandoRetiroDeExtaccion(persona=empleado, estudio=estudio, extracionista='pepe se la lleva a la muestra', fecha_retiro=generar_fecha_now()).save()
    
    # estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(persona=empleado, estudio=estudio,numero_lote='2ef').save()
    # estudio_models.EsperandoProcesamientoDeLoteBiotecnologico(persona=empleado, estudio=estudio, resultado_url='https://www.google.com/informe.pdf', fecha_resultado=generar_fecha_now()).save()
    # estudio_models.EsperandoInterpretacionDeResultados(persona=empleado, estudio=estudio, fecha_informe=generar_fecha_now(), medico_informante=mm, informe='estas recontra bien. andate de vacaciones').save()
    # estudio_models.EsperandoEntregaAMedicoDerivante(persona=empleado, estudio=estudio, fecha_entrega=generar_fecha_now()).save()


class InitSite(APIView):
    
    permission_classes= [permissions.IsAdminUser]

    def get(self, request, format=None):


        """
            aca genero todos los datos del modelo necesarios para que el sistema esté inicializado
        """
        logging.debug('inicializando sistema')


        patologias = [
            "Acidez de estómago",
            "Acné",
            "Acúfenos",
            "Adenoma hipofisiario",
            "Aerofagia",
            "Aftas bucales",
            "Agorafobia",
            "Alergia",
            "Alergia al látex",
            "Alergia al polen",
            "Alergias alimentarias",
            "Alopecia",
            "Alzheimer",
            "Amenorrea",
            "Amigdalitis",
            "Anemia",
            "Aneurisma de aorta",
            "Angina de pecho",
            "Anisakiasis",
            "Anorexia",
            "Ansiedad",
            "Apendicitis",
            "Apnea del sueño",
            "Arritmias",
            "Arterioesclerosis",
            "Artritis reumatoide",
            "Artrosis",
            "Asbestosis",
            "Asma",
            "Astigmatismo",
            "Ataxia",
            "Ateroesclerosis",
            "Autismo",
            "Balanitis",
            "Bartolinitis",
            "Botulismo",
            "Bradicardia",
            "Bronquiectasias",
            "Bronquitis",
            "Brucelosis",
            "Bruxismo",
            "Bulimia",
            "Bullying",
            "Bursitis",
            "Callos",
            "Cáncer de cabeza y cuello",
            "Cáncer de colon",
            "Cáncer de cuello de útero",
            "Cáncer de endometrio",
            "Cáncer de estómago",
            "Cáncer de faringe",
            "Cáncer de intestino delgado",
            "Cáncer de laringe",
            "Cáncer de las vías biliares",
            "Cáncer de mama",
            "Cáncer de ovario",
            "Cáncer de páncreas",
            "Cáncer de piel",
            "Cáncer de próstata",
            "Cáncer de pulmón",
            "Cáncer de riñón",
            "Cáncer de testículo",
            "Cáncer de tiroides",
            "Cáncer de uretra",
            "Cáncer de vejiga",
            "Candidiasis",
            "Cardiopatías congénitas",
            "Cataratas",
            "Celiaquía",
            "Cervicitis",
            "Chikungunya",
            "Ciática",
            "Cirrosis",
            "Citomegalovirus",
            "Colecistitis",
            "Colelitiasis",
            "Cólera",
            "Cólico del lactante",
            "Cólico nefrítico",
            "Colitis ulcerosa",
            "Colon irritable",
            "Conjuntivitis",
            "Coronavirus",
            "Corte de digestión o hidrocución",
            "Creutzfeldt jakob (Vacas locas)",
            "Degeneración macular asociada a la edad (DMAE)",
            "Demencia",
            "Demencia con cuerpos de Lewy",
            "Dengue",
            "Depresión",
            "Dermatitis atópica",
            "Dermatitis del pañal",
            "Dermatitis seborreica",
            "Derrame pleural",
            "Desprendimiento de retina",
            "Diabetes",
            "Diarrea",
            "Diarrea del viajero",
            "Difteria",
            "Disfunción sexual femenina",
            "Dislexia",
            "Dismenorrea",
            "Dismorfofobia",
            "Dispepsia",
            "Diverticulitis",
            "Dolor de cabeza o cefalea",
            "Eccema",
            "Edema Pulmonar",
            "ELA (esclerosis lateral amiotrófica)",
            "Embolia pulmonar",
            "Encefalitis",
            "Encefalopatía hepática",
            "Endocarditis",
            "Endometriosis",
            "Enfermedad de Crohn",
            "Enfermedad de Kawasaki",
            "Enfermedad de Paget",
            "Enfermedad de Whipple",
            "Enfermedad de Wilson",
            "Enfermedad del sueño",
            "Enfermedad por virus de Marburgo",
            "Enfermedad renal crónica",
            "Enfermedad tromboembólica venosa",
            "Enfisema",
            "Enuresis",
            "Epilepsia",
            "EPOC (enfermedad pulmonar obstructiva crónica)",
            "Escarlatina",
            "Esclerodermia",
            "Esclerosis múltiple",
            "Escoliosis",
            "Esofagitis",
            "Esofagitis eosinofílica",
            "Esófago de Barret",
            "Espina bífida",
            "Espolón calcáneo",
            "Espondilitis anquilosante",
            "Esquizofrenia",
            "Esterilidad e infertilidad",
            "Estrabismo",
            "Estreñimiento",
            "Estrés",
            "Factores de riesgo cardiovascular",
            "Faringitis",
            "Faringoamigdalitis",
            "Fascitis plantar",
            "Fenilcetonuria",
            "Fibromialgia",
            "Fibrosis pulmonar",
            "Fibrosis pulmonar idiopática",
            "Fibrosis Quística",
            "Fiebre amarilla",
            "Fiebre del heno",
            "Fiebre tifoidea",
            "Fiebres hemorrágicas",
            "Fimosis",
            "Fobia social",
            "Gases y flatulencias",
            "Gastritis",
            "Gastroenteritis",
            "Glaucoma",
            "Golpe de calor",
            "Gonorrea",
            "Gota",
            "Gripe",
            "Hafefobia",
            "Halitosis",
            "Hematoma subdural",
            "Hemocromatosis",
            "Hemofilia",
            "Hemorragias ginecológicas",
            "Hemorroides",
            "Hepatitis A",
            "Hepatitis B",
            "Hepatitis C",
            "Hernia discal",
            "Hernia inguinal",
            "Herpes labial",
            "Herpes zóster",
            "Hidradenitis supurativa",
            "Hidrocele",
            "Hipercolesterolemia",
            "Hipercolesterolemia familiar",
            "Hiperhidrosis",
            "Hipermenorrea",
            "Hipermetropía",
            "Hiperplasia benigna de próstata",
            "Hipertensión arterial",
            "Hipertiroidismo",
            "Hipoglucemia",
            "Hipotensión",
            "Hipotiroidismo",
            "Hirsutismo",
            "Hongos",
            "Ictus",
            "Impétigo",
            "Impotencia/ disfunción eréctil",
            "Incontinencia urinaria",
            "Infarto de miocardio",
            "Infección urinaria o cistitis",
            "Insomnio",
            "Insuficiencia cardiaca",
            "Intolerancia a la lactosa",
            "Juanetes",
            "Ladillas (piojos del pubis)",
            "Legionella",
            "Leishmaniasis",
            "Lengua geográfica o glositis migratoria benigna",
            "Lepra",
            "Leucemia",
            "Linfoma",
            "Lipedema",
            "Lipotimia",
            "Listeriosis",
            "Litiasis renal",
            "Ludopatía",
            "Lumbalgia",
            "Lupus",
            "Malaria",
            "Melanoma",
            "Melanoma metastásico",
            "Melasma",
            "Meningitis",
            "Mielitis transversa",
            "Mieloma múltiple",
            "Migrañas",
            "Miocardiopatía",
            "Miomas uterinos",
            "Miopía",
            "Mobbing",
            "Molusco contagioso",
            "Mononucleosis",
            "Muerte súbita cardiaca",
            "Narcolepsia",
            "Neumonía",
            "Neumotórax",
            "Obesidad",
            "Ojo seco",
            "Ojo vago",
            "Orquitis",
            "Ortorexia",
            "Orzuelo",
            "Osteoporosis",
            "Osteosarcoma",
            "Otitis",
            "Pancreatitis",
            "Paperas (parotiditis)",
            "Parálisis de Bell",
            "Parálisis del sueño",
            "Parkinson",
            "Pericarditis",
            "Peste",
            "Pie de atleta",
            "Pielonefritis",
            "Pies cavos",
            "Pies planos",
            "Pies zambos",
            "Poliomielitis",
            "Preeclampsia",
            "Presbicia",
            "Prostatitis",
            "Psoriasis",
            "Rabia",
            "Rectocele",
            "Retinoblastoma",
            "Retinopatía diabética",
            "Rinitis",
            "Rosácea",
            "Rotavirus",
            "Rubéola",
            "Salmonelosis",
            "Sarampión",
            "Sarcoidosis",
            "Sarcoma",
            "Sepsis",
            "Sífilis",
            "Silicosis",
            "Síndrome de burnout",
            "Síndrome de Diógenes",
            "Síndrome de Down",
            "Síndrome de Dravet",
            "Síndrome de estrés postraumático",
            "Síndrome de fatiga crónica",
            "Síndrome de Ganser",
            "Síndrome de Gilbert",
            "Síndrome de Gorlin-Goltz",
            "Síndrome de Guillain-Barré",
            "Síndrome de hiperestimulación ovárica",
            "Síndrome de Marfan",
            "Síndrome de Patau",
            "Síndrome de Reiter",
            "Síndrome de Rett",
            "Síndrome de Reye",
            "Síndrome de Sanfilippo",
            "Síndrome de Sjögren",
            "Síndrome de Smith-Magenis",
            "Síndrome de Tourette",
            "Síndrome de Turner",
            "Síndrome de Williams",
            "Síndrome de Wolfram",
            "Síndrome del túnel carpiano",
            "Síndrome postvacacional",
            "Síndromes mielodisplásicos (SMD)",
            "Sinus Pilonidal",
            "Sinusitis",
            "Siringomielia",
            "Sobrecrecimiento bacteriano o SIBO",
            "Sonambulismo",
            "Tendinitis",
            "Tétanos",
            "Tortícolis",
            "Tos ferina",
            "Toxoplasmosis",
            "Trastorno bipolar",
            "Trastorno de conducta del sueño en fase REM",
            "Trastorno de menstruación",
            "Trastorno obsesivo compulsivo (TOC)",
            "Trastorno por atracón",
            "Trastorno por déficit de atención e hiperactividad (TDAH)",
            "Trastornos del ritmo circadiano",
            "Tricomoniasis",
            "Trombosis venosa (flebitis)",
            "Tuberculosis",
            "Tumores cerebrales",
            "Uñas encarnadas (onicocriptosis)",
            "Uretritis",
            "Urticaria",
            "Vaginitis o vulvovaginitis",
            "Vaginosis bacteriana",
            "Varicela",
            "Varices",
            "Varicocele",
            "Vasculitis",
            "Vegetaciones",
            "Vértigo",
            "Vigorexia",
            "VIH / Sida",
            "Virus del Nilo Occidental",
            "Virus del papiloma humano (VPH)",
            "Virus Zika",
            "Vitíligo",
            "Vulvitis"
        ]

        for p in patologias:
            try:
                estudio_models.Diagnostico.objects.get(nombre=p)
            except estudio_models.Diagnostico.DoesNotExist as e:
                logging.debug(f'agregando patología {p}')
                d = estudio_models.Diagnostico(nombre=p)
                d.save()

        tipos_estudio = [
            'Exoma',
            'Genoma mitocondrial completo',
            'Carrier de enfermedades monogénicas recesivas',
            'Cariotipo',
            'Array CGH'
        ]

        for te in tipos_estudio:
            try:
                estudio_models.TiposDeEstudio.objects.get(nombre=te)
            except estudio_models.TiposDeEstudio.DoesNotExist as e:
                logging.debug(f'agregando tipo de estudio {te}')
                t = estudio_models.TiposDeEstudio(nombre=te)
                t.save()

        generar_parametros_de_turnos_por_defecto()

        return Response({'status':'sistema inicializado'})


class Ejemplos(APIView):
    
    permission_classes= [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
            Inicializo datos de ejemplo de una persona y un estudio
        """
        persona_models.ObraSocial(nombre='Osde', telefono='221-4237467', email='consutlas@osde.com.ar').save()
        persona_models.ObraSocial(nombre='IOMA', telefono='221-4237467', email='consutlas@ioma.gov.ar').save()

        p1 = persona_models.Persona(nombre='Pablo', apellido='R', dni='1', email='pablo@supermail.com', telefono='221-1112233', fecha_nacimiento='1980-12-01')
        p1.save()
        persona_models.Persona(nombre='Leonardo', apellido='B', dni='2211', email='leo@supermail.com', telefono='221-1112233', fecha_nacimiento='1981-02-03').save()
        persona_models.Persona(nombre='Nico', apellido='G', dni='2222211', email='nico@supermail.com', telefono='221-1112233', fecha_nacimiento='2004-05-04').save()

        mm = persona_models.Persona(nombre='Medi', apellido='Cote', dni='2212211', email='m@hotmail.com', telefono='221-1112233', fecha_nacimiento='1995-06-02')
        mm.save()

        generar_estudio_de_muestra()
        generar_lote()

        return Response({'status':'ejemplos generados'})

    def delete(self, request, format=None):

        return Response({'status':'ejemplos eliminados'})

