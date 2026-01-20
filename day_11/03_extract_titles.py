import requests
import bs4

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

request = requests.get(url_base.format(1))
soup = bs4.BeautifulSoup(request.content, 'lxml')

libros = soup.select('.product_pod')

estrella = libros[0].select('.star-rating.Three')
titulo_libro = libros[0].select('a')[1]['title']
print(estrella)
print(titulo_libro)