def imprimir(texto):
    print(texto)

# Slicing
texto = 'ABCDEFGHIJKLM'

fragmento = texto[2] # extrae una posición en especifico
fragmentos = texto[2:5] # extrae un rango de posiciones
hasta = texto[:5] # extrae hasta una posición en especifico
desde = texto[2:] # extrae datos desde una posición hasta el final de la cadena
saltar = texto[0:10:2] # extrae datos haciendo saltos

imprimir(fragmento)
imprimir(fragmentos)
imprimir(hasta)
imprimir(desde)
imprimir(saltar)