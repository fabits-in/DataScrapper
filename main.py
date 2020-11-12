import nse

instruments = ["SBIN", "RELIANCE", "ASHOKLEY", "BHARTIARTL", "PVR", "IRCTC", "ITC", "INFY", "POWERGRID", "ACC"]


def symbol_info(symbol):
    instrument_info = nse.equity_info("SBIN")
    instrument_trade_info = nse.equity_trade_info("SBIN")
    # code
    return {}


for x in instruments:
    symbol_info(x)

#
# x = nse.list_of_all_securities()


# import json
#
# result = {}
# result["symbol"] = json.loads(instrument_info)["info"]["symbol"]
# result["isin"] = json.loads(instrument_info)["info"]["isin"]
# print(result)

# "symbol"
# "isin"
# "status"
# "date of listing"
# "Industry"
# "P/E"
# "Sectoral_Index P/E"
# "Sectoral_Index"
# "Board Status"
# "Trading Status"
# "Trading Segment"
# "Session No."
# "SLB"
# "Class of Shares"
# "Derivatives"
# "Face Value"
# "List Issued Capital"
# "Surveillance"
# "Total Market Cap"
# "Free Float Market Cap"
# "Impact cost"
# -----
# "PREV. CLOSE"
# "OPEN"
# "HIGH"
# "LOW"
# "CLOSE"
# "VWAP"
# "LOWER BAND"
# "UPPER BAND"
# "PRICE BAND"
# "ADJUSTED PRICE"
# "Traded Volume"
# "Traded Value"
# "Value at Risk"
# "Security VaR"
# "Index VaR"
# "VaR Margin"
# "Extreme Loss Rate"
# "Adhoc Margin"
# "Applicable Margin Rate"
# ----
# "52_OPEN"
# "52_HIGH"
# "52_LOW"
# "52_CLOSE"
