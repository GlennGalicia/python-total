# Importar numpy como np
import numpy as np

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