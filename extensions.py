import requests

class APIException(Exception):
    def __init__(self, message):
        self.message = message


class CurrencyConverter:
    @staticmethod
    def get_supported_currencies():
        supported_currencies = ['RUB', 'USD', 'EUR']
        return supported_currencies

    @staticmethod
    def get_price(base, quote, amount):
        if base == quote:
            return amount

        try:
            url = f'https://api.exchangerate-api.com/v4/latest/{base}'
            response = requests.get(url)
            data = response.json()
            conversion_rate = data['rates'][quote]
            result = amount * conversion_rate
            return result
        except KeyError:
            raise APIException(f"Валюта '{base}' или '{quote}' не найдена.")

