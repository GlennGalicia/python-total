from random import choice

diccionario_letras = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
palabras = ['python', 'java', 'kotlin', 'javascript']
num_caracteres = 0
letras_correctas = list()
letras_incorrectas = list()


def elegir_palabra():
    return choice(palabras)


def letra_es_valida(letra):
    if len(letra) != 1:
        print('Por favor, ingresa solo una letra.')
        return False
    elif letra not in diccionario_letras:
        print('Por favor, ingresa una letra válida del alfabeto.')
        return False
    return True

def letra_en_palabra(letra):
    return letra in palabra_secreta


def solicitar_letras(n_caracteres):
    vidas = 6

    while vidas > 0:
        validacion_letra = True
        print(f'Cuentas con {vidas} vidas.')

        while validacion_letra:
            letra = input('Ingresa una letra del alfabeto: ').lower()

            if letra_es_valida(letra):

                if letra_en_palabra(letra):
                    posicion_letra = palabra_secreta.index(letra)
                    letras_correctas[posicion_letra] = letra
                    print(letras_correctas)
                    n_caracteres += 1
                    if n_caracteres == len(palabra_secreta):
                        print(f'¡Felicidades! Has adivinado la palabra secreta: "{palabra_secreta}", te quedaron {vidas} vidas.')
                        vidas -= 1
                        return
                else:
                    letras_incorrectas.append(letra)
                    print(f'Lo siento, la letra "{letra}" no está en la palabra secreta. {letras_incorrectas}')
                    validacion_letra = False
                    vidas -= 1
            else:
                pass


def bienvenida():
    print("¡Bienvenido al juego del Ahorcado!")
    print("Cuentas con 6 vidas para adivinar la palabra secreta.")

    for letra in palabra_secreta:
        letras_correctas.append('-')
    print(letras_correctas)
    print('\n')


palabra_secreta = elegir_palabra()
num_letras_secretas = len(palabra_secreta)

bienvenida()
solicitar_letras(num_caracteres)
