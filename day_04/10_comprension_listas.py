mi_lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(mi_lista)

pies = [10,20,30,40,50]
metros = [m / 3.281 for m in pies]
print(metros)