# Comparación de Int en igualdad
mi_bool = (4 < 5) and (5 > 6)
print(f'La comparación de 4 < 5 and 5 > 6 es: {mi_bool}')

# Comparación con diferentes tipos de datos en igualdad
mi_bool = (5 == 5) and ('perro' == 'perro')
print(f'La comparación de 5 = 5 y \"perro\" = \"perro\" es: {mi_bool}')

# Comparación con diferentes tipos de datos en desigualdad
mi_bool = (10 == 10) or ('gato' == 'perro')
print(f'La comparación de 10 = 10 o \"gato\" = \"perro\" es: {mi_bool}')  # true por que 10 = 10

# Comparación con diferentes tipos de datos en desigualdad
mi_texto = 'Esta frase es breve'
mi_bool = ('frase' in mi_texto) or ('gato' in mi_texto)
print(f'La busqueda de \"frase\" o \"gato\" dentro de \"{mi_texto}\" es: {mi_bool}')
