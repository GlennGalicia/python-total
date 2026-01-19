def mi_lista():
    lista = []
    for x in range(1,6):
        lista.append(x)
    return lista

def mi_generador():
    for x in range(1,6):
        yield x * 10


print(mi_lista())

dato = mi_generador()

print(next(dato))
print(next(dato))
print(next(dato))
print(next(dato))
print(next(dato))
print(next(dato))


