from random import randint, uniform, choice, shuffle

# Implementando randit
num_int = randint(1, 100)
print(num_int)

# Implementando uniform
num_floar = round(uniform(1, 100),1)
print(num_floar)

# Implementando choice
mi_lista = ['azul','verde','rojo','amarillo','negro']
color = choice(mi_lista)
print(color)

# Implementando shuffle
num_list = [1,2,3,4,5,6,7,8,9,10]
shuffle(num_list)
print(num_list)