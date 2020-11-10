# https://www.nseindia.com/api/monthly-reports?key=CM

import requests


def monthly_reports(key):
    headers = {
        'authority': 'www.nseindia.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': '_ga=GA1.2.2144872892.1604855871; _gid=GA1.2.1790079190.1604855871; nseQuoteSymbols=[{"symbol":"SBIN","identifier":null,"type":"equity"}]; ak_bmsc=607E14A61DEDC891D12B3BF78264F7846011B6CBCC13000050BEAA5FAE0F3F75~plAhftFA+Vbh8Ssga7SIObRthVpg5nIYHkql32fqlGNT4X7OSOx/fZmjV2meyZBJ9kzU86rSxU60qyxd9f9m1OBzbi6O7DdPwyfJFWfOiHTKcZ8rMF79BX3WlpT4DcnQrShX1RtHMXOpd8fHowjAvW70hTTeawr1a8cqWy7rbyRB57tke0I7E8Br7LleVjVkiFlZy2l4WaGZkca8eg8JdsRiX9XrW76XPhyOz20bPLX8OoMmiWxku7JqvXvNby3ldz; nsit=PETcHGmO6uWwPU-Y7v4rAmRc; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYwNTAzMDYxNSwiZXhwIjoxNjA1MDM0MjE1fQ.l4ELkOj4ptMBzIh-BcfvoncK6sHPsaWi9FfcLQU7fcU; RT="z=1&dm=nseindia.com&si=615c436d-6b02-4ca1-b413-73ea811277a5&ss=khc98h16&sl=4&tt=amj&bcn=%2F%2F684d0d39.akstat.io%2F"; bm_sv=558674CC60E7270975155396A47637D3~WC6atZsItDDzdNKu7SVOLkw6qJpEWixgBx5VTUvhoj8fC8s7bTFFdGoNWmT911rC02ciz+Y7+HyCsuQEU5fp8hj+fiKQgemZNxKzmqTYLSvut9t3ywbRSJ9qD7kaibzovYjz2b1UvZRLDHSPdxHg+4ppS0kn3pjhA6fSMbHZsDQ=',
    }

    params = (
        ('key', key),
    )

    response = requests.get('https://www.nseindia.com/api/monthly-reports', headers=headers, params=params)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get('https://www.nseindia.com/api/monthly-reports?key=CM', headers=headers)
    print(response.text)


monthly_reports("CM")
