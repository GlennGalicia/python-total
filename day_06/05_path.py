from pathlib import Path

base = Path.home()
guia1 = Path(base, 'Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt')
guia2 = guia1.with_name('La_Pedrera.txt')
print(f'Ruta base:  {base}')
print(f'1er ruta:  {guia1}')
print(f'2da ruta: {guia2}')
print(f'Padre de la ruta 1: {guia1.parent}')

# Buscar todos los archivos .txt en la carpeta Europa y sus subcarpetas
searching = Path(base, 'Europa')

for file in searching.rglob('*.txt'):
    print(file)

print('\n--- Rutas relativas ---')

# Rutas relativas
base2 = Path('Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt')
europa = base2.relative_to(Path('Europa'))
spain = base2.relative_to(Path('España'))
print(base2)
print(f'Ruta relativa: {europa}')