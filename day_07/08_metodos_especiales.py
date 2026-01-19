class CD:

    # Atributos de instancia
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones


mi_cd = CD('Armin Van Buren', 'Mirage', 40)

print(str(mi_cd))
print(len(mi_cd))
