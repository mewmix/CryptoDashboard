import requests

headers = {
    'authority': 'api.thegraph.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'origin': 'https://thegraph.com',
    'referer': 'https://thegraph.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
}

json_data = {
    'query': '{\n  accounts(where: {health_gt: 0, health_lt: 1.005, totalBorrowValueInUSD_gt: 1000}) {\n    id\n    health\n    totalBorrowValueInUSD\n    totalCollateralValueInUSD\n  }\n}\n',
    'variables': None,
}

response = requests.post('https://api.thegraph.com/subgraphs/name/traderjoe-xyz/lending', headers=headers, json=json_data)

dict = response.json()

for i in dict:

  all = dict[i]["accounts"]
  total = len(all)
  print(f"There are {total} accounts near liquidation on Trader Joe based on our filters")
  if total > 0:
    print(f"Printing the first 2 results of {total}")
    print(all[0]["id"], all[0]["health"], all[0]["totalBorrowValueInUSD"])
    print(all[1]["id"], all[1]["health"], all[1]["totalBorrowValueInUSD"])
        
  if total < 0:
    print("No results to display")



