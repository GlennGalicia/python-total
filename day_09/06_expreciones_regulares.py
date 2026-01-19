import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'
patron = 'ayuda'

# Encuentra la primer coincidencia
busqueda = re.search(patron, texto)
print(busqueda.group())

# Encuentra las conincidencias y las recupera
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
    print(hallazgo.group())

# Busca los numeros
texto2 = 'llama al 564-856-6588'
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron, texto2)
print(resultado)


clave = input('Ingrese la clave: ')
patron = r'\D{1}\w{7}'
busqueda = re.search(patron, clave)
print(busqueda)