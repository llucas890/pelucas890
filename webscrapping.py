import requests
from bs4 import BeautifulSoup as bs
import msvcrt

r = requests.get('https://www.nosis.com/es/institucional/quienes-somos')
soup = bs(r.content, 'lxml')

texto1 = soup.find('div', class_='col-xs-12 cuerp-izq').text
print(texto1)

nombre1 = soup.find('div', class_='titBannServicios').text
print(nombre1)

respuesta = input('Si o No?: ')
if respuesta == 'Si':
    numero = soup.find('div', class_='titBannServ01').text
    print(f'{numero}')
    print('Llamanos!!!')
elif respuesta == 'No':
    print('Que lastima que no quieras contratar a nosis')
else:
    print('Debes proporcionar Si o No')

msvcrt.getch()
