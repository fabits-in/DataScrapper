# https://www.nseindia.com/api/monthly-reports?key=CM

import requests


def monthly_reports(key):
    headers = {
        'authority': 'www.nseindia.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.nseindia.com/get-quotes/equity?symbol=SBIN',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    }

    r = requests.get(f"https://www.nseindia.com/api/monthly-reports?key={key}", headers=headers)
    print(r.text)


monthly_reports("CM")
