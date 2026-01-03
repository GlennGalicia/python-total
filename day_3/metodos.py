def imprimir(texto):
    print(texto)

# Métodos de cadenas
mi_texto = 'Este es el texto de Glenn'
res1 = mi_texto.upper()  # convierte el texto a mayusculas
res2 = mi_texto.lower() # convierte el texto a minusculas
res3 = mi_texto[20:].upper() # convierte el texto a mayuscolas comenzando desde la posición 20
res4 = mi_texto.split() # recupera la cadena de texto dentro de una lista
res5 = mi_texto.find('ñ') # al no encontrar el caracter ñ, retorna -1
res6 = mi_texto.replace('Glenn', 'Rocio') # remplaza un caracter o palabra

imprimir(res1)
imprimir(res2)
imprimir(res3)
imprimir(res4)
imprimir(res5)
imprimir(res6)

# Método Join
val1 = 'Aprender'
val2 = 'python'
val3 = 'es'
val4 = 'genial'
res5 = ' '.join([val1, val2, val3, val4])

imprimir(res5)