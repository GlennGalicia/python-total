# loop while con int
monedas = 5
while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print('No tengo más monedas')

# loop while con string
respuesta = 's'
while respuesta == 's':
    respuesta = input('Quieres continuar? (s/n): ')
else:
    print('Gracias')

# palabra reservada break
nombre = input('Ingrese su nombre: ').lower()
for letra in nombre:
    if letra == 'g':
        break
    print(letra)
