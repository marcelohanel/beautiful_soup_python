import sys
import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cotao+do+dolar"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}
requisicao = requests.get(link, headers=headers)

if requisicao.status_code == 200:
    site = BeautifulSoup(requisicao.text, "html.parser")
else:
    print("Não foi possível obter os dados do site !")
    sys.exit()

cotacao_dolar = site.find("span", class_="SwHCTb")

print(cotacao_dolar["data-value"])
print(cotacao_dolar.get_text())

