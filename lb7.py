import requests
import json

# валютний код криптовалюти
currency_code = input("Введіть валютний код криптовалюти: ")

# формуємо посилання на API з використанням валютного коду
api_url = f"https://api.coinpaprika.com/v1/coins/{currency_code}"

# виконуємо HTTP-запит та зберігаємо відповідь в форматі JSON
response = requests.get(api_url)
response_json = json.loads(response.text)

# отримуємо необхідну інформацію з JSON-об'єкту
currency_name = response_json['name']
currency_symbol = response_json['symbol']
currency_description = response_json['description']

# виводимо інформацію у консоль

print(f"Назва: {currency_name}")
print(f"Символ: {currency_symbol}")
print(f"Опис: {currency_description}")