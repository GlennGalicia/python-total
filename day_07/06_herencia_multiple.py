class Padre:
    def hablar(self):
        print('Padre Habla')


class Madre:
    def reir(self):
        print('ja ja ja')

    def hablar(self):
        print('Madre habla')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)
