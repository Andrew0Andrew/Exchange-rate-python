import requests

print("if you want to stop the program, just write 'stop'")
flag = True
while flag:
    currency = input('write currency - ').upper().strip()

    if currency == 'STOP':
        flag = False
        break

    comparable_currency = input('write comparable currency - ').upper().strip()

    if len(currency) == 3 and len(comparable_currency) == 3 and isinstance(currency, str) and isinstance(comparable_currency, str) and currency.isalpha() and comparable_currency.isalpha():
        def exchangeRate(currency, comparable_currency):
            url = f'https://v6.exchangerate-api.com/v6/c1a3397367a9dcdcbdf3c622/latest/{currency}'
            response = requests.get(url).json()
            if response["result"] == 'error':
                print("write existing value")
                return
            if not (comparable_currency in response["conversion_rates"]):
                print("write existing value")
                return
            data = round(response["conversion_rates"][comparable_currency],2)
            print(f'1 {currency} - {data} {comparable_currency}')

        exchangeRate(currency, comparable_currency)
    else:
        print('write value like "usd" or "USD"')