import requests

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


def equity_trade_info(symbol):
    response = nse.get(f'https://www.nseindia.com/api/quote-equity?symbol={symbol}&section=trade_info', headers=headers)
    return response.text


def equity_info(symbol):
    response = nse.get(f'https://www.nseindia.com/api/quote-equity?symbol={symbol}', headers=headers)
    return response.text


def list_of_all_securities():
    response = nse.get("https://www1.nseindia.com/corporates/datafiles/LDE_EQUITIES_MORE_THAN_5_YEARS.csv",
                       headers=headers)
    return response.text


def holding_shares(table):
    response = nse.get(
        f'https://www1.nseindia.com/corporates/shldStructure/ShareholdingPattern/shp_{table}.jsp?ndsId=153247&symbol=RELIANCE&countStr=0|0|0|0|0|0|0|0|0|0|0|0|0|0|NEW_1|0|N&asOnDate=30-Sep-2020&industry=-&CompanyName=Reliance%20Industries%20Limited&RevisedData=N',
        headers=headers)
    return response.text

