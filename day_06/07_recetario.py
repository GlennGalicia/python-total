from pathlib import Path
from os import system

ruta_base = Path(Path.home(), 'Recetas')
lista_opciones = ['1', '2', '3', '4', '5', '6']
arreglo_categorias = []
arreglo_recetas = []
enRecetario = True


# Retorna el numero de recetas existentes global
def num_recetas():
    return len(list(ruta_base.glob('**/*.txt')))


# Imprime y guarda en una lista las Categorias/Carpetas existentes en Recetas
def mostrar_lista_categorias():
    arreglo_categorias.clear()

    for d in ruta_base.iterdir():
        if d.stem != '.DS_Store':
            arreglo_categorias.append(d.name)
            print(f'- {d.name}')


# Imprime las recetas dentro de una categoria seleccionada
def mostrar_lista_recetas(categoria):
    arreglo_recetas.clear()

    searching = Path(ruta_base, categoria)

    print(f'La Categoría {categoria} cuentas con las siguientes recetas: ')

    for file in searching.glob('*.txt'):
        arreglo_recetas.append(file.stem)
        print(f'- {file.stem}')


# Función que permite leer el contenido de una receta
def leer_receta(categoria, receta):
    system('clear')
    print('Descripción de la receta:')
    receta = Path(ruta_base, categoria, receta + '.txt')
    print(receta.read_text())
    print('\n')


# Función que permite crear una receta y su contenido
# Retorna True si se creo exitosamente
# Retorna False si existe una receta con el mismo directorio y nombre
def crear_receta(categoria, nueva_receta, nuevo_contenido):
    system('clear')
    if categoria in arreglo_categorias:
        nueva_receta = Path(ruta_base, categoria, nueva_receta + '.txt')
        if not nueva_receta.exists():
            nueva_receta.write_text(nuevo_contenido)
            print(f'La Receta: {nueva_receta.stem} fue creada exitosamente...\n')
            return True
        else:
            print(f'La receta con el nombre: {nueva_receta.stem}, existe.\n')
            return False
    else:
        print(f'La Categoría {categoria}, no existe.\n')
        return False


# Función que permite crear una categoria nueva dentro de las recetas
# Retorna True cuando la carpeta de la categoria se creo exitosamente
# Retorna False cuando la carpeta de la categoria ya existe
def crear_categoria(categoria):
    system('clear')
    categoria = Path(ruta_base, categoria)
    if not categoria.exists():
        categoria.mkdir(exist_ok=True)
        print(f'La Categoría: {categoria.stem} se creo exitosamente...\n')
        return True
    else:
        print(f'La Categoría: {categoria.stem}, existe.\n')
        return False


# Función que permite eliminar una receta de una categoria
# Retorna True si la receta fue eliminada exitosamente
# Retorna False si no existe la receta a eliminar
def eliminar_receta(categoria, delete_receta):
    system('clear')
    borrar_receta = Path(ruta_base, categoria, delete_receta + '.txt')

    if borrar_receta.exists():
        borrar_receta.unlink()
        print(f'Receta: {delete_receta} borrada exitosamente....\n')
        return True
    else:
        print(f'La receta: {delete_receta}, no existe.\n')
        return False


# Función que permite eliminar una categoria seleccionada
# Retorna True si la categoria se elimino exitosamente
# Retorna False si no existe la categoria a eliminar
def eliminar_categoria(delete_categoria):
    system('clear')
    borrar_categoria = Path(ruta_base, delete_categoria)

    if borrar_categoria.exists():
        borrar_categoria.rmdir()
        print(f'La Categoría: {delete_categoria} se ha eliminado exitosamente.\n')
        return True
    else:
        print(f'La Categoría: {delete_categoria} no existe. \n')
        return False


# Menu de opciones para el Cliente
def menu_opciones():
    print('[1] - Leer Receta')
    print('[2] - Crear Receta')
    print('[3] - Crear Categoría')
    print('[4] - Eliminar Receta')
    print('[5] - Eliminar Categoría')
    print('[6] - Salir del recetario')


# Funcion que valida que la opcion seleccionada sea valida
def validar_opcion(select):
    if len(select) != 1:
        print('Ingresa solo un numero, ejemplo: 1 ')
        return False
    elif select not in lista_opciones:
        print('Por favor, ingresa una número válido entre 1 y 6')
        return False
    return True


def seleccion_opcion():
    opciones = False
    seleccion = ''

    while not opciones:
        seleccion = input('Elige una opción [x]: ')

        if validar_opcion(seleccion):
            break
        else:
            pass

    return int(seleccion)

def inicio_recetario(recetario):
    while recetario:
        menu_opciones()
        option = seleccion_opcion()
        system('clear')

        match option:
            case 1:
                print('[1] - Leer Receta:')
                mostrar_lista_categorias()
                catego = input('Elige una Categoría: ').capitalize()
                system('clear')
                if catego in arreglo_categorias:
                    mostrar_lista_recetas(catego)
                    busqueda_receta = input('Qué receta quieres leer: ')
                    if busqueda_receta in arreglo_recetas:
                        leer_receta(catego, busqueda_receta)
                    else:
                        print('No existe esa receta.')
                else:
                    print('No existe esa Categoría.')
            case 2:
                print('[2] - Crear Receta:')
                mostrar_lista_categorias()
                catego = input('Elige una Categoría: ').capitalize()
                nombre_receta = input('Nombre de tu receta: ').capitalize()
                descripcion_receta = input('Descripción de tu receta: ')
                crear_receta(catego, nombre_receta, descripcion_receta)
            case 3:
                print('[3] - Crear Categoría:')
                nueva_categoria = input('Nombre de tu Categoría: ').capitalize()
                crear_categoria(nueva_categoria)
            case 4:
                print('[4] - Eliminar Receta:')
                mostrar_lista_categorias()
                catego = input('Elige una Categoría: ').capitalize()
                system('clear')
                mostrar_lista_recetas(catego)
                busqueda_receta = input('Qué receta quieres borrar: ')
                eliminar_receta(catego, busqueda_receta)
            case 5:
                print('[5] - Eliminar Categoría')
                mostrar_lista_categorias()
                catego = input('Elige una Categoría para eliminar: ').capitalize()
                eliminar_categoria(catego)
            case 6:
                recetario = False
                print('Gracias por visitar tu Recetario')
            case _:
                pass



print('Bienvenido al recetario de cocina. Aquí puedes agregar y ver tus recetas favoritas.')
print(f'La ruta de tus recetarios es: {ruta_base} y cuentas con {num_recetas()} recetas guardadas.')
inicio_recetario(enRecetario)

