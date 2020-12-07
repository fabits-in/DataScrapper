import time
from datetime import datetime

from core import utils, nse
from core.server.MongoDB import MongoDB
from tqdm import tqdm

mongodb = MongoDB()


def process_bhavcopy_data(data):
    data = data.strip().split("\n")
    result = []
    for row in data[1:]:
        row = row.strip().split(",")
        symbol = row[0].strip()
        series = row[1].strip()
        date = row[2].strip()
        prev_close = 0 if row[3].strip() in ["-", ""] else float(row[3].strip())
        open_price = 0 if row[4].strip() in ["-", ""] else float(row[4].strip())
        high_price = 0 if row[5].strip() in ["-", ""] else float(row[5].strip())
        low_price = 0 if row[6].strip() in ["-", ""] else float(row[6].strip())
        last_price = 0 if row[7].strip() in ["-", ""] else float(row[7].strip())
        close_price = 0 if row[8].strip() in ["-", ""] else float(row[8].strip())
        avg_price = 0 if row[9].strip() in ["-", ""] else float(row[9].strip())
        quantity = 0 if row[10].strip() in ["-", ""] else float(row[10].strip())
        turnover = 0 if row[11].strip() in ["-", ""] else float(row[11].strip())
        trades = 0 if row[12].strip() in ["-", ""] else float(row[12].strip())
        delivery = 0 if row[13].strip() in ["-", ""] else float(row[13].strip())
        dct = {"symbol": symbol, "series": series, "prev_close": prev_close, "open": open_price, "high": high_price,
               "low": low_price, "last": last_price, "close": close_price, "avg": avg_price, "quantity": quantity,
               "turnover": turnover, "trades": trades, "delivery": delivery,
               "date": datetime.strptime(date, '%d-%b-%Y')}

        result.append(dct)

    return result


while True:
    now = datetime.now()
    # if 16 <= now.hour <= 18:
    try:
        today = utils.bhavcopy_date(now)
        task = mongodb.get_day_task(today)
        if not task:
            data = nse.get_bhavcopy_csv(today)
            data = process_bhavcopy_data(data)
            check_date = utils.bhavcopy_date(data[0]["date"])
            task1 = mongodb.get_day_task(check_date)
            if task1:
                break
            print("Updating data...")
            mongodb.write_historical_data(data)
            for row in tqdm(data):
                mongodb.write_instrument_data(row["symbol"], row)
            mongodb.update_day_task_ohlc(today)
        else:
            print("already done")

    except Exception as e:
        print(e)
    time.sleep(1800)
