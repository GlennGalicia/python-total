def imprimir(texto):
    print(texto)

# Index
mi_texto = 'esta es una prueba'
indice = mi_texto[-4]
caracter = mi_texto.index('a')
palabra = mi_texto.index('prueba')
especifico = mi_texto.index('a',5)
reversa = mi_texto.rindex('e',1)

imprimir(indice)
imprimir(caracter)
imprimir(palabra)
imprimir(especifico)
imprimir(reversa)