import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/search?q=dolar+a+peso+chileno"
r = requests.get(URL)

soup = BeautifulSoup(r.text, 'html.parser')
temp = soup.find("div",class_="BNeawe iBp4i AP7Wnd").text
print(temp.split(" ")[0])