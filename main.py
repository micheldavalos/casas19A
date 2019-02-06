import requests
from bs4 import BeautifulSoup
import json
url = 'http://aviso.informador.com.mx/index.php/bienes-raices'
r = requests.get(url)
r.encoding = 'utf-8'
# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
items = soup.find_all(class_ = 'items')
# print(items)
casas = items[0].find_all('li')
# print(casas)
lista = []
for c in casas:
    casa = {
        "ubicacion": c.find_all(class_='location')[0].text,
        "titulo": c.a.text,
        "precio": c.h5.text,
        "descripcion": c.p.text,
        "recamaras": c.find(class_='info-rec').text,
        "m2": c.find(class_='info-m2').text,
        "m2_2": c.find(class_='info-m2-2').text,
        "wc": c.find(class_='info-wc').text,
        "cars": c.find(class_='info-cars').text,
        "colonia": c.find(class_='info-gps').contents[1],
        "imgs": ['http:' + i['src'] for i in c.find_all('img')]
    }
    lista.append(casa)

with open('informador.json', 'w') as archivo:
    json.dump(lista, archivo, sort_keys=False, indent=4)

# print(lista)
# c = casas[0]
# ubicacion = c.find_all(class_='location')[0].text
# titulo = c.a.text
# precio = c.h5.text
# descripcion = c.p.text
# recamaras = c.find(class_='info-rec').text
# m2 = c.find(class_='info-m2').text
# m2_2 = c.find(class_='info-m2-2').text
# wc = c.find(class_='info-wc').text
# cars = c.find(class_='info-cars').text
# colonia = c.find(class_='info-gps').contents[1]
# imgs = ['http:' + i['src'] for i in c.find_all('img')]