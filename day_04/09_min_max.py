# Encuentra el numero menor y mayor pasando numeros como argumentos
menor = min(10,11,20,30,4)
mayor = max(10,11,20,30,4)
print(f'el num menor de lista es: {menor}\nel num mayor de lista es: {mayor}')

# Pasar una lista de numeros para encontar el mayor y menor numero
lista = [10,11,20,30,4]
print(f'el numero mayor de la lista es: {max(lista)}\nel numero menor de la lista es: {min(lista)}')

# pasar una lista de strings para encontrar el nombre mayor y menor
nombres = ['pablo', 'laura', 'glenn', 'luis', 'julia', 'rocio', 'jannet']
print(f'el nombre mayor de la lista es: {max(nombres)}\nel nombre menor de la lista es: {min(nombres)}')

# pasar un diccionario llave / valor para encontrar el valor mayor y menor
dic = {'clave1': 1, 'clave2': 2, 'clave3': 3, 'clave4': 4}
print(f'el valor mayor de la lista es: {max(dic.values())}\nel valor menor de la lista es: {min(dic.values())}')