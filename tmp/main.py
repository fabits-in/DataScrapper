# from core import nse
# import json
#
# instruments = ["SBIN", "RELIANCE", "ASHOKLEY", "BHARTIARTL", "PVR", "IRCTC", "ITC", "INFY", "POWERGRID", "ACC"]
#
# index = ["NIFTY", "SENSEX", "VIX", "NIFTY BANK", "NASDAQ", "DOW JONES", "S&P 500", "DAX", "	EURO STOXX 50",
#          "SHANGHAI", "NIKKEI 225", "HANG SENG", "KOSPI", "FTSE 100"]
#
# investing_index = ["17940", "39929", "14958", "166", "172", "175", "40820", "37426"]
#
# x = nse.list_of_all_results("ASHOKLEY")
# x = json.loads(x)
# print(json.dumps(x))

# if resultDetailedDataLink field is not null then use
# nse.parse_old_result_table(resultDetailedDataLink)
# if null then use
# nse.get_result(x[-1]["params"], x[-1]["seqNumber"])
import time

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320',
    'accept': 'text/html',
    'sec-fetch-user': '?1',
}

nse = requests.Session()
i = 0
while True:
    x = nse.get("https://www.nseindia.com", headers=headers)
    print(i)
    i += 1
    time.sleep(1)
