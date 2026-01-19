class Pajaro:
    # Atributo de Clase
    alas = True

    # Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


pajarito1 = Pajaro('Rojo', 'Tucan')

print(f'Mi pajaro {pajarito1.especie} es de color {pajarito1.color} y alas {pajarito1.alas}')
print(Pajaro.alas)