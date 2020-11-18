from datetime import datetime, timedelta
import json
import requests

headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320',
    'Content-Type': 'text/plain',
    'Origin': 'https://tvc-invdn-com.akamaized.net',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://tvc-invdn-com.akamaized.net/web/1.12.27/index59-prod.html?carrier=81d125a138fc6f6eae835cd3c2994024&time=1605464798&domain_ID=56&lang_ID=56&timezone_ID=23&version=1.12.27&locale=en&timezone=Asia/Kolkata&pair_ID=17940&interval=D&session=session&prefix=in&suffix=&client=1&user=0&family_prefix=tvc4&init_page=instrument&sock_srv=https://stream171.forexpros.com:443&m_pids=&watchlist=&geoc=IN&site=https://in.investing.com',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

investing = requests.Session()
response = investing.get('https://in.investing.com/', headers=headers)


def _historical_data(symbol, from_date, to_date):
    response = requests.get(
        f'https://tvc4.forexpros.com/81d125a138fc6f6eae835cd3c2994024/1605464798/56/56/23/history?symbol={symbol}&resolution=D&from={from_date}&to={to_date}',
        headers=headers)
    return response.text


def historical_data(symbol, limit_in_days=10):
    dates = get_dates(5000, limit_in_days)
    arr = dict(t=[], o=[], h=[], l=[], c=[])
    for date in dates:
        # print(date[0], date[1])
        # print(int(datetime.timestamp(date[0])), int(datetime.timestamp(date[1])))
        data = _historical_data(symbol, int(datetime.timestamp(date[0])), int(datetime.timestamp(date[1])))
        print(data)
        data = json.loads(data)
        if data['s'] == 'no_data':
            continue

        arr["t"] += data["t"]
        arr["o"] += data["o"]
        arr["h"] += data["h"]
        arr["l"] += data["l"]
        arr["c"] += data["c"]
    return arr


# from=1329330428&to=1351016826
#      1519066200 1544986200
def day_before_today(no_of_days):
    day = datetime.today() - timedelta(days=no_of_days)
    return day


def get_dates(shift, lmt):
    result = []
    times = lmt // shift
    for x in range(times):
        to_date = day_before_today(x * shift + (0 if x == 0 else +1))
        from_date = day_before_today(x * shift + shift)
        result.insert(0, (from_date, to_date))

    # left overs??
    left = lmt % shift
    st = times * shift
    if left > 0:
        to_date = day_before_today(st)
        from_date = day_before_today(lmt)
        result.insert(0, (from_date, to_date))
    return result


# investing_index = [ "172",]
# for inv in investing_index:
#     print(inv)
#     x = historical_data(inv, 20000)
#     print(x)
#     f = open(inv, 'w')
#     f.write(json.dumps(x))
#     f.close()
