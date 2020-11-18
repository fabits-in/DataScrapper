from tqdm import tqdm

from datetime import datetime
import re
from core import nse
from core.server.MongoDB import MongoDB
import os.path
import time
import json

instruments = ["SBIN", "RELIANCE", "ASHOKLEY"]
investing_index = ["17940", "39929", "14958", "166", "172", "175", "40820", "37426"]

investing_name = {"17940": "Nifty 50", "39929": "BSE Sensex", "14958": "Nasdaq",
                  "166": "S&P 500", "172": "DAX", "175": "Euro Stoxx 50", "40820": "Shanghai",
                  "37426": "KOSPI"}

ISIN = {
    "SBIN": "INE062A01020",
    "RELIANCE": "INE002A01018",
    "ASHOKLEY": "INE208A01029",
    "BHARTIARTL": "INE397D01024",
    "PVR": "INE191H01014",
    "IRCTC": "INE335Y01012",
    "ITC": "INE154A01025",
    "INFY": "INE009A01021",
    "POWERGRID": "INE752E01010",
    "ACC": "INE012A01025"

}

index = ["NSEI", "BSESN", "IXIC", "DJI", "HSI", "N225", "KS11"]

mgdb = MongoDB()


def cache_all_historical_data(symbol):
    data = nse.historical_data(symbol, 15000)
    name = f"raw1/{symbol}.csv"
    f = open(name, 'w')
    f.write(data)
    f.close()


def store_mongo_data(arr):
    for i in tqdm(range(0, len(arr), 100)):
        sq = arr[i:i + 100]
        mgdb.write_historical_data(sq)
        # time.sleep(10)


def get_and_store_all_delivery():
    from datetime import date, timedelta

    sdate = date(2002, 1, 1)  # start date
    edate = date(2020, 11, 14)  # end date
    date_modified = sdate
    list = [sdate]

    while date_modified < edate:
        date_modified += timedelta(days=1)
        list.append(date_modified)

    for date in tqdm(list):
        day = date.day
        month = date.month
        if 1 <= date.day <= 9:
            day = '0' + str(date.day)
        if 1 <= date.month <= 9:
            month = '0' + str(date.month)

        import os.path
        if os.path.isfile(f"raw/{date.year}:{month}:{day}.csv"):
            continue

        try:
            x = nse.delivery_value(day, month, date.year)
            name = f"raw/{date.year}:{month}:{day}.csv"
            f = open(name, 'w')
            f.write(x)
            f.close()
        except:
            pass


def new_delivery_data(name, symbol):
    if not os.path.isfile(name):
        # print(name)
        return 0
    f = open(name, 'r')
    lines = f.read().strip().split("\n")
    data = {}
    ok = 0

    if len(lines[0].split(",")) > 1:
        for i in range(1, len(lines)):
            elem = lines[i].split(",")
            if elem[2] == "EQ":
                data[elem[1]] = int(elem[3])
    else:
        for i in range(len(lines)):
            elem = lines[i].split(",")
            if len(elem) > 1 and elem[1] == 'Settlement Type <N>':
                continue
            if len(elem) > 1 and elem[1] == 'Settlement Type <D>':
                continue
            if elem[0] == "Record Type":
                ok = 1
                continue
            if ok:
                if elem[3] == "EQ":
                    data[elem[2]] = int(elem[5])

    f.close()
    val = data.get(symbol, 0)
    # if val == 0:
    #     print("-", name)
    return val


def clean_it(data):
    d = []
    for x in data:
        if x == '':
            x = '0'
        if x == '"-"':
            x = '-1'
        d.append(x.replace('"', "").replace(',', ''))
    return d


