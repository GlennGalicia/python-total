# Definiciones
lista = []

texto = input('Digite una frase: ').lower()
lista.append(input('Digite primer letra: ').lower())
lista.append(input('Digite segunda letra: ').lower())
lista.append(input('Digite tercera letra: ').lower())
frase = texto.split()
validacion = "python" in texto
print('\n')
print(f'- La primer letra "{lista[0]}" se repite {texto.count(lista[0])} veces')
print(f'- La segunda letra "{lista[1]}" se repite {texto.count(lista[1])} veces')
print(f'- La tercera letra "{lista[2]}" se repite {texto.count(lista[2])} veces')
print(f'- La frase ingresada cuenta con {len(frase)} palabras')
print(f'- La primera letra dentro de la frase es {texto[0]}')
print(f'- La última letra dentro de la frase es {texto[-1]}')
print(f'- Te muestro la frase de forma invertida:\n\t{texto[::-1]}')
print(f'- La palabra \"python\" se encuentra dentro de la frase ? : {validacion}')
