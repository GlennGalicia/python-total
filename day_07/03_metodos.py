class Pajaro:
    # Atributos de Clase
    alas = True

    # Atributos de Instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Metodos
    def piar(self):
        print('Pio...mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro color {self.color} ha volado {metros} metros')


# Instancias
pajarito = Pajaro('Rojo', 'Pinson')
piolin = Pajaro('amarillo', 'Canario')

pajarito.piar()
pajarito.volar(50)

piolin.piar()
piolin.volar(100)
