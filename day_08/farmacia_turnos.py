from farmacia_numeros import *
from os import system

turnoFarmacia = num_perfumeria()
turnoPerfumeria = num_perfumeria()
turnoCosmetico = turno_cosmeticos()


def bienvenida():
    print('¡ Bienvenid@ a la Farmacia del Bienestar !\n')

    while True:
        print('[1] - Turno Farmacia')
        print('[2] - Turno Perfumeria')
        print('[3] - Turno Cosmeticos')
        print('[4] - Salir')

        try:
            opcion = int(input('Toma turno:'))
        except:
            system('clear')
            print('Teclea [1, 2, 3]\n')
        else:
            system('clear')
            if opcion == 1:
                generador_turno('F', next(turnoFarmacia))
            elif opcion == 2:
                generador_turno('P', next(turnoPerfumeria))
            elif opcion == 3:
                generador_turno('C', next(turnoCosmetico))
            elif opcion == 4:
                system('clear')
                print('Gracias por visitar la farmacia del Bienestar.')
                break
            else:
                print('Elige un numero correcto\n')


bienvenida()
