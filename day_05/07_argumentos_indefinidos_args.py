def suma_argumentos(*args):
    """Suma una cantidad indefinida de argumentos numéricos."""
    print(type(args))
    return sum(args)

# Ejemplo de uso
print(suma_argumentos(1,2,3,4,5,6,7,8,9))
print(suma_argumentos(10, 20, 30))
print(suma_argumentos())  # Debería devolver 0