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

data = get_currencies()
printer.pprint(data)