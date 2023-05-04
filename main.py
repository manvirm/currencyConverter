from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()
    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()

    if len(data) == 0:
        print('Invalid currency')
        return

    return list(data.values())[0]


rate = exchange_rate("USD", "CAD")
print(rate)