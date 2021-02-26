import csv
import io

import requests


# https://www1.nseindia.com/content/equities/EQUITY_L.csv
def getAllStockListUpdated():
    url = "https://www1.nseindia.com/content/equities/EQUITY_L.csv"
    req = requests.get(url)
    url_content = req.content
    reader = csv.DictReader(io.StringIO(url_content.decode("utf-8")))
    return list(reader)


print(getAllStockListUpdated())
