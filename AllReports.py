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
    'cookie': 'nseQuoteSymbols=[{"symbol":"SBIN","identifier":null,"type":"equity"}]; nsit=2IgsCTfCHvcDuwW2cQc-qzlM; bm_mi=CC004BBF6144435FC658CDE8F9A118F8~1fA0ErwizoxCM/HgduevhX3JLCnCYBG9I0fW9nCkS1bHM4QdfVInt+zmwG53G0HOn7/ZSp3Tb1cAiyt+6IkYDqgk8I8+0uBwEspDrJ/Y8TvsCoFQ9eUKcLJhtTB2qdu1t51lxM2pBt1JdC9B8YuxErOCIHSGth+QTA4CT5IIksOKBdUVdF2m/veSgEM+s9EXQC+WHWQxG/kxOOeeWE2JapJhbOBPnoeqvsZOsmhPBrWz7VLlMz8d49H7bdn4EUrvPlYv28rCT6yz82g1IZlmIIjdfzQa360h6JkE3gocmX8=; ak_bmsc=534BF2DDC3C239AC5749FDAFE467BF3D58DDDE4AB2320000FF0DAB5FDCA8DA2B~plHRpM2cFMV7+QZ8Mv6oIlRJCP3zLllG1z8g4huHCKqxHFQaEyaUdHnTNcsUP8Kl0TQBRsgxBxXUH9/zoCHvFjtYtDMiHF4sDtgbT4UlredE3Q49m4VUqWfB2ozKPVeJdqyYKSxd5vz4tInGgmkizHHaqCKLVoeAMLrSWabNwaTZH0iVgDCif+keuaJRZqANFxjjMdQrKLits3vDzIPyQHaZsk0X55Z3yQH36E2VIv4lviknObgLlSIaDe3J6V/TzE; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTYwNTA0NjQwNCwiZXhwIjoxNjA1MDUwMDA0fQ.r4-8liRf8X787pyzSgqfc1I2rIerlF-BaRZVDdD-rXs; bm_sv=BE1218DD4B05D5449F70A547C1B01B53~or05uIx/IoqcWmObeOHc6+XY11Rm9lUg6Fi1UaaD5kmTSMggaRTLp2MbtkzdY2jqHX5CDes6rNdamPIRvxXVd7hLlVmtCrPBhbQCsBFL45/jR5hhvVIJ9JksWr9sLSrDHnD2dZcjTn5IqpiJDuDf10NIWCp9Xmc6j3KIC+oC564=',
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
