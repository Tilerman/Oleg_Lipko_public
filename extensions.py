import requests
import json
from config import keys

class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')
        try:
            amount = int(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[keys[base]])
        total_base = total_base * amount
        return total_base
