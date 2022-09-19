import requests
import os
from bs4 import BeautifulSoup

def obtiene_peso():
    response = requests.request("GET","https://openexchangerates.org/api/latest.json",params={"app_id":os.getenv("API_CURRENCY_KEY")})
    values = response.json()
    try:
        return values['rates']['CLP']
    except:
        return "Ocurrió un error"
    # URL = "https://www.google.com/search?q=dolar+a+peso+chileno"
    # r = requests.get(URL)

    # soup = BeautifulSoup(r.text, 'html.parser')
    # temp = soup.find("div",class_="BNeawe").text
    # return temp.split(" ")[0]