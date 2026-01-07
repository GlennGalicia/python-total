# Argumentos indefinidos con kwargs (**kwargs)
def imprimir_datos(**kwargs):
    print(type(kwargs))


imprimir_datos(a=1, b=2, c=3, nombre="Juan", apellido="Pérez")


# Ejemplo de uso práctico de **kwargs
def suma_valores(**kwargs):
    total = 0
    for k, v in kwargs.items():
        print(f'{k} = {v}')
        total += v
    return total


resultado = suma_valores(a=10, b=20, c=30, d=40)
print(f'La suma total es: {resultado}\n')


# Ejemplo combinando *args y **kwargs
def funcion_combinada(num1, num2, *args, **kwargs):
    print(f'num1: {num1}\nnum2: {num2}')

    for arg in args:
        print(f'arg: {arg}')

    for k, v in kwargs.items():
        print(f'{k} = {v}')


funcion_combinada(13, 420, 3, 4, 5, nombre="Glenn", edad=25)
args = [3, 4, 5]
kwargs = {'nombre': 'Rocio', 'edad': 59}
funcion_combinada(13, 420, *args, **kwargs)