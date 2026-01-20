import requests
import bs4

# Crear URL sin definir pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de Titutlos con 4 o 5 estrellas
titulos_rating_alta = []

# Iterar paginas
for page in range(1, 51):
    # Crear sopa de cada pagina
    url_pagina = url_base.format(page)
    resultado = requests.get(url_pagina)
    soup = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de libros
    libros = soup.select('.product_pod')

    # Iterar en cada libro
    for libro in libros:

        # Checar 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar libro a la lista
            titulos_rating_alta.append(titulo_libro)



# Mostrar libros de 4 o 5 estrellas

for libro in titulos_rating_alta:
    print(libro)