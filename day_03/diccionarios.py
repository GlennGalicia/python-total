# Tipo de dato(diccionario)
mi_diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(type(mi_diccionario))
print(mi_diccionario)

# Define e imprime el diccionario creoado
cliente = {'nombre': 'Glenn', 'apellido': 'Galicia', 'peso': 65, 'talla': 1.70}
print(cliente)

# Navegar entre diccionarios
dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200, 's3': 300}}
print(dic['c2'][1])
print(dic['c3']['s1'])

# Buscar un elemento en el diccionario y cambiarlo a mayusculas
dic2 = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(dic2['c2'][1].upper())

# Agregar elementos al diccionario
dic3 = {1: 'a', 2: 'b'}
print(dic3)
dic3[3] = 'c'
print(dic3)
print(dic3.keys()) # Imprime las claves del diccionario
print(dic3.values()) # Imprime los valores del diccionario
print(dic3.items()) # Imprime los elementos del diccionario
