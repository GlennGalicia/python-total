import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# opciones de voz
id1 = 'com.apple.eloquence.es-ES.Eddy'
id2 = 'com.apple.eloquence.es-MX.Flo'
id3 = 'com.apple.eloquence.es-MX.Grandma'
id4 = 'com.apple.eloquence.es-MX.Shelley'


# escuchar microfono y devolver el audio como texto
def transformar_audio_en_texto():
    # almacenar el recognizer en una valiable
    r = sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as source:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar comenzo la grabación
        print("Ya puedes hablar...")

        # guardar audio
        audio = r.listen(source)

        try:
            # Buscar en google lo que escucho
            pedido = r.recognize_google(audio, language='es-ES')

            # Prueba de que pudo ingresar y transformar
            print(f'Dijiste: {pedido}')

            # devolver a pedido
            return pedido
        # No comprende el audio
        except sr.UnknownValueError:

            # No comprendio el audio
            print("No se puede hablar....")

            return 'Sigo esperando 1'

        # en caso de no resolver el pedido
        except sr.RequestError:

            # No comprendio el audio
            print("ups, no hay servicio....")

            return 'Sigo esperando 2'

        # errores inesperados
        except Exception as e:
            # Mostrar el error específico
            print(f"Ups algo ha salido mal.... Error: {type(e).__name__}: {e}")
            return 'Sigo esperando'


# asistente pueda ser escuchado
def hablar(mensaje):
    # encender el pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():
    # crear datos con dia de hoy
    hoy = datetime.date.today()
    print(hoy)

    # crear el dia de la semana
    dia_semana = hoy.weekday()
    print(dia_semana)

    # diccionario dias de la semana
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sabado',
                  6: 'Domingo'}
    # decir dia de la semana
    hablar(f'El día de hoy es: {calendario[dia_semana]}')


# informar la hora actual
def pedir_hora():
    # crear variable con datos de la hora
    hora = datetime.datetime.now()

    hora = f'En este momento son las {hora.hour} con {hora.minute} minutos y {hora.second} segundos.'

    # decir la hora
    hablar(hora)


# saludo inicial
def saludo_inicial():
    # Crear valiable con la hora
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas Noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen Día'
    else:
        momento = 'Buenas Tardes'

    hablar(f'{momento}, soy Jarvis, tu asistente personal. Por favor dime en que te puedo ayudar')


# funcion central del asistente
def pedir_cosas():
    # activar el saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    while comenzar:

        # activar microfono y guardar en variable string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('con gusto estoy abriebndo youtube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Trabajo en ello')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('buscar en Wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es-ES')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('buscar en internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto encontre')
            continue
        elif 'reproducir' in pedido:
            hablar('buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'gogle': 'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMaraketPrice']
                hablar(f'La encontre, el precio de {accion} es de {precio_actual}')
                continue
            except:
                hablar('NO la he encontrado....')
                continue
        elif 'adiós' in pedido:
            hablar('Cuidate Miller')
            break


pedir_cosas()
