# Control de flujo con Int
if 9 > 10:
    print('verdadero')
else:
    print('falso')

# Control de flujo con String
mascota = 'gato'
if mascota == 'perro':
    print('tienes un perro')
elif mascota == 'gato':
    print('tienes un gato')
else:
    print('Tu mascota no se encuentra en la lista')

# Control de flujo anidado
edad = 16
calificacion = 7
if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Haz aprobado tu curso')
    else:
        print('Haz reprobado tu curso')
else:
    print('Eres mayor de edad')
