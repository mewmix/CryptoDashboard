import requests
import json

headers = {
    'accept': 'application/json',
}

params = {
    'ids': 'wax',
    'vs_currencies': 'usd',
}

response = requests.get('https://api.coingecko.com/api/v3/simple/price', params=params, headers=headers)
result = response.json().get('wax')
print(result['usd'])
