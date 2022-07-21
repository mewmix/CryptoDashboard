import requests
import json

headers = {
    'accept': 'application/json',
}



response = requests.get('https://api.yearn.finance/v1/chains/1/vaults/all', headers=headers)
result = response.json()
for i in result : 
    if i['apy']['gross_apr'] >= 0.50 : 
        print(f"Name: {i['name']} APY: {i['apy']['gross_apr']} TVL: {i['tvl']['tvl']}")
   
