names = ['Jannet', 'Berenice', 'Rocio']
age = [36, 32, 59]
city = ['CDMX', 'CDMX', 'EDOMEX']
mix = list(zip(names, age, city))
print(mix)

for name,a, c in mix:
    print(f'{name} tiene {a} años y nacio en {c}')

