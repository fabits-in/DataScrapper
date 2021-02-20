import requests
from bs4 import BeautifulSoup


def getFinancialData(symbol, requestType, financialType, frequency):
    headers = {
        'authority': 'www.moneycontrol.com',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'accept': 'text/html, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'A18ID=1611895915934.37304; _cb_ls=1; _cb=DmFFZMCzflbPBfBFRV; __io_r=google.com; '
                  '__io_first_source=google.com; __io_lv=1611895918302; __io=3e5c9a8e0.7d6e8d537_1611895918306; '
                  '__io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22www.google.com%22%7D; __io_unique_43938=29; '
                  '_abck=D14630D99FE8611788F432F339958975~-1'
                  '~YAAQ340sMXh3K693AQAAIghFsAUuta9KKmyiFnIsUOJMADkZwhQ9jsd1DBD92WjXcNtnwQMRNhPVzt/flg26C6chL'
                  '+TlbKnWnlwkZMgOMPctVVCUsHc1niy0+2DwakA4thLD7U7+e+9eV968NdiQm7aPY0NoEltC0p'
                  '/iejo2WqHX5gmN2QRMNP71pNDwN05WbdAc7p9+s+fjsxdYtcUttkHmdb7YzjWRf9radC6Nydwqd/eQpLySoyJMV8RPRZR'
                  '/gQUh7viVuPvpXGNlKX2HNR+7FN73CjjyLZbfu7pcyGDWX0Hsfji4lpUTSEcZLkRf~-1~-1~-1; '
                  '_gid=GA1.2.2081419449.1613570051; '
                  '__gads=ID=81b96305a1260e99:T=1613570055:S=ALNI_MY5Y85ns2FXsDUgg5tjJOtAoUYyRQ; '
                  'bm_sz=A9B565E1621AF502E482478FCB861B3E'
                  '~YAAQr40sMc08JK93AQAAfCRSsQoeH09DMVC7rRtxJldlx4BBDlDPQb0zYFo1ZkjAxxU'
                  '+LIr478JqzxUH4cW2tRntYvl19u8TqQnjpuNQqyjJIpdgfmsI7BjmBy8EDFQRZdqQ4xoveYYm2DBXw9Ap8p3vQkAA8RtLULAUa0SsphHRVTitIeYPcw1rPmh7Eij/DUlhAQL0; bm_mi=F862E9E1041E18874A0188499960C584~cytEz4q4n05FX050PFAt1DFbqPWBZQ4ZByuRr33aLxpBPKokuPQaoBRQYZtzVSe/tZSc9GlhTWokTYb9xaueDAeplRM88noSvaw+h+qzdVhCWPRotKP/LKr78ZOrk2Ao27eWIfWbsbZ6vsh8dgAJ+JDbnWghGxtLC9fgKWBQqCzWHatNH/vUAoAdDlqioTAVwuGpgaKVDuOtDS7MxoBNdBtjkm+A4XeoFyntzgFLbmbDVJ55o3am+XtE++5nPIVgEuLKnOzIfLuAi96X5VYouw==; __utma=1.237627950.1611895918.1613587688.1613587688.1; __utmc=1; __utmz=1.1613587688.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=1.1.10.1613587688; ak_bmsc=76C7E9E43C88108D5423E1E6A609D01C312C8DAFD33B0000E6642D602834AF47~plh+DgA3nIudn9RhufN4vYvwuR6NjZmaLxjZWnr/SP9i+k1MsO8wIKx5rn9O5rdzRV7qFaGDcjRTC9ar5gUzNQH+1IlzsG6blnHTMpa/4SDcovQWayONRjcDQN8nRZq2qI6Tmoz5+s4qOXRsuZwpf2llfPXtdywSP0lg/Cq/I9yr+h9m1LRjIz8ZeTv4YNi5UAlgdyx/CeVW8fcOrGQ34dFWYW6sOIDcd0FY3V/9A8+Qj0ZaAV4fGW6kGn1ZFzZagpvywQX66FjssOM0r2cawV/HGcJmydvt92iO+02k3STpM=; _gcl_au=1.1.132186992.1613587699; _cb_svref=https%3A%2F%2Fwww.moneycontrol.com%2F; PHPSESSID=tlvr5oue0osh9q0duq13etl7r4; OB-USER-TOKEN=27599eda-cf41-4f7a-ba2d-cda542921e9c; _ga_4S48PBY299=GS1.1.1613587698.1.1.1613588121.0; _chartbeat2=.1604144572093.1613588123412.0000000000000001.D3CoLPDds_3MB-pG58Byz8ufCpaK-J.3; bm_sv=470D841AFA1B2B44AEF8CB6C4AA8A83D~rubaarqpVPt0VzvUjBkkzEQ7/NNM2gKwJu+eLGmWkLN3RkEu2r0wH2GIFUUBHXa4iio7gTjaTIin/IX/HALUC2manDqDa0P5omtTYpPSsMYxsqspMoFdKHUdZw5c8G733aPXSsPtX9qkM7N2RT0bhrAo+/sup3R/8F+RSTa863w=; _ga=GA1.2.237627950.1611895918; _chartbeat5=415,6674,%2Findia%2Fstockpricequote%2Fbanks-public-sector%2Fstatebankindia%2FSBI,https%3A%2F%2Fwww.moneycontrol.com%2Findia%2Fstockpricequote%2Fbanks-public-sector%2Fstatebankindia%2FSBI%23income_statement,BVzAYDDCl4SPBc-xJyDnHui4Cj2YdM,,c,D3yu2gBliwVxDqyr-5BQLAkXutpdj,moneycontrol.com,',
    }

    params = (
        ('classic', 'true'),
        ('referenceId', financialType),
        ('requestType', requestType),
        ('scId', symbol),
        ('frequency', frequency),
    )

    response = requests.get('https://www.moneycontrol.com/mc/widget/mcfinancials/getFinancialData', headers=headers,
                            params=params).text
    soup = BeautifulSoup(response, 'lxml')
    return soup.text

