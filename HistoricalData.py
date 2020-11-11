import requests

headers = {
    'authority': 'www.nseindia.com',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nseindia.com/get-quotes/equity?symbol=SBIN',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': 'nseQuoteSymbols=[{"symbol":"SBIN","identifier":null,"type":"equity"}]; nsit=w_v7Yoaxx78PKCa3AXgMuArm; ak_bmsc=BD301BF649682F149298EAB11B827A7E75EFBD73ED5B0000B07BAB5F6BFCE329~plnC0yGpLCQyZwz4lWBPJgOE69/EnSiWjuEGGksQ6n0Vj7iJIZUvvRZymUlusKraR6BBZqxB0KdSsJxU0fxJQqQWmTuAR2Bp+dDZPsdmQlmucrSJjFbV6pIKJ0JS5fBqDSqqpK3m0cQQ86IH3RLoeD/pvOSVp4ew0sZS8r4qFsj8NrAUA2MKfRzWxKHv9znLP+ZsI24yx89syAMXtccClP9xWES9Bw6me8ZT2FQgoc4+/w75nVGLtv0m5/Cm9lxDzn; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYwNTA3NjA1NSwiZXhwIjoxNjA1MDc5NjU1fQ.cB8EhFA4-J1fAXaLUyHhoh9mp4IQOVA2up3cd1ULTHQ; bm_sv=0444BA2ACC93C060EFA3E261C5254E77~EW/N13QvJErsknTR4Y+aYrY+zZDKI7F+535Uv3qcfvA9KmAt7Y1QJBQw8uyRpDM7TcdcQU768VgsfdOQzVAPO6GeRM5qRdtILfzP9bELJSAnv97DcQzBoNn94M7wM0NiPvSUNe/54FLsrTqCIepPY9Cc9Ahmn8jX8BhP2OrvGfA=',
}

params = (
    ('symbol', 'SBIN'),
    ('series', '/["EQ"/]'),
    ('from', '11-10-2020'),
    ('to', '11-11-2020'),
    ('csv', 'true'),
)

response = requests.get('https://www.nseindia.com/api/historical/cm/equity', headers=headers, params=params)

print (response.text)