import requests
from bs4 import BeautifulSoup as bs
import msvcrt
import pandas as pd

print('Programa creado por Lucas Lescano')
print('Debes ingresar la url de la categoria')
print('por ejemplo: https://computacion.mercadolibre.com.ar/pc-escritorio/pc/')
r = requests.get(input('Introduce la url: '))
soup = bs(r.content, 'lxml')

# nombres de items
nombres = soup.find_all('h2', class_='ui-search-item__title', limit=50)
nombreslista = list()
# precios de items
precios = soup.find_all('span', class_='price-tag-fraction', limit=50)
precioslista = list()

contador = 0

for nombre in nombres:
    nombreslista.append(nombre.get_text())

for precio in precios:
    precioslista.append(precio.get_text())

df = pd.DataFrame({'Nombre'.center(50, '-'): nombreslista, 'Precio': precioslista}, index=list(range(1, 51)))
print(df)

msvcrt.getch()