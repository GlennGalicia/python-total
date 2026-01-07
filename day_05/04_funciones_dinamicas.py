def revisar_3_cifras(numero):
    """Revisa si un número tiene exactamente 3 cifras."""
    return numero in range(100, 1000)


suma = 840 + 10
resultado = revisar_3_cifras(suma)
print(f'¿El número {suma} tiene 3 cifras?: {resultado}')


def revisar_lista(lista):
    """Revisa si todos los números en una lista tienen exactamente 3 cifras."""
    for numero in lista:
        if numero in range(100, 1000):
            return True
        else:
            pass
    return False


print(revisar_lista([12, 25, 3, 470]))  # Debe retornar True
print(revisar_lista([12, 25, 3, 47]))  # Debe retornar False


def revisar_lista_v2(lista):
    mi_lista = []
    for numero in lista:
        if numero in range(100, 1000):
            mi_lista.append(numero)
        else:
            pass
    return mi_lista


print(revisar_lista_v2([12, 25, 3, 470, 150, 999]))  # Debe retornar [470, 150, 999]
print(revisar_lista_v2([12, 25, 3, 47]))
