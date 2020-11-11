# https://www.nseindia.com/api/monthly-reports?key=CM

import requests


def daily_reports(url,key):

    headers = {
    'authority': 'www.nseindia.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nseindia.com/all-reports',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    }


    params = (
        ('key', key),
    )
    link = 'https://www.nseindia.com/api/'+url
    response = requests.get(link, headers=headers, params=params)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get('https://www.nseindia.com/api/monthly-reports?key=CM', headers=headers)
    print(response.text)

apiKeys=['circulars','latest-circulars','allMarketStatus','marketStatus','daily-reports','merged-daily-reports','monthly-reports'] # [2]< ,key=''
favKeys=['favCaptial','favDerivatives','favDebt']
keys=["CM",'INDEX','SLBS','SME','FO','COM','CD','NBF','WDM','CBM','IRD']

#daily_reports(apiKeys[0],'')
daily_reports(apiKeys[5],keys[2])
