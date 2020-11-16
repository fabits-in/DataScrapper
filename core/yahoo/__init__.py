import requests
import time

headers = {
    'authority': 'query1.finance.yahoo.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'accept': '*/*',
    'origin': 'https://finance.yahoo.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://finance.yahoo.com/chart/%5EDJI',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
}

investing = requests.Session()
response = investing.get('https://in.finance.yahoo.com/', headers=headers)


def streaming_chart(symbol, dmy_on, dmy_to, interval):
    time_object_on = time.strptime(dmy_on, "%d %b %Y")
    on = int(time.mktime(time_object_on))
    time_object_to = time.strptime(dmy_to, "%d %b %Y")
    to = int(time.mktime(time_object_to))
    params = (
        ('symbol', symbol),
        ('period1', on),
        ('period2', to),
        ('useYfId', 'true'),
        ('interval', interval),
        ('includePrePost', 'true'),
        ('events', 'div|split|earn'),
        ('lang', 'en-US'),
        ('region', 'US'),
        ('crumb', 'AC8D9NbajIk'),
        ('corsDomain', 'finance.yahoo.com'),
    )
    response = investing.get(f'https://query1.finance.yahoo.com/v8/finance/chart/%5E{symbol}', headers=headers,
                             params=params)
    return (response.text)


print(streaming_chart('NSEI', '01 Nov 2000', '3 Nov 2007', '1d'))
