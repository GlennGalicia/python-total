class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muuu')


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')


vaca_1 = Vaca('Vaquita')
oveja_1 = Oveja('Birrias')

vaca_1.hablar()
oveja_1.hablar()

animales = [vaca_1,oveja_1]
for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca_1)
animal_habla(oveja_1)