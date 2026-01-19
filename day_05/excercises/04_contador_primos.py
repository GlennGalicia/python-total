def contar_primos(numero):
    contador = 3
    lista_primos = [2]

    if numero < 2:
        return 0

    while contador <= numero:
        for n in range(3, contador, 2):
            if contador % n == 0:
                contador += 2
                break
        else:
            lista_primos.append(contador)
            contador += 2
    print(lista_primos)
    return len(lista_primos)


print(contar_primos(50))
