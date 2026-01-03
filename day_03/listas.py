lista1 = ['a', 'b', 'x', 'y']
lista2 = [123, 'hola', 45.4, 'x']
lista3 = lista1 + lista2
lista3[0] = 'Glenn'  # Reemplaza el dato
lista3.append('g')  # Añade dato a la lista
lista3.pop(0)  # Elimina dato de la lista
lista4 = ['z', 'y', 'x', 'm', 'g', 'b']
lista4.sort()  # Ordena la lista

print(type(lista1))  # Imprime el tipo de dato
print(len(lista2))  # Imprime el tamaño de la lista
print(lista2[2])  # Imprime el dato especificado de la lista
print(lista3)  # Imprime la concatenación de una lista
print(lista4) # Imprime la lista 4 ordenada