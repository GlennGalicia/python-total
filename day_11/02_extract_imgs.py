import bs4
import requests

# Petición para solicitar imagenes del sitio web
peticion = requests.get('https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1')

# Volcar peticion a formato lxml
sopa = bs4.BeautifulSoup(peticion.content, 'lxml')

# recuperar la url de la primer foto encontrada
imagenes = sopa.select('.ProductImage')[0]['src']

# Petición para consultar la imagen
peticion_imagen = requests.get(imagenes)

# Crear y guardar img
f = open('img.jpg', 'wb')
f.write(peticion_imagen.content)
f.close()