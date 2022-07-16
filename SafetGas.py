import requests
import json
import os

key = os.environ.get('etherscan_key')
cookies = {
    '__cf_bm': 'XmNs72B3H1U4VgNNb8pWyfE0KqRxfKPoa9w_DZjdfy8-1657953426-0-ARNi3Szvrz6Q5zUUnlLkQmt7XJeN0Y2vUHnx5IYX6lcAtNWOUc6CouM5Ie6iJ/c0t+25XvpHoot58M8FCYUz25ulbVzm9VXq5T3c4Wri/pScSv4wbfE+g70EjH+rNRzhNQ==',
    '__stripe_mid': '8363bde1-0d41-4a57-a346-2902c97a14fdcdd304',
    '__stripe_sid': '79b43399-68e3-4132-b592-5ef40860f3107f7f38',
    '__cuid': 'd38ea0eec6314e7f8f4448b8b040bdbf',
    'amp_fef1e8': 'c1c7ec8d-5a27-4bc2-bbf1-c72c5659d7b1R...1g82rf5ki.1g82rotep.5.2.7',
}

headers = {
    'authority': 'api.etherscan.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__cf_bm=XmNs72B3H1U4VgNNb8pWyfE0KqRxfKPoa9w_DZjdfy8-1657953426-0-ARNi3Szvrz6Q5zUUnlLkQmt7XJeN0Y2vUHnx5IYX6lcAtNWOUc6CouM5Ie6iJ/c0t+25XvpHoot58M8FCYUz25ulbVzm9VXq5T3c4Wri/pScSv4wbfE+g70EjH+rNRzhNQ==; __stripe_mid=8363bde1-0d41-4a57-a346-2902c97a14fdcdd304; __stripe_sid=79b43399-68e3-4132-b592-5ef40860f3107f7f38; __cuid=d38ea0eec6314e7f8f4448b8b040bdbf; amp_fef1e8=c1c7ec8d-5a27-4bc2-bbf1-c72c5659d7b1R...1g82rf5ki.1g82rotep.5.2.7',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
}

params = {
    'module': 'gastracker',
    'action': 'gasoracle',
    'apikey': f'{key}',
}

response = requests.get('https://api.etherscan.io/api', params=params, cookies=cookies, headers=headers)

result = response.json().get('result')
print(result['SafeGasPrice'])
