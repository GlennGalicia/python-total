from random import shuffle, randint

# Lista inicial
palitos = ['-', '--', '---', '----']


# Mezcla palitos
def mezclar_palitos(lista):
    shuffle(lista)
    return lista


# Perdir intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un palito entre 1 y 4: ')
    return int(intento)


# Verificar intento
def verificar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('¡Ha lavar los platos!')
    else:
        print('¡Te haz salvado!')

    print(f'El palito elegido es: {lista[intento - 1]}')


# Juego de palitos
palitos_mezclados = mezclar_palitos(palitos)


# intento_usuario = probar_suerte()
# verificar_intento(palitos_mezclados, intento_usuario)

def lanzar_dados():
    dado_1 = randint(1, 6)
    dado_2 = randint(1, 6)
    return dado_1, dado_2


def evaluar_jugada(dado_1, dado_2):
    suma_dados = dado_1 + dado_2
    if suma_dados <= 6:
        return f'La suma de tus dados es {suma_dados}. Lamentable'
    elif suma_dados > 6 and suma_dados < 10:
        return f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    else:
        return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'


print(evaluar_jugada(lanzar_dados()[0], lanzar_dados()[1]))
