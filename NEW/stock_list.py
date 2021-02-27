import csv
import io
import json

import requests

# https://www1.nseindia.com/content/equities/EQUITY_L.csv
from tqdm import tqdm


def getAllStockListUpdated():
    url = "https://www1.nseindia.com/content/equities/EQUITY_L.csv"
    req = requests.get(url)
    url_content = req.content
    reader = csv.DictReader(io.StringIO(url_content.decode("utf-8")))
    return list(reader)


def equity_info(symbol):
    headers = {
        'authority': 'www.nseindia.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en;q=0.9',
    }
    nse = requests.Session()
    nse.get("https://www.nseindia.com/", headers=headers)
    response = nse.get(f'https://www.nseindia.com/api/quote-equity', headers=headers, params=[('symbol', symbol)])
    return response.text


#
# result = []
with open("stocklist.txt", "w") as f:
    for stock in tqdm(getAllStockListUpdated()):
        try:
            symbol = stock["SYMBOL"]
            x = json.loads(equity_info(symbol))
            stock["INDUSTRY"] = x.get("metadata", {}).get("industry", "-")
            stock["SECTOR INDEX"] = x.get("metadata", {}).get("pdSectorInd", "-").strip()
            stock["ISSUED SHARES"] = x.get("securityInfo", {}).get("issuedCap", 0)
            # result.append(stock)
            f.write(json.dumps(stock) + "\n")
        except Exception as e:
            print(e, stock)