def process_historical_csv(symbol):
    name = f"raw1/{symbol}.csv"
    f = open(name, 'r')
    all_mongo = []
    for x in f.readlines():
        comma_sep = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
        data = comma_sep.split(x.strip())
        data = clean_it(data)
        if data[1] == 'EQ':
            date = datetime.strptime(data[0], '%d-%b-%Y')
            # timestamp = int(datetime.timestamp(date))
            series = data[1]
            _open = float(data[2])
            high = float(data[3])
            low = float(data[4])
            close = float(data[7])
            prev_close = float(data[5])
            volume = int(data[11])
            value = float(data[12])
            trades = float(data[13])
            day = date.day
            month = date.month
            if 1 <= date.day <= 9:
                day = '0' + str(date.day)
            if 1 <= date.month <= 9:
                month = '0' + str(date.month)
            name = f"raw/{date.year}:{month}:{day}.csv"
            delivery = new_delivery_data(name, symbol)
            # if delivery == 0:
            #     print(date, delivery)

            mongo_data = {"symbol": symbol, "series": series, "market_type": "N", "exchange": "NSE",
                          "isin": ISIN[symbol], "open": _open, "high": high, "low": low, "close": close,
                          "prev_close": prev_close, "total_volume": volume, "total_value": value,
                          "total_trade": 0 if trades == '' else trades, "delivery": delivery, "date": date}

            # print(mongo_data)
            # break
            all_mongo.append(mongo_data)
    store_mongo_data(all_mongo)
    f.close()


def process_index_data(symbol):
    f = open(f"raw2/{symbol}")
    all_mongo = []
    data = json.loads(f.read().strip())
    for t, o, h, l, c in zip(data["t"], data["o"], data["h"], data["l"], data["c"]):
        mongo_data = {"symbol": investing_name[symbol], "series": "INDEX",
                      "investing_id": symbol, "open": o, "high": h, "low": l, "close": c,
                      "date": datetime.fromtimestamp(int(t))}
        all_mongo.append(mongo_data)
    f.close()
    store_mongo_data(all_mongo)


def update_specific_date_data(symbol):
    dt = datetime(2020, 11, 17)
    x = nse.get_ohlc_data(symbol, dt).strip().split("\n")[1]
    comma_sep = re.compile(r",(?=(?:[^\"']*[\"'][^\"']*[\"'])*[^\"']*$)")
    data = comma_sep.split(x.strip())
    data = clean_it(data)
    if data[1] == 'EQ':
        date = datetime.strptime(data[0], '%d-%b-%Y')
        # timestamp = int(datetime.timestamp(date))
        series = data[1]
        _open = float(data[2])
        high = float(data[3])
        low = float(data[4])
        close = float(data[7])
        prev_close = float(data[5])
        volume = int(data[11])
        value = float(data[12])
        trades = float(data[13])
        day = date.day
        month = date.month
        if 1 <= date.day <= 9:
            day = '0' + str(date.day)
        if 1 <= date.month <= 9:
            month = '0' + str(date.month)
        name = f"raw/{date.year}:{month}:{day}.csv"
        delivery = new_delivery_data(name, symbol)
        # if delivery == 0:
        #     print(date, delivery)

        mongo_data = {"symbol": symbol, "series": series, "market_type": "N", "exchange": "NSE",
                      "isin": ISIN[symbol], "open": _open, "high": high, "low": low, "close": close,
                      "prev_close": prev_close, "total_volume": volume, "total_value": value,
                      "total_trade": 0 if trades == '' else trades, "delivery": delivery, "date": date}

        mgdb.write_historical_data([mongo_data])


if __name__ == '__main__':
    # update 17 data missed
    for symbol in instruments:
        update_specific_date_data(symbol)

    # for symbol in instruments:
    #     print(symbol)
    #     process_historical_csv(symbol)
    #     insert_all_historical_data(symbol)
    #
    # insert_all_historical_data("SBIN")
    # get_and_store_all_delivery()
    # process_historical_csv("SBIN")
    # from datetime import datetime
    #
    # x = int(datetime.timestamp(datetime.strptime("13-Nov-1997", "%d-%b-%Y")))
    # print(x)

    # for x in investing_index:
    #     process_index_data(x)
