import json

import requests
from bs4 import BeautifulSoup


def get_financial_fata(stock_name, start_year, end_year, max_year, result_type):
    headers = {
        'authority': 'www.moneycontrol.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://www.moneycontrol.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'iframe',
        'referer': 'https://www.moneycontrol.com/stocks/company_info/print_financials.php?sc_did=SBI&type=profit_VI',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'A18ID=1611895915934.37304; _cb_ls=1; _cb=DmFFZMCzflbPBfBFRV; __io_r=google.com; __io_first_source=google.com; __io=3e5c9a8e0.7d6e8d537_1611895918306; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22www.google.com%22%7D; __gads=ID=81b96305a1260e99:T=1613570055:S=ALNI_MY5Y85ns2FXsDUgg5tjJOtAoUYyRQ; __utma=1.237627950.1611895918.1613587688.1613587688.1; __utmz=1.1613587688.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gcl_au=1.1.132186992.1613587699; OB-USER-TOKEN=27599eda-cf41-4f7a-ba2d-cda542921e9c; __utmz=129839248.1613808254.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); bm_sz=F6FDAA20BDA83D0C4F0F7CE162F65DC9~YAAQ5I0sMZfeCLV3AQAAlBRK2QrJiMtWV6hlC03xu+RVZF5LcgLUJngOs60dbqwwdg4YxtLouzgmafeh3G0ZVw8GPSQcXKt8V/QkgwvZOCZbhcruGYIyzh7mr4Dg3zMwyCjH8FIMgM66IPfQb1Wr9yEMxET8FLVtTJTbVISS4YZC1fJgWnu5QDD5E8cfpUFPN86t34Qj; _abck=D14630D99FE8611788F432F339958975~-1~YAAQ5I0sMZjeCLV3AQAAlBRK2QXK8RH1pANsw8/68PqWRiB3Uf7hDvak7QAzyVbcqADTXdBAmvNuC/hxVvfJaUfXXntAJFEz7yilLeOCX3I1Ie1BhenyI1k9PQo8kPwCvbTbazOMaguRAEg3S55srD+7GH7LLRF0XNPjvhHEcoURy8Z+4qhXBoBzFGcqiQgthpnbEou9N7ofNBobS9NGgXm4Vo6r5X1zFb0t9u5l4RMKUw6YEuCN+AjL8f0KL7nblXwKpeNdzAP9/XrlitlfJ3JRjdUvUxt9UN5EzPblDPLo2HHrqZHV2Nbz6zUWoDdENq+g4cu00SlKC/b0HuUsy5jqzqZtt0p2Glhd9cVjKABF2xDYo7/weQ==~-1~-1~-1; _gid=GA1.2.1990759450.1614258248; _cb_svref=null; bm_mi=ABD87EF45FD48994723277F233785217~1jCDGhxvkar+g+s0hH13LCkKea/qA8Cqop0YTq0796Ld3MSn5avjIDLAIEHI0YDtfTfT4DjvBPWYuFfQVKRzKJ0ZsD+X9olwZME7w+NRU5a1nLhnnNVuPqly+PWN/8lrZVsqFSTusAhayAnV5Y6r7yYPb67Hbc6bn+ivr/rN2vkwWBynGhCWJnr8zKwwa3xlYD8bWJmFfjddn6AWyHraCMON7/0CENMfLHKksEmyONjuCJzjWLBB0s8I145av/OUyAlML1FYa7B1k4nXkHFWNK+QOQmHlzwP0gVCJmLG9AAqkO/k69Ywy8v/cWa6c403; ak_bmsc=967520F6D45C89FF8A84ACBCF73E77E4312C8DE4655F000046A037600302367A~pl9V/sI8SEDnRdQyR8thzMAZGM/mgcGfnCMNPJDV+9k6DzwGJZYY9wfP8YmRtsOolSYBpyLHPCMiDxpk7uuxZRbdkFcP9Dj8MQXtIhGQE1a8Gjv5EY/Ii1OosWBzaWrT78s3k5Pp2lYQVqyu1EUq7pvjS0gdBQY6bpL5GdvXdfDWWVyCS0eu8oAb2zdtuXvzpehXtLgtyem+26oh2HN3cignZYCNOTxMjMQnpjgRqHcsx+LMrXEKv8HT8sXrBSP1OW/yonXJz53eitsb5k3JpI7Y3CwzlZg/wpJjc1Sa7AVYw=; PHPSESSID=6juaatlsblimc5qoicdaj0oh61; _ga_4S48PBY299=GS1.1.1614258247.7.1.1614258268.0; _ga=GA1.2.237627950.1611895918; __utma=129839248.202680670.1613808254.1614020564.1614258277.3; __utmc=129839248; _chartbeat2=.1604144572093.1614258277544.0000000011110101.CY64yGDF5gjI-H4gfBqE4k4-xgk2.3; _io_ht_r=1; __io_d=1_1860060068; __io_session_id=a216114ef.5fd14de0f_1614258277595; __io_nav_state43938=%7B%22current%22%3A%22%2Fstocks%2Fcompany_info%2Fprint_main.php%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previousDomain%22%3A%22%22%7D; __io_unique_43938=25; __io_visit_43938=1; bm_sv=647F87C2B9D40FA8E383688077DBB60C~UObSim48FnKQ8qOsHJnWvkzUzFvGVU3d6R14M9ZQbD6YVMJZ3vMpfvMKF1ryUcFe6U6nRcuYpARnEsoUb/VE2AiE0ZFjz8KOQj89XVvvYJNOBVh68Gkax/W99B3GAEA50+9m9QXr2vY74pi7khTAHII7aIbZ8SMnVKxhOAtBYxQ=; __utmb=129839248.3.10.1614258277; __io_lv=1614258337662',
    }
    params = (
        ('sc_did', stock_name),
    )

    data = {
        'nav': 'next',
        'type': result_type,
        'sc_did': stock_name,
        'start_year': start_year,  # 202003
        'end_year': end_year,  # 201603
        'max_year': max_year  # 202003
    }
    response = requests.post('https://www.moneycontrol.com/stocks/company_info/print_financials.php', headers=headers,
                             params=params, data=data).text
    soup = BeautifulSoup(response, features="lxml")
    html_data = soup.find_all("table")[3]
    table_data = [[cell.text for cell in row("td")] for row in html_data.find_all("tr")]
    result = {}
    for row in table_data:
        if len(row) >= 2:
            result[row[0]] = row[1:]
    return result


x = get_financial_fata("RI", 202012, 201912, 202012, "quarterly")
print(x)
