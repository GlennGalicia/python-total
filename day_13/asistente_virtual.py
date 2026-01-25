import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


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

transformar_audio_en_texto()