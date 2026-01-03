tuple1 = (1, 2, 3, 4, 5)
print(type(tuple1))
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

tuple2 = ('a', 'b', 3)
x, y, z = tuple2
print(x)
print(y)
print(z)

tuple3 = (1, 1, 2, 3, 4, 5, 6)
print(f'La tupla cuenta con {tuple3.count(1)} veces el numero 1')
print(f'El numero 1 se encuentra en la posicion {tuple3.index(1)}')