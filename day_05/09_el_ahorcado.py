from random import choice

diccionario_letras = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
lista_palabras = ['python', 'java', 'kotlin', 'javascript']
num_caracteres = 0
caracteres_validos = list()
caracteres_invalidos = list()


def seleccionar_palabra():
    return choice(lista_palabras)


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

                if letra in palabra_secreta:
                    posicion_letra = palabra_secreta.index(letra)
                    caracteres_validos[posicion_letra] = letra
                    print(caracteres_validos)
                    n_caracteres += 1
                    if n_caracteres == len(palabra_secreta):
                        print(f'¡Felicidades! Has adivinado la palabra secreta: "{palabra_secreta}", te quedaron {vidas} vidas.')
                        vidas -= 1
                        return
                else:
                    caracteres_invalidos.append(letra)
                    print(f'Lo siento, la letra "{letra}" no está en la palabra secreta. {caracteres_invalidos}')
                    validacion_letra = False
                    vidas -= 1
            else:
                pass


def bienvenida():
    print("¡Bienvenido al juego del Ahorcado!")
    print("Cuentas con 6 vidas para adivinar la palabra secreta.")

    for letra in palabra_secreta:
        caracteres_validos.append('-')
    print(caracteres_validos)
    print('\n')


palabra_secreta = seleccionar_palabra()
num_letras_secretas = len(palabra_secreta)

bienvenida()
solicitar_letras(num_caracteres)
