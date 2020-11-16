from core import nse
import json

instruments = ["SBIN", "RELIANCE", "ASHOKLEY", "BHARTIARTL", "PVR", "IRCTC", "ITC", "INFY", "POWERGRID", "ACC"]

index = ["NIFTY", "SENSEX", "VIX", "NIFTY BANK", "NASDAQ", "DOW JONES", "S&P 500", "DAX", "	EURO STOXX 50",
         "SHANGHAI", "NIKKEI 225", "HANG SENG", "KOSPI", "FTSE 100"]

investing_index = ["17940", "39929", "14958", "166", "172", "175", "40820", "37426"]


def symbol_info(symbol):
    instrument_info = json.loads(nse.equity_info(symbol))
    instrument_trade_info = json.loads(nse.equity_trade_info(symbol))
    return {**instrument_info, **instrument_trade_info}

# for x in instruments:
#     save_instrument_data(x)
