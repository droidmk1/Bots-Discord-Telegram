import requests
from web_scrap import precioInicial
from web_scrap import precioDeseado


def telegram_bot_sendtext(bot_message):

    bot_token  = '2052847633:AAFcfcmOLI65KSjG0gAS7VIP6O9qAkMc7aQ'

    bot_chatID = '1064793253'

    enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(enviar_text)

    return response.json()

if precioInicial < precioDeseado:
    test = telegram_bot_sendtext(f"ATENCION Hay oferta, bajo el precio! Esta en: S/.{precioInicial} en el Enlace: https://store.steampowered.com/app/728880")

else:
    test = telegram_bot_sendtext("No hay oferta")