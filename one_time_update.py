from tqdm import tqdm

from core import nse
from core.server.InfluxDB import InfluxDB

instruments = ["SBIN", "RELIANCE", "ASHOKLEY", "BHARTIARTL", "PVR", "IRCTC", "ITC", "INFY", "POWERGRID", "ACC"]
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
influxdb = InfluxDB()


def insert_all_historical_data(symbol):
    data_arr = nse.historical_data(symbol, 15000)
    arr = []
    for data in data_arr:
        influx_data = f"day,symbol={data['symbol']},series={data['series']},market_type={data['market_type']}," \
                      f"exchange=NSE,isin={ISIN[symbol]}" \
                      f" open={data['open']},high={data['high']},low={data['low']},close={data['close']}," \
                      f"prev_close={data['prev_close']},total_volume={data['total_volume']}," \
                      f"total_value={data['total_value']},total_trade={0 if data['total_trade'] is None else data['total_trade']}" \
                      f" {data['time']}"
        arr.append(influx_data)

    for i in tqdm(range(0, len(arr), 10000)):
        sq = arr[i:i + 10000]
        influxdb.write_data(sq)


if __name__ == '__main__':

    for symbol in instruments:
        insert_all_historical_data(symbol)
