import requests
#also Security-wise Delivery Position (10-NOV-2020 EOD)
headers = {
    'authority': 'www.nseindia.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nseindia.com/get-quotes/equity?symbol=SBIN',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': 'nseQuoteSymbols=[{"symbol":"SBIN","identifier":null,"type":"equity"}]; ak_bmsc=1191083BD7A8A52338CA6CF9E27DB0CD75EFBD69767200002BA7AA5F700E890D~plUxslYiVFOGGVHUpp6oOTOS8L5E5iOf6y0/ktWBrFBHkZo5FbfS96wcZaKqZ/oTmtUZqVtebC24PanJ3rVdrufuYyiWtX7QH0vETmueR0cZGmctjQsxmOKIDMMt8eKu3ATPhV8cUENDhevKLsS7TY71V7h6rEWjZq6bloslMZ5rUe4aTNsQLm6m+DIdTTVl9F+YvI/BGDoEr9pXJLpHoLI3AEdGpK+GrDzvQr66lnTqLBvrh6eWPTPL3AHaIwwj99; nsit=44lWhjuCjx5oiMbUwP8wwY8W; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYwNTAyMDg5MiwiZXhwIjoxNjA1MDI0NDkyfQ.GT0sTlYhT9vEH3lsfTA0LCEv57FM1yFMXSimKaAo29M; bm_sv=249C5530B68EDAC09B8C8972D86F5DB0~oLBYk4WAw5FJ/7RwhC94eCKJ4kbgJX741jLPoFLzgbcgo3kPSLidiJL5b10uWd35eyM3i8lyeQnQ2VzxrHsAEbgLmkgGcXAYSBRNDnyJWk0pEnsfFQn636TJWKfeid26UD5WGN1VKtGb9cShAoslKeTzwNg1tVUNXbPOJPkjqsk=',
}

params = (
    ('symbol', 'SBIN'),
    ('section', 'trade_info'),
)

response = requests.get('https://www.nseindia.com/api/quote-equity', headers=headers, params=params)


