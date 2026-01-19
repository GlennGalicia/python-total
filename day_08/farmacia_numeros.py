# Decorador
def decorador_turno(funccion):
    def imprime_turno(area, turno):
        print('Su turno es:')
        funccion(area, turno)
        print('Aguarde y sera atendido\n')

    return imprime_turno


@decorador_turno
def generador_turno(area, turno):
    print(f'{area} - {turno}')


# Generadores
def num_perfumeria():
    turno = 0

    while True:
        turno += 1
        yield turno


def turno_farmacia():
    turno = 0

    while True:
        turno += 1
        yield turno


def turno_cosmeticos():
    turno = 0

    while True:
        turno += 1
        yield turno
