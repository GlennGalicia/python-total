# Abrir un archivo en modo lectura
archivo1 = open('Prueba.txt')

# Leer línea por línea
line = archivo1.readline()
print(line)

line = archivo1.readline()
print(line)

line = archivo1.readline()
print(line)

# Abrir un archivo en modo lectura
archivo2 = open('file2.txt')

# Leer todo el contenido del archivo
for line in archivo2:
    print(line)

# Cerrar los archivos
archivo1.close()
archivo2.close()
