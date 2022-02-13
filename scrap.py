from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://peru.as.com/resultados/futbol/torneo_descentralizado/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# #Equipos

eq = soup.find_all('span', class_='nombre-equipo')

equipos = list()

count = 0
for i in eq:
    if count < 18:
        equipos.append(i.text)
    else:
        break
    count += 1

# print(equipos)

#Puntos

pt = soup.find_all('td', class_='destacado')

puntos = list()

count = 0
for i in pt:
    if count < 18:
        puntos.append(i.text)
    else:
        break
    count += 1

# print(puntos)

df = pd.DataFrame({'Nombre' : equipos, 'Puntos' : puntos}, index=list(range(1,19)))
print(df)

df.to_csv('Clasificacion_Liga1.csv', index=False)