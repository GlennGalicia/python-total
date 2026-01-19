class Pajaro:
    # Atributos de Clase
    alas = True

    # Atributos de Instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # (Métod de Instancia)
    def piar(self):
        print('pio')

    # (Métod de Instancia) Función que permite acceder a otros metodos
    def volar(self, metros):
        print('El pajaro vuela {}'.format(metros))
        self.piar()

    # (Métod de Instancia) Función que accede y modifica atributos de la instancia
    def color_negro(self):
        self.color = 'Negro'
        print('Ahora el pajaro es color {}'.format(self.color))

    # (Métod de clase)
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')

    # (Métod estatico) No modifica valores en la instancias o atributos de clase
    @staticmethod
    def mirar():
        print('El pajaro Mira')


# Instancia de Pajaro
piolin = Pajaro('amarillo', 'Canario')

piolin.color_negro()
piolin.volar(100)
piolin.poner_huevos(15)
piolin.mirar()

print(piolin.alas)
# Modificar atributos de la clase
piolin.alas = False
print(piolin.alas)

# Acceder a metodos de clase
Pajaro.poner_huevos(50)
Pajaro.mirar()
