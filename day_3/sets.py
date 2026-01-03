# Definición de Sets
set1 = set([1,2,3,4,5,6,7,8,9,10])
print(type(set1))
print(len(set1))
print(set1)

# Crear un set en base a 2 sets diferentes
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

# Añadir elemento a un set
s1.add(4)
print(s1)

# Remover elemento de un set
s1.remove(2)
print(s1)

# Limpiar un set
print(s3.clear())