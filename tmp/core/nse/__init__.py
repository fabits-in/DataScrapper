from datetime import datetime, timedelta
import requests
import json
import re
from bs4 import BeautifulSoup

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

headers_nse1 = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www1.nseindia.com/live_market/dynaContent/live_watch/live_index_watch.htm',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

headers_tickertape = {
    'authority': 'api.tickertape.in',
    'accept': 'application/json, text/plain, */*',
    'accept-version': '4.0.0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.tickertape.in',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.tickertape.in/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': '_ga=GA1.2.951469948.1606036010; _gid=GA1.2.2104854695.1606036010; _gat=1; x-lp-tk=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbiI6ZmFsc2UsImlhdCI6MTYwNjAzNjAxMCwiZXhwIjoxNjA2MDY0ODEwfQ.PGUN_DMtxjYOAkjjDNMBx-cZfYihdofG96dCeLuV8jA; _gcl_au=1.1.974583058.1606036010; x-lp-auth=bf7cc96eca21d65900c722321473a868823bf419a3564e9a6af74e2a822643fe; _hjTLDTest=1; _hjid=baba9d4b-12dc-4c45-b10b-9933094769ff; _hjFirstSeen=1; WZRK_G=9e5767c48d244f57af327d878bc4f752; WZRK_S_445-48R-495Z=%7B%22p%22%3A1%2C%22s%22%3A1606036010%2C%22t%22%3A1606036010%7D; hide-bts-banner=true',
}

cookies_nse1 = {
    'NSE-TEST-1': '1910513674.20480.0000',
    'ak_bmsc': '7B22EC0C6D1C8B2724964E9E83D6C0F2312C8AD4A26900008032BA5FC4687E23~pl3w7ol1LZ6IMVzGHxpqRRb2RGOiCQqx5n3CshKFhQwKeuJNDvAzafEH63zuKDVyTOyHWNY9pMSoIjj6mtx7KdjwS27ylVC7nRAfSpQhWGqp1nfVsb4afuV59v22S+aCr0E6TpbAE1UfJYCZG6JPvVF25yFc2wv8jiDdhVO2LsJAwsiPs2MVc4FO5zOICaMKazV4Rk0nqmb+3NVAIP76DHoKBb45LtDEsrA6AkHMNmRRh+RFXm9nbIZQofBR/tCfPk',
    'bm_sv': '015E4C4FB30A432BC2D126B2EC5DAE26~E/d3mCz44qP2FkIgTd/gcE6M2vNl5NHrZO45FVb+6Dk12gSrcNLeQrQx0pXwO8NZ940SMjL3liPWXRPMhSYnV1IPdUigbiEHTYrxH8ZQwlTkYm2RqLefSOQZz15jMtc217+lN9vTjovHQpu0cDZFn4ykpGEffkZlzCkjurjljOY=',
    'RT': 'z=1&dm=nseindia.com&si=32b59acc-4499-4f00-a75c-13fc2fbb2724&ss=khsxn70f&sl=1&tt=27m&bcn=%2F%2F684d0d3d.akstat.io%2F&ld=289&ul=81x&hd=856',
}

nse = requests.Session()
nse.get("https://www.nseindia.com/", headers=headers)


def equity_trade_info(symbol):
    response = nse.get(f'https://www.nseindia.com/api/quote-equity?symbol={symbol}&section=trade_info', headers=headers)
    return response.text


def equity_info(symbol):
    response = nse.get(f'https://www.nseindia.com/api/quote-equity?symbol={symbol}', headers=headers)
    return response.text


def _historical_data(symbol, from_date, to_date, series='["EQ", "BE"]'):
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
    # left overs
    left = lmt % shift
    st = times * shift
    if left > 0:
        to_date = date_format(day_before_today(st))
        from_date = date_format(day_before_today(lmt))
        result.insert(0, (from_date, to_date))
    return result


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


def delivery_value(day, month, year):
    response = nse.get(f"https://archives.nseindia.com/archives/equities/mto/MTO_{day}{month}{year}.DAT", timeout=2)
    return response.text


def financial_results():
    response = nse.get(
        f'https://www1.nseindia.com/corporates/corpInfo/equities/results_Nxbrl.jsp?param=01-Jul-202030-Sep-2020Q2UNNCNERELIANCE&seq_id=1093626&industry=-&viewFlag=N&frOldNewFlag=N',
        headers=headers)
    return response.text


def list_of_all_securities():
    response = nse.get("https://www1.nseindia.com/corporates/datafiles/LDE_EQUITIES_MORE_THAN_5_YEARS.csv",
                       headers=headers)

    data = response.text
    data = data.split("\n")
    result = []
    for x in data[1:]:
        result.append(x.split(",")[0][1:-1])
    return result


def holding_shares(table):
    response = nse.get(
        f'https://www1.nseindia.com/corporates/shldStructure/ShareholdingPattern/shp_{table}.jsp?ndsId=153247&symbol=RELIANCE&countStr=0|0|0|0|0|0|0|0|0|0|0|0|0|0|NEW_1|0|N&asOnDate=30-Sep-2020&RevisedData=N',
        headers=headers)
    return response.text


def list_of_all_results(symbol):
    params = (
        ('index', 'equities'),
        ('from_date', '01-01-1981'),
        ('to_date', '21-11-2020'),
        ('symbol', symbol),
        ('issuer', 'State Bank of India'),
        ('period', 'Quarterly'),
    )
    response = nse.get('https://www.nseindia.com/api/corporates-financial-results', headers=headers, params=params)
    return response.text


def get_result(params, seq_id):
    params = (
        ('index', 'equities'),
        ('params', params),
        ('seq_id', seq_id),
        ('industry', '-'),
        ('frOldNewFlag', ''),
        ('ind', 'A'),
        ('format', 'New'),
    )

    response = nse.get('https://www.nseindia.com/api/corporates-financial-results-data', headers=headers,
                       params=params)
    return response.text


def parse_old_result_table(url):
    response = nse.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    info = soup.find_all("table", attrs={"class": "table table-bordered"})[0]
    data = soup.find_all("table", attrs={"class": "table table-bordered"})[1]
    meta = {}
    k = None
    for x in info.find_all("td"):
        if x.get("class")[0] == "tablehead":
            k = x.text.strip()
        if x.get("class")[0] == "t1":
            meta[k] = x.text.strip()

    result = {}
    for x in data.find_all("tr"):
        td = x.find_all("td")
        if len(td) == 2:
            result[td[0].text.strip()] = td[1].text.strip()

    return meta, result


# parse_old_result_table("1")

# https://www.nseindia.com/companies-listing/corporate-filings-actions

# print(financial_results())


def get_stock_industry_and_sector():
    data = '{"match":{"mrktCapf":{"g":0,"l":9999999999}},"sortBy":"mrktCapf","sortOrder":-1,"sids":[],"project":[' \
           '"subindustry","mrktCapf","lastPrice","apef"],"offset":0,"count":2000} '
    response = requests.post('https://api.tickertape.in/screener/query', headers=headers_tickertape, data=data)
    return response.text


def indian_indices():
    response = requests.get(
        'https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/liveIndexWatchData'
        '.json', headers=headers_nse1, cookies=cookies_nse1)
    return response.text


