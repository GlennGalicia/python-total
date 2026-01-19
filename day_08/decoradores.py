def cambiar_palabras(tipo):
    def mayusculas(texto):
        print(texto.upper())

    def minusculas(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayusculas
    elif tipo == 'min':
        return minusculas


mi_operacion = cambiar_palabras('may')
mi_operacion('todo a mayusculas')

mi_operacion = cambiar_palabras('min')
mi_operacion('todo a minusculas')


# Decorador
def decorar_palabra(funcion):
    def metodo_aleatoreo(texto):
        print('Hola')
        funcion(texto)
        print('Adios')

    return metodo_aleatoreo


@decorar_palabra
def mayusculas(texto):
    print(texto.upper())


@decorar_palabra
def minusculas(texto):
    print(texto.lower())


mayusculas('Glenn Fernando Galicia Aviña')
minusculas('GLENN FERNANDO GALICIA AVIÑA')
