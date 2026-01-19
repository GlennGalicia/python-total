def devolver_distintos(a, b, c):
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]


# Ejemplos de uso:
print(devolver_distintos(1, 2, 3))  # suma = 6 → 1
print(devolver_distintos(5, 4, 6))  # suma = 15 → 5
