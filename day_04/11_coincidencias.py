serie = 'N-02'

if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Motorola')
else:
    print('No existe el producto')

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe el producto')

print('\n')

cliente = {'nombre': 'glenn',
           'edad': 34,
           'ocupacion': 'Ingeniero'}

pelicula = {'titulo': 'Matriz',
            'ficha_tecnica': {'protagonista': 'Keanu Reeves', 'direccion': 'Lana y Lili'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print('Cliente:')
            print(f'Nombre: {nombre}, Edad: {edad}, Ocupacion: {ocupacion}')
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'direccion': direccion}}:
            print('Pelicula:')
            print(f'Titulo: {titulo}, Protagonista: {protagonista}, Direccion: {direccion}')
        case _:
            print('No existe el nombre')
