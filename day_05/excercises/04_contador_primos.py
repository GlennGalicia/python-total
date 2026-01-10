def contar_primos(number):
    contador = 2
    lista_primos = []
    while contador < number + 1:

        if contador % 2 == 1:
            lista_primos.append(contador)
            print(contador)

        contador += 1


contar_primos(20)
