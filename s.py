import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.nseindia.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': 'nseQuoteSymbols=[{"symbol":"SBIN","identifier":null,"type":"equity"}]; nsit=5VOAMyTUhEtnHHyOwc0lBgq4; ak_bmsc=AE50B42D88B14656A462F6C175969C9317030F4ED2770000D5C4AA5F984D150A~plAUS9AiguYYualBR8N4zWQsRMfOazDZmX68q6meQTYfyVjDOvdBrAFBD/kY6c3DuKT/eiLepEC7GIiKmmODlvwXlgT8IHohLrzAwtybkmFcZl0QHTje5I6IMJ9TI+t/TGjm8PnS9hRwiEGztqTEegWIQ6F+CrgqPM+J3DNsGbQuQflTYl0gRDdQaw8uY86pTa2hCwtmAf05Z5ncyBB1WK0s5+136EG6ZLrDqEKYA7z5tQ05U8XRiILxGuwXu5jNNI; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYwNTAyNzc3MSwiZXhwIjoxNjA1MDMxMzcxfQ.wYLKiPtaEIQnih1qmHxwwuLOxTU-MT4c0Il_kVDzj_0; bm_sv=13DC0D41F84814CC9CE759B7489A1EE8~9cdwWSlAiymCE9tf2rRZosbCtJ9qlUrX0vSeiHok5mcuRQ8UrS5Ne8UMEFAC7d+SkGjbXE9HH8DCVhk94SGLvlf+VOlOFswxsC1zb4Hai/2r23Gqh9I4MF9UHz21X62H6D/BIoTnTqV0dgiQacNf4837AQIXPPUCAz6GGtAlo0o=',
}

response = requests.get('https://www.nseindia.com/all-reports', headers=headers)

soup = BeautifulSoup(response.text,'html.parser')
csvUrls=[]
for a in soup.findAll('span',{'class':'reportDownloadIcon'}):
 url = a.find('a',href=True, attrs={'class':'pdf-download-link'})
 csvUrls.append(url)
print(csvUrls)