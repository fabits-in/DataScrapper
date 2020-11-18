from datetime import datetime

from core import nse
import json
from core.server.MongoDB import MongoDB

instruments = ["SBIN", "RELIANCE", "ASHOKLEY"]

mongodb = MongoDB()


def symbol_info(symbol):
    instrument_info = json.loads(nse.equity_info(symbol))
    instrument_trade_info = json.loads(nse.equity_trade_info(symbol))
    return {**instrument_info, **instrument_trade_info}


def get_total_number_of_trades(symbol):
    data = nse.get_today_ohlc_data(symbol)
    data = data.strip().split("\n")
    x = data[1].strip().split(",")[-1]
    return int(x)


def update_instrument(symbol):
    data = symbol_info(symbol)
    total_trades = get_total_number_of_trades(symbol)

    listing_date = datetime.strptime(data["metadata"]["listingDate"], '%d-%b-%Y')
    updated_date = datetime.strptime(data["metadata"]["lastUpdateTime"], '%d-%b-%Y %H:%M:%S')
    ohlc_date = datetime(updated_date.year, updated_date.month, updated_date.day)

    instrument_summary = {'symbol': data["info"]["symbol"],
                          'name': data["info"]["companyName"],
                          'industry': data["info"]["industry"],
                          'isin': data["metadata"]["isin"],
                          'series': data["metadata"]["series"],
                          'status': data["metadata"]["status"],
                          'listing_date': listing_date,
                          'last_update_time': updated_date,
                          'sector_index': data["metadata"]["pdSectorInd"].strip(),
                          'face_value': data["securityInfo"]["faceValue"],
                          'issued_cap': data["securityInfo"]["issuedCap"],
                          "open": data["priceInfo"]["open"],
                          "high": data["priceInfo"]["intraDayHighLow"]["max"],
                          "low": data["priceInfo"]["intraDayHighLow"]["min"],
                          "close": data["priceInfo"]["close"],
                          "prev_close": data["priceInfo"]["previousClose"],
                          "total_volume": data["marketDeptOrderBook"]["tradeInfo"]['totalTradedVolume'],
                          "total_value": data["marketDeptOrderBook"]["tradeInfo"]['totalTradedValue'],
                          "total_trade": total_trades,
                          "delivery": data["securityWiseDP"]['deliveryQuantity'],
                          }

    mongo_data = {"symbol": symbol, "series": data["metadata"]["series"], "market_type": "N",
                  "exchange": "NSE",
                  "isin": data["metadata"]["isin"],
                  "open": data["priceInfo"]["open"], "high": data["priceInfo"]["intraDayHighLow"]["max"],
                  "low": data["priceInfo"]["intraDayHighLow"]["min"], "close": data["priceInfo"]["close"],
                  "prev_close": data["priceInfo"]["previousClose"],
                  "total_volume": data["marketDeptOrderBook"]["tradeInfo"]['totalTradedVolume'],
                  "total_value": data["marketDeptOrderBook"]["tradeInfo"]['totalTradedValue'],
                  "total_trade": total_trades, "delivery": data["securityWiseDP"]['deliveryQuantity'],
                  "date": updated_date}
    mongodb.write_historical_data([mongo_data])
    mongodb.write_instrument_data(symbol, instrument_summary)

# for x in instruments:
#     update_instrument(x)