def get_world_indices():
    cookies = {
        'identifier': '583fd8b42da7afe6e567ae0efd806af0',
        'adBlockerNewUserDomains': '1598271681',
        'welcomePopup': '1',
        'OB-USER-TOKEN': '27599eda-cf41-4f7a-ba2d-cda542921e9c',
        '_hjid': '8ce9b1b1-30c3-48e7-918a-645e379985d0',
        '_fbp': 'fb.1.1603470232009.311395598',
        'udid': '2438df4e1ffc40f934e2e10af4b94a97',
        'G_ENABLED_IDPS': 'google',
        'smd': '2438df4e1ffc40f934e2e10af4b94a97-1606036614',
        '_gid': 'GA1.2.453440638.1606036616',
        '_tz_id': 'b538964f553622d023f3a6558192382f',
        'geoC': 'IN',
        'StickySession': 'id.28638332397.576in.investing.com',
        'PHPSESSID': 'unjne7ni2b1u3kppuff7p5a6av',
        'SKpbjs-unifiedid': '%7B%22TDID%22%3A%22f5db6ca8-e6a0-407d-962f-ec3beed22ef1%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222020-10-22T09%3A18%3A16%22%7D',
        'SKpbjs-unifiedid_last': 'Sun%2C%2022%20Nov%202020%2009%3A18%3A16%20GMT',
        'SKpbjs-id5id': '%7B%22ID5ID%22%3A%22ID5-ZHMOPK3G1vcBg-xjIpo2uhXLE2wBqyomk0ne1CtgyQ%22%2C%22ID5ID_CREATED_AT%22%3A%222020-11-18T07%3A12%3A30.914Z%22%2C%22ID5_CONSENT%22%3Atrue%2C%22CASCADE_NEEDED%22%3Atrue%7D',
        'SKpbjs-id5id_last': 'Sun%2C%2022%20Nov%202020%2009%3A18%3A16%20GMT',
        'billboardCounter_56': '1',
        'prebid_page': '0',
        'prebid_session': '1',
        'gtmFired': 'OK',
        'r_p_s_n': '1',
        'comment_notification_219706551': '1',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Sun+Nov+22+2020+15%3A01%3A11+GMT%2B0530+(India+Standard+Time)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IN%3BWB',
        'OptanonAlertBoxClosed': '2020-11-22T09:31:11.053Z',
        '__gads': 'ID=c6e4445285ae5e00-227c523edfc4003c:T=1606037764:RT=1606037764:S=ALNI_MZ9P9igflz_mmJOPt-mjfacaBCl5w',
        '_ga_H1WYEJQ780': 'GS1.1.1606036692.12.1.1606039319.5',
        '_ga': 'GA1.2.847918899.1598271683',
        '_gat_UA-2555300-55': '1',
        'nyxDorf': 'MDcwZ285YThjP29hZDc1NmA7NT9lZmZkMjFhaGNgbmQ0M2ExMz81Y2NnbzBlaGNnZWw2YjRhYDdmb2E7NzRlODAyMGlvO2FuYzdvNg%3D%3D',
        'GED_PLAYLIST_ACTIVITY': 'W3sidSI6IlJaaVEiLCJ0c2wiOjE2MDYwMzkzMjgsIm52IjoxLCJ1cHQiOjE2MDYwMzkzMjAsImx0IjoxNjA2MDM5MzI2fSx7InUiOiJaQ24xIiwidHNsIjoxNjA2MDM5MzIwLCJudiI6MSwidXB0IjoxNjA2MDM5MjY1LCJsdCI6MTYwNjAzOTMyMH0seyJ1IjoieGd4MyIsInRzbCI6MTYwNjAzOTI2NSwibnYiOjEsInVwdCI6MTYwNjAzOTAxNiwibHQiOjE2MDYwMzkyNjV9XQ..',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'res-scheme': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://in.investing.com/indices/world-indices?additional-indices=on&c_id[]=all&major-indices=on&r_id[]=1&r_id[]=2&r_id[]=3&r_id[]=4&r_id[]=5',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    params = (
        ('additional-indices', 'on'),
        ('c_id/[/]', 'all'),
        ('major-indices', 'on'),
        ('r_id/[/]', ['1', '2', '3', '4', '5']),
        ('_', '1606038772804'),
    )

    response = requests.get('https://in.investing.com/indices/world-indices', headers=headers, params=params,
                            cookies=cookies)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get(
    #     'https://in.investing.com/indices/world-indices?additional-indices=on&c_id\[\]=all&major-indices=on&r_id\[\]=1&r_id\[\]=2&r_id\[\]=3&r_id\[\]=4&r_id\[\]=5&_=1606038772804',
    #     headers=headers, cookies=cookies)
    return response.text


def corporate_news():
    params = (
        ('index', 'equities'),
        ('from_date', '01-01-1985'),
        ('to_date', '24-11-2020'),
        ('symbol', 'ASHOKLEY'),
        ('issuer', 'Ashok Leyland Limited'),
    )

    response = nse.get('https://www.nseindia.com/api/corporate-announcements', headers=headers, params=params)
    print(response.text)

# corporate_news()
