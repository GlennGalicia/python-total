nombre_empleado = input('Ingrese su nombre: ')
num_ventas = int(input('Ingrese la cantidad de ventas del mes: '))
comisiones = round(num_ventas * 13 / 100, 2)
print(f'Hola {nombre_empleado}, tus comisiones de este mes, son de ${comisiones} \nFelicidades!!')
