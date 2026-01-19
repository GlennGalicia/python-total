from collections import Counter, defaultdict, namedtuple

mi_lista = [5, 5, 5, 3, 3, 1, 1, 1, 6, 9, 9, 9, 9]
mi_string = 'glenn galicia'
mi_frase = 'al pan pan y al vino vino'

print(Counter(mi_lista))
print(Counter(mi_string))
print(Counter(mi_frase.split()))

serie = Counter([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4])
print(serie.most_common())
print(serie.most_common(2))

print('--- default dic ---')

mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_dic['uno'])

mi_dic2 = defaultdict(lambda: 'nada')
mi_dic2['uno'] = 'verde'
print(mi_dic2)
print(mi_dic2['dos'])
print(mi_dic2)

print('--- namedtuple ---')

mi_tupla = (13, 25, 17, 45)
print(mi_tupla[0])

Persona = namedtuple('Persona',['nombre','edad','peso'])
ariel = Persona('Glenn','34','65')
print(ariel)
print(ariel[0])