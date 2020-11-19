import requests

response = requests.get('https://www.fnb.co.za')
print(response.headers)



url = 'https://v6.exchangerate-api.com/v6/b00ff8206ab7df95b5d9d335/latest/USD'
response = requests.get(url)
result = response.json()
print(result['conversion_rates'])
amount = float(input("Enter Amount"))
x = result['conversion_rates']['ZAR']
total_USD = (amount/x)
y = result['conversion_rates']['USD']
print ("USD", round(total_USD,2))

