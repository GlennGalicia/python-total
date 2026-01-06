def imprimir(arreglo):
    for key, value in dic.items():
        print(key, value)  # Imprime cada par clave-valor

# Ejemplo de uso
dic = {'clave1': 100, 'clave2': 200, 'clave3': 300}

imprimir(dic)
print('---')
print(dic.popitem())  # Elimina y devuelve un par clave-valor aleatorio
print('---')
imprimir(dic)
print('---')

# Ejemplo de lstrip
mixed = "xyxxyzabcxy"
print(mixed.lstrip("xy")) # Elimina 'x' y 'y' del inicio de la cadena

# Ejemplo de insert()
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
print(frutas)
frutas.insert(3, 'naraja') # Inserta 'naranja' en el índice 3
print(frutas)

# Ejemplo de disjoint
set_a = {1, 2, 3}
set_b = {4, 5, 6}
diferencia = set_a.isdisjoint(set_b)
print(f'¿Los conjuntos son disjuntos? {diferencia}')