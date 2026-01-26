# Importar numpy como np
import numpy as np
import pandas as pd

# Crear array de una dimensión con la función np.array()
array_unidim = np.array([1, 2, 3, 4, 5])

# Crear array de dos dimensiones(bidimensional)
array_bidim = np.array([[1, 2, 3],
                        [4, 5, 6]])

# Crear array con tres dimenciones (tridimensional)
array_tridim = np.array([[[1, 2, 3],
                          [4, 5, 6]],
                         [[7, 8, 9],
                          [10, 11, 12]]])

# Atributos del array unidimensional (forma, número de dimensiones, tipos de datos, tamaño, y tipo)
print(f'forma: {array_unidim.shape}')
print(f'dimensiones: {array_unidim.ndim}')
print(f'tipo de dato: {array_unidim.dtype}')
print(f'tamaño: {array_unidim.size}')
print(f'tipo: {type(array_unidim)}')

# Atributos del array bidimensional
print(f'forma: {array_bidim.shape}')
print(f'dimensiones: {array_bidim.ndim}')
print(f'tipo de dato: {array_bidim.dtype}')
print(f'tamaño: {array_bidim.size}')
print(f'tipo: {type(array_bidim)}')

# Atributos del array tridimensional
print(f'forma: {array_tridim.shape}')
print(f'dimensiones: {array_tridim.ndim}')
print(f'tipo de dato: {array_tridim.dtype}')
print(f'tamaño: {array_tridim.size}')
print(f'tipo: {type(array_tridim)}')

# Importamos pandas como pd, y creamos un DataFrame a partir del array bidimensional
datos = pd.DataFrame(array_bidim)
print(datos)

# Creamos un array de tamaño 4x3, formado únicamente por unos (1)
unos = np.ones((4, 3))
print(unos)

# Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)
ceros = np.zeros((2, 4, 3))
print(ceros)

# Creamos un array de números en el rango de 0 a 100, con un paso de 5
array_1 = np.arange(0, 101, 5)
print(array_1)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)
array_2 = np.random.randint(0, 10, (2, 3))
print(array_2)

# Creamos un array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3, 5)
array_3 = np.random.random((3, 5))
print(array_3)

# Establecemos la "semilla" de números aleatorios en 27
np.random.seed(27)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5)
array_4 = np.random.randint(0, 10, (3 ,5))
print(array_4)