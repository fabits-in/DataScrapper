# import json
#
# from core.server.MongoDB import MongoDB
#
# f = open("s1")
# mongodb = MongoDB()
#
# forecast = "forecasts?section=price"
# financial1 = "financials?statement=income&view=normal&period=annual"
# financial2 = "financials?period=quarter&statement=income&view=normal"
# financial3 = "financials?period=annual&statement=balancesheet&view=normal"
# financial4 = "financials?period=annual&statement=cashflow"
# peers = "peers?table=valuation"
# news = "news?type=mixed"
# holding = "holdings?history=mfPctT&type=mixed"
# dividend = "events?type=dividends"
# corp_action = "events?type=corpActions"
# announce = "events?type=announcements"
# legal_order = "events?type=legal"
#
# for x in f.readlines():
#     x = x.split("####")
#     url, data = x[0].strip(), x[1].strip()
#     url = url.split("/")[-1].strip()
#     if url == forecast:
#         url = "forecast"
#     elif url == financial1:
#         url = "financial1"
#     elif url == financial2:
#         url = "financial2"
#     elif url == financial3:
#         url = "financial3"
#     elif url == financial4:
#         url = "financial4"
#     elif url == peers:
#         url = "peers"
#     elif url == news:
#         url = "news"
#     elif url == holding:
#         url = "holding"
#     elif url == dividend:
#         url = "dividend"
#     elif url == corp_action:
#         url = "corp_action"
#     elif url == announce:
#         url = "announce"
#     elif url == legal_order:
#         url = "legal_order"
#     else:
#         data = json.loads(data)
#         info = data["props"]["pageProps"]["securityInfo"]["info"]
#         isin = data["props"]["pageProps"]["securityInfo"]["isin"]
#         print(info, isin)
#         mongodb.write_instrument_data(symbol, instrument_summary)
#     # print(url, data)
# f.close()


import core.ticker_tape
from core.server.MongoDB import MongoDB

mongodb = MongoDB()

fin = core.ticker_tape.get_financials_income_data()
fin1 = core.ticker_tape.get_financials_balance_sheet_data()
fin2 = core.ticker_tape.get_financials_cash_flow_data()

result = []
for x in fin2:
    x["symbol"] = "SBIN"
    x["type"] = "cash_flow"
    x["isin"] = "INE062A01020"
    result.append(x)

mongodb.write_financial_data(result)

# print(fin)
# symbol : "SBIN"
# type : "income", "balance_sheet", "cash_flow"
# isin : "INE062A01020"
