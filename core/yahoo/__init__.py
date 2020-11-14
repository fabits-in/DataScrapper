import requests
import time
headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Content-Type': 'text/plain',
        'Origin': 'https://tvc-invdn-com.akamaized.net',
        'Referer': 'https://tvc-invdn-com.akamaized.net/',
    }
investing = requests.Session()

def streaming_chart(symbol='169',dmy_on='30 Nov 00',dmy_to='1605374563',resolution='M'):
    time_object_on = time.strptime(dmy_on, "%d %b %y")
    on = time.mktime(time_object_on)
    time_object_to = time.strptime(dmy_to, "%d %b %y")
    to = time.mktime(time_object_to)
    params = (
            ('symbol', symbol),
            ('resolution', resolution),
            ('from', on),
            ('to', to),
        )
    response=investing.get('https://tvc4.forexpros.com/4ba24e053beb906079de977313b48804/1605374563/56/56/23/history', headers=headers, params=params)
    return response.text

print(streaming_chart('169','01 Nov 00','3 Nov 20','M'))