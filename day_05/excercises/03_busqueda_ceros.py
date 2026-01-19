def ceros_consecutivos(*args):
    contador = 0

    for numero in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        contador += 1
    return False


# Ejemplos de uso:
print(ceros_consecutivos(5, 6, 1, 0, 0, 9, 3, 5))  # True
print(ceros_consecutivos(1, 0, 2, 0, 0, 3))  # True
print(ceros_consecutivos(1, 0, 2, 0, 3))  # False
