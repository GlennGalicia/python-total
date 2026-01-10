def ceros_consecutivos(*args):
    anterior = 0

    for numero in args:
        if numero == 0 and anterior == 0:
            return True
        anterior = numero
    return False


# Ejemplos de uso:
print(ceros_consecutivos(5, 6, 1, 0, 0, 9, 3, 5))  # True
print(ceros_consecutivos(1, 0, 2, 0, 0, 3))  # True
print(ceros_consecutivos(1, 0, 2, 0, 3))  # False
