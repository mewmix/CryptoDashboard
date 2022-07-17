from email.quoprimime import quote
import requests

headers = {
    'authority': 'wax.dfuse.eosnation.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US;q=0.7',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
}

params = {
    'account': 'eosio',
    'scope': 'eosio',
    'table': 'rammarket',
    'json': 'true',
}

response = requests.get('https://wax.dfuse.eosnation.io/v0/state/table', params=params, headers=headers)
result = response.json().get('rows')
quote_balance  = result[0]["json"]["quote"]["balance"]
base_balance = result[0]["json"]["base"]["balance"]
connector_weight = result[0]["json"]["quote"]["weight"]
con_weight = str(connector_weight).replace("WAX" , "")
base_bal = str(base_balance).replace("RAM" , "")
quote_bal = str(quote_balance).replace("WAX" , "")

bs_bal = int(float(base_bal))
qu_bal = int(float((quote_bal)))
cn_wght = int(float((con_weight)))
## credits to https://eosio.stackexchange.com/questions/847/how-to-get-current-last-ram-price & bancor (yet again)

#print(qu_bal / bs_bal * float(con_weight))

base_ram = qu_bal / bs_bal
limited_float = round(base_ram * 1024, 4) 
print(limited_float)


