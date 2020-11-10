import requests

headers = {
    'authority': 'www.nseindia.com',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.207',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nseindia.com/get-quotes/equity?symbol=SBIN',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'nsit=yr2nbX9tttXqbVdhJsMUIMir; '
              'nseQuoteSymbols=[{"symbol":"SBIN","identifier":null,"type":"equity"}];'
              'nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYwNDk5OTY3MiwiZXhwIjoxNjA1MDAzMjcyfQ.tU0bewmoSUMIS5PeYI4OqSWMw7sg8hKLSuPcZOJsnTE; '

}

response = requests.get('https://www.nseindia.com/api/quote-equity?symbol=SBIN&section=trade_info', headers=headers)

print(response.text)
