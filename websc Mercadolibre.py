import requests
from bs4 import BeautifulSoup as bs
import msvcrt

print('Programa creado por Lucas Lescano')
print('Debes introducir la url de mercadolibre que quieres que te muestre items y precios')
print('Debes ingresar la url de la categoria')
r = requests.get(input('Introduce la url: '))
soup = bs(r.content, 'lxml')

nombres = soup.find_all(class_='ui-search-item__title', limit=10)

precios = soup.find_all('span', class_='price-tag-fraction', limit=10)

for nombre in nombres:
    for precio in precios:
        print(f'[{nombre.get_text()}] [${precio.get_text()}]')


msvcrt.getch()
