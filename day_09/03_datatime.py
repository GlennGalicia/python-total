from datetime import datetime, date,time

# Crear un horario
dia_creado = datetime(1991, 7, 13)
print(f'El dia creado es: {dia_creado}')

# Fecha actual
hoy = datetime.now()
print(f'Hoy es: {hoy}')

dia_actual = datetime.today()
print(f'Dia actual: {dia_actual}')
print(f'Año: {dia_actual.year}')
print(f'mes:{dia_actual.month}')
print(f'día:{dia_actual.day}')


# Calcular una fecha
nacimiento = date(1900,1,1)
defuncion = date(2000,2,2)
vida = defuncion - nacimiento
print(f'Vida es: {vida}')