from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    currency = soup.find('span', {'class': 'ccOutputRslt'}).text
    currency =float(currency[:-4])
    return(currency)

    # return soup.find('span', {'class': 'ccOutput
print(get_currency('USD', 'EUR'))