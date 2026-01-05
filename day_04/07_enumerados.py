lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for key, item in enumerate(lista):
    print(f'{key}: {item}')

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for key, name in enumerate(lista_nombres):
    if name.startswith('M'):
        print(key)

