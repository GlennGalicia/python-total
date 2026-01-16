def sumar():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    print(f'La suma es: {n1+n2}')
    print('Gracias por sumar '+ n1)

def intentar_sumar():
    try:
        # Codigo que queremos probar
        sumar()
    except TypeError:
        # Codigo a ejecutar si hay error
        print('Error al concatenar valores int con str')
    except ValueError:
        # Codigo a ejecutar si hay error
        print('Error al capturar Str, se espera valores númericos')
    else:
        # Codigo a ejecutar si no hay error
        print('Hiciste todo bien')
    finally:
        # Codigo que se ejecutara de todos modos
        print('Eso fue todo')

def pedir_numero():

    while True:
        try:
            numero = int(input('Ingresa Numero: '))
        except:
            print(f' no es un numero')
        else:
            print(f'numero ingresado es: {numero}')
            break

#intentar_sumar()
pedir_numero()

