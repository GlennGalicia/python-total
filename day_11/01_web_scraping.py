import requests
import bs4

# Generar la petición
response = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')

# Convertir en xml la respuesta
sopa = bs4.BeautifulSoup(response.text, 'lxml')

# Extraer titulo
titulo = sopa.select('title')[0].get_text()
print(f'Titulo: {titulo}\n')


# Extraer parrafor
parrafos = sopa.select('.post-body p')

for parrafo in parrafos:
    print(parrafo.get_text())
