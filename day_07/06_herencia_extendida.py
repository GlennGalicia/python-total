class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite sonidos')


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('pio...')

    def volar(self,metros):
        print('El Pajaro vuela {} metros'.format(metros))

piolin = Pajaro(1, 'amarillo',60)

# Metodo heredados de Animal
piolin.nacer()
print(f'Pajaro tiene edad de {piolin.edad} y es de color {piolin.color}, Vuela a {piolin.altura_vuelo} metros de altura.')

# Metodo heredado y sobre escrito
piolin.hablar()

# Metodo propios de la clase
piolin.volar(100)