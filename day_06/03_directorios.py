from pathlib import Path
import os

# Obtener la ruta del directorio actual
ruta = os.getcwd()
# Imprimir la ruta del directorio actual
print(ruta)

# Cambiar el directorio actual
os.chdir('/Users/glenn/Documents/Python')

# Imprimir la nueva ruta del directorio actual
ruta = os.getcwd()
print(ruta)
file = open("otro_archivo.txt", "r")
print(file.read())
file.close()
os.chdir('/Users/glenn/PycharmProjects/PythonProject/day_06')
ruta = os.getcwd()
print(ruta)

# Dividir la ruta en partes
tupla_ruta = os.path.split(ruta)
print(tupla_ruta)

# Crear un nuevo directorio
os.makedirs('/Users/glenn/PyCharmProjects/PythonProject/day_06/nuevo_directorio', exist_ok=True)

# Eliminar un directorio
os.rmdir('/Users/glenn/PyCharmProjects/PythonProject/day_06/nuevo_directorio')

# Usar pathlib para manejar rutas
direccion = Path('/Users/glenn/Documents/Python') / 'otro_archivo.txt'
another_file = open(direccion, "r")
print(another_file.read())
another_file.close()
