# loop for con letras
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for letra in letras:
    print(f'Letra: {letra} se encuentra en la posición: {letras.index(letra)}')
print('\n')

# loop for con palabras
nombres = ['pablo', 'laura', 'glenn', 'luis', 'julia', 'rocio', 'jannet']
for nombre in nombres:
    if nombre.startswith('l'):
        print(f'Nombre: {nombre.upper()}')
    else:
        print(f'Nombre: {nombre} no empieza con la letra l')
print('\n')

# loop con lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
for numero in numeros:
    suma += numero
print(f'La suma de los numeros es: {suma}')
print('\n')

# loop con lists de numeros anidados
for num, num2 in [[1, 2], [4, 5, ]]:
    print(f'{num} - {num2}')
print('\n')

# loop con diccionarios
dic = {'clave1': 1, 'clave2': 2, 'clave3': 3, 'clave4': 4}
for key, value in dic.items():
    print(f'{key}: {value}')