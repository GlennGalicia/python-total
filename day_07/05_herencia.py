class Animal:

    # Atributo de Clase
    vida = False

    # Atributos de Instancia
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')


class Pajaro(Animal):
    pass


piolin = Pajaro(6,'amarillo')

print(Pajaro.__bases__)
print(Animal.__subclasses__())
#print(piolin.nacer())
print(piolin.edad)
print(piolin.color)

piolin.vida = True
print(piolin.vida)