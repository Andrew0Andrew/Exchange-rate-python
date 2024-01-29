import requests

currency = input('write currency - ').upper()
comparable_currency = input('write comparable currency - ').upper()
def exchangeRate(currency, comparable_currency):
    url = f'https://v6.exchangerate-api.com/v6/c1a3397367a9dcdcbdf3c622/latest/{currency}'
    response = requests.get(url).json()
    data = round(response["conversion_rates"][comparable_currency],2)
    return data

result = exchangeRate(currency, comparable_currency)
print(f' 1 {currency} - {result} {comparable_currency}')




