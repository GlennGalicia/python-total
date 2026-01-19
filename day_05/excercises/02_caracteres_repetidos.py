def caracteres_unicos(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista

print(caracteres_unicos('entretenido'))  # ['a', 'e', 'm', 'n', 'o', 'r', 't']))