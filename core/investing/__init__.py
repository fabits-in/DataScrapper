import requests
headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Content-Type': 'text/plain',
        'Origin': 'https://tvc-invdn-com.akamaized.net',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://tvc-invdn-com.akamaized.net/',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    }

params = (
        ('symbol', '169'),
        ('resolution', 'D'),
        ('from', '947872062'),
        ('to', '1038700799'),
    )
investing = requests.Session()
response=investing.get('https://tvc4.forexpros.com/4ba24e053beb906079de977313b48804/1605374563/56/56/23/history', headers=headers, params=params)


def streaming_chart(symbol,on,to,resolution):
    params = (
            ('symbol', symbol),
            ('resolution', resolution),
            ('from', on),
            ('to', to),
        )
    response=investing.get('https://tvc4.forexpros.com/4ba24e053beb906079de977313b48804/1605374563/56/56/23/history', headers=headers, params=params)
    return response.text

print(streaming_chart('169','441568782','1605374563','M'))