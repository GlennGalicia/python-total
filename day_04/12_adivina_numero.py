from random import randint

num_intentos = 0
estimado = 0
num_secreto = randint(1, 100)

nombre_jugador = input('Ingresa tu nombre: ')
print(f'{nombre_jugador}, He pensando un numero entre 1 y 100\nTienes 8 intentos para adivinar el numero...\n')

while num_intentos < 8:
    num_intentos += 1
    estimado = int(input('Introduce un numero entre 1 y 100: '))
    print(f'Intento: {num_intentos}')
    if estimado < 1 or estimado > 100:
        print('Introduce un numero entre 1 y 100')
    elif estimado < num_secreto:
        print(f'Haz elegido un número menor al número secreto')
    elif estimado > num_secreto:
        print(f'Haz elegido un número mayor al número secreto')
    elif estimado == num_secreto:
        print(f'{nombre_jugador} Haz elegido el número correcto y te tomo {num_intentos} intentos')
        break

if estimado != num_secreto:
    print(f'\nLo siento !!, el número secreto fue: {num_secreto}')
