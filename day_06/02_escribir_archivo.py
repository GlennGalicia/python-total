# Abrir el archivo en modo escritura
mi_archivo1 = open("file3.txt", "w")
mi_archivo2 = open("file4.txt", "w")
mi_archivo3 = open("Prueba.txt", "a")

# Escribir líneas en el archivo
mi_archivo1.write("Primera línea de texto.\n")
mi_archivo1.write("Segunda línea de texto.\n")
mi_archivo1.write("Tercera línea de texto.\n")

# Escribir múltiples líneas usando una lista
lista_palabras = ["Cuarta línea de texto.", "Quinta línea de texto.", "Sexta línea de texto."]
for palabra in lista_palabras:
    mi_archivo2.write(palabra + "\n")
#mi_archivo2.writelines(lista_palabras)

# Agregar texto al final del archivo existente
mi_archivo3.write("\nEsta línea se agrega al final del archivo existente.")

# Cerrar el archivo
mi_archivo1.close()
mi_archivo2.close()
mi_archivo3.close()
