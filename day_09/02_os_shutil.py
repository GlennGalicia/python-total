import os
import shutil
import send2trash

print(os.getcwd())

mi_archivo = open('curso.txt','w')
mi_archivo.write('Texto de prueba en archivo curso .txt')
mi_archivo.close()

# Imprime lista de archivos en el directorio actual
print(os.listdir())

# Mover archivo de ubicación
# shutil.move('curso.txt','/Users/glenn/Desktop')

# Mover archivo a la papelera
send2trash.send2trash('curso.txt')

# Navegar entre carpetas
ruta = '/Users/glenn/Documents/Python/Carpeta_Superior'

for carpeta, subcarpeta, archivo in os.walk(ruta,True):
    print(f'En la carpeta: {carpeta}')
    print(f'Las Subcarpeta, son:')
    for subc in subcarpeta:
        print(f'\t{subc}')
    print('Los archivos, son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')