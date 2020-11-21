from datetime import datetime, timedelta

import requests
import time

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
        f'https://www1.nseindia.com/corporates/shldStructure/ShareholdingPattern/shp_{table}.jsp?ndsId=153247&symbol=RELIANCE&countStr=0|0|0|0|0|0|0|0|0|0|0|0|0|0|NEW_1|0|N&asOnDate=30-Sep-2020&RevisedData=N',
        headers=headers)
    return response.text


def _historical_data(symbol, from_date, to_date, series='["EQ"]'):
    response = nse.get(
        f"https://www.nseindia.com/api/historical/cm/equity?symbol={symbol}&series={series}&from={from_date}&to={to_date}&csv=true",
        headers=headers)
    data = str(response.text) + "\n"
    return data


def historical_data(symbol, limit_in_days=10):
    dates = get_dates(700, limit_in_days)
    arr = ""
    for date in dates:
        data = _historical_data(symbol, date[0], date[1])
        arr += data

    return arr


def day_before_today(no_of_days):
    day = datetime.today() - timedelta(days=no_of_days)
    return day


def date_format(date_time):
    date_time = date_time.strftime("%d-%m-%Y")
    return date_time


def get_dates(shift, lmt):
    result = []
    times = lmt // shift
    for x in range(times):
        to_date = date_format(day_before_today(x * shift + (0 if x == 0 else +1)))
        from_date = date_format(day_before_today(x * shift + shift))
        result.insert(0, (from_date, to_date))

    # left overs??
    left = lmt % shift
    st = times * shift
    if left > 0:
        to_date = date_format(day_before_today(st))
        from_date = date_format(day_before_today(lmt))
        result.insert(0, (from_date, to_date))
    return result


def financial_results():
    response = nse.get(
        f'https://www1.nseindia.com/corporates/corpInfo/equities/results_Nxbrl.jsp?param=01-Jul-202030-Sep-2020Q2UNNCNERELIANCE&seq_id=1093626&industry=-&viewFlag=N&frOldNewFlag=N',
        headers=headers)
    return response.text


def delivery_value(day, month, year):
    response = nse.get(f"https://archives.nseindia.com/archives/equities/mto/MTO_{day}{month}{year}.DAT", timeout=2)
    return response.text


def get_today_ohlc_data(symbol):
    date1 = date_format(day_before_today(0))
    date2 = date_format(day_before_today(1))
    data = _historical_data(symbol, date2, date1)
    return data


def get_ohlc_data(symbol, date):
    date1 = date_format(date)
    date2 = date_format(date)
    data = _historical_data(symbol, date2, date1)
    return data

# delivery_value()
