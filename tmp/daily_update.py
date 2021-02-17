import re
from datetime import datetime, timedelta

import tqdm

from core import nse, investing
import json
from core.server.MongoDB import MongoDB

instruments = ["SBIN", "RELIANCE", "ASHOKLEY"]

investing_index = ["17940", "39929", "14958", "166", "172", "175", "40820", "37426"]

investing_name = {"17940": "Nifty 50", "39929": "BSE Sensex", "14958": "Nasdaq",
                  "166": "S&P 500", "172": "DAX", "175": "Euro Stoxx 50", "40820": "Shanghai",
                  "37426": "KOSPI"}

mongodb = MongoDB()


def symbol_info(symbol):
    instrument_info = json.loads(nse.equity_info(symbol))
    instrument_trade_info = json.loads(nse.equity_trade_info(symbol))
    return {**instrument_info, **instrument_trade_info}


def clean_it(data):
    d = []
    for x in data:
        if x == '':
            x = '0'
        if x == '"-"':
            x = '-1'
        d.append(x.replace('"', "").replace(',', ''))
    return d


def get_total_number_of_trades(symbol):
    data = nse.get_today_ohlc_data(symbol)
    # print(data)
    data = data.strip().split("\n")
    comma_sep = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
    data = comma_sep.split(data[1].strip())
    x = clean_it(data)
    _open = float(x[2])
    high = float(x[3])
    low = float(x[4])
    close = float(x[7])
    prev_close = float(x[5])
    volume = int(x[11])
    value = float(x[12])
    no_of_trades = int(x[13])
    return _open, high, low, close, prev_close, volume, value, no_of_trades


def update_instrument(symbol):
    try:
        data = symbol_info(symbol)
        _open, high, low, close, prev_close, volume, value, no_of_trades = get_total_number_of_trades(symbol)
        listing_date = datetime.strptime(data["metadata"]["listingDate"], '%d-%b-%Y')
        if data["metadata"]["lastUpdateTime"] == "-":
            updated_date = datetime.now()
        else:
            updated_date = datetime.strptime(data["metadata"]["lastUpdateTime"], '%d-%b-%Y %H:%M:%S')
        ohlc_date = datetime(updated_date.year, updated_date.month, updated_date.day)
        instrument_summary = {'symbol': data["info"]["symbol"],
                              'name': data["info"]["companyName"],
                              'industry': data["metadata"]["industry"],
                              'isin': data["metadata"]["isin"],
                              'series': data["metadata"]["series"],
                              'status': data["metadata"]["status"],
                              'listing_date': listing_date,
                              'last_update_time': updated_date,
                              'sector_index': data["metadata"]["pdSectorInd"].strip(),
                              'face_value': data["securityInfo"]["faceValue"],
                              'issued_cap': data["securityInfo"]["issuedCap"],
                              "open": _open,
                              "high": high,
                              "low": low,
                              "close": close,
                              "prev_close": prev_close,
                              "total_volume": volume,
                              "total_value": value,
                              "total_trade": no_of_trades,
                              "delivery": data["securityWiseDP"]['deliveryQuantity'],
                              }

        # mongo_data = {"symbol": symbol, "series": data["metadata"]["series"], "market_type": "N",
        #               "exchange": "NSE",
        #               "isin": data["metadata"]["isin"],
        #               "open": _open,
        #               "high": high,
        #               "low": low,
        #               "close": close,
        #               "prev_close": prev_close,
        #               "total_volume": volume,
        #               "total_value": value,
        #               "total_trade": no_of_trades, "delivery": data["securityWiseDP"]['deliveryQuantity'],
        #               "date": ohlc_date}

        # print(instrument_summary)
        # mongodb.write_historical_data([mongo_data])
        mongodb.write_instrument_data(symbol, instrument_summary)
    except Exception as e:
        print(e)


def day_before_today(no_of_days):
    day = datetime.today() - timedelta(days=no_of_days)
    return day


def update_today_index(symbol):
    dt = day_before_today(1)
    dt1 = day_before_today(0)
    x = investing.get_specific_date_historical_data(symbol, datetime(dt.year, dt.month, dt.day),
                                                    datetime(dt1.year, dt1.month, dt1.day))
    data = json.loads(x.strip())
    for t, o, h, l, c in zip(data["t"], data["o"], data["h"], data["l"], data["c"]):
        mongo_data = {"symbol": investing_name[symbol], "series": "INDEX",
                      "investing_id": symbol, "open": o, "high": h, "low": l, "close": c,
                      "date": datetime.fromtimestamp(int(t))}
        # print(mongo_data)
        mongodb.write_historical_data([mongo_data])

# for x in instruments:
#     print(x)
#     update_instrument(x)


# for x in investing_index:
#     update_today_index(x)

# xx = nse.list_of_all_securities()[290:]
# for x in tqdm.tqdm(xx):
#     print(x)
# update_instrument(x)a
