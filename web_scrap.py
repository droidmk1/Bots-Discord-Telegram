from bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://store.steampowered.com/app/728880/Overcooked_2/?l=spanish")

soup = BeautifulSoup(url.content, "html.parser")

resultado = soup.find("div", class_="discount_final_price")

precioInicio_text = resultado.text
precioInicio_text = precioInicio_text.replace('S/.','')
precioInicial = float(precioInicio_text)
# print(precioInicial)
# print(type(precioInicial))


precioDeseado = 15.00

if precioInicial < precioDeseado:
    print("Hay oferta")
else:
    print("No hay oferta")