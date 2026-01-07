# Ejemplo de uso de tuplas en un bucle for para calcular descuentos en precios de café
precio_cafe = [("Espresso", 1.5), ("Latte", 2.5), ("Cappuccino", 3.0)]

for cafe, precio in precio_cafe:
    print(precio * 0.45)

# Función para encontrar el café más caro en una lista de tuplas
def cafe_mas_caro(lista):
    cafe_mas_caro = ("", 0)
    for cafe, precio in lista:
        if precio > cafe_mas_caro[1]:
            cafe_mas_caro = (cafe, precio)
    return cafe_mas_caro


cafe, precio = cafe_mas_caro(precio_cafe)
print(f'El café más caro es {cafe} con un precio de ${precio}')
