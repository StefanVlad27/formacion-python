import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import wikipedia
import datetime

# opciones de voz / idioma
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# escuchar nuestro microfono y devolver lo que escucha en texto
def transformar_audio_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Escuchando...")

        # almacenar lo que escucha en variable
        audio = r.listen(origen)

        try:
        #     buscar en google
            pedido = r.recognize_google(audio, language="es-ES")
            print(pedido)
            return pedido

        # manejo de errores
        except sr.UnknownValueError:
            print("Lo siento, no te he entendido")
            return "Lo siento, no te he entendido"

        except sr.RequestError:
            print("Lo siento, mi servicio de google speech no funciona")
            return "Lo siento, mi servicio de google speech no funciona"

        except:
            return "Algo no ha ido bien"

# funcion para que el asistente hable
def hablar(mensaje):

    # encender el motor de voz pytttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # prununciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# informar dia de la semana
def pedir_dia():

    # datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # lista de dias de la semana
    calenario = {0: "Lunes",
                 1: "Martes",
                2: "Miércoles",
                3: "Jueves",
                4: "Viernes",
                5: "Sábado",
                6: "Domingo"}

    # informar dia de la semana
    hablar(f"Hoy es {calenario[dia_semana]}.")

# informar hora actual
def pedir_hora():

    #   crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"Son las {hora.hour} horas y {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    # informar hora
    hablar(hora)

# saludo incial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buenos días"
    else:
        momento= "Buenos tardes"


    # informar saludo
    hablar(f"{momento}, soy tu asistente virtual.")

    # informar dia de la semana
    pedir_dia()

    # informar hora
    pedir_hora()

# funcion central del asistente
def pedir_cosas():
    saludo_inicial()

    comenzar = True
    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_texto().lower()

        if 'abrir youtube' in pedido:
            hablar("Abriendo youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif 'abrir google' in pedido:
            hablar("Abriendo google")
            webbrowser.open("https://www.google.com/")
            continue
        elif 'que dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice que")
            hablar(resultado)
        elif 'busca en internet' in pedido:
            hablar("Buscando en google")
            pedido = pedido.replace("busca en google", "")
            pywhatkit.search(pedido)
            continue
        elif 'reproducir' in pedido:
            hablar("Reproduciendo")
            pedido = pedido.replace("reproducir", "")
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'cerrar' in pedido:
            hablar("Hasta luego")
            break


pedir_cosas()




