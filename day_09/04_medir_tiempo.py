import timeit

setup1 = '''
def prueba_for(numero):
    lista = []
    for nu in range(1, numero +1):
        lista.append(nu)
    return lista
'''

setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 0
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

'''

duracion_for = timeit.timeit('prueba_for(10)', setup1, number=1000)
duracion_while = timeit.timeit('prueba_while(10)', setup2, number=1000)
print(f'duracion_for: {duracion_for}')
print(f'duracion_while: {duracion_while}')
