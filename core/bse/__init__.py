from datetime import datetime, timedelta

from bs4 import BeautifulSoup

import requests
import time

headers = {
    'authority': 'www.bseindia.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.378',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en;q=0.9',
}

bse = requests.Session()
bse.get("https://www.bseindia.com", headers=headers)


def get_historical_form_data(form_url):
    data = bse.get(form_url, headers=headers)
    return get_view_state_and_event_validator(data.text)


def get_view_state_and_event_validator(html):
    soup = BeautifulSoup(html, "html.parser")
    view_state = soup.find("input", attrs={'name': "__VIEWSTATE"}).get("value").strip()
    event_validation = soup.find("input", attrs={'name': "__EVENTVALIDATION"}).get("value").strip()
    return view_state, event_validation


def historical_data():
    view_state, event_validation = get_historical_form_data(
        "https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx")
    data = {
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$btnDownload',
        '__VIEWSTATE': view_state,
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': event_validation,
        'ctl00$ContentPlaceHolder1$hiddenScripCode': '500112',
        'ctl00$ContentPlaceHolder1$smartSearch': 'SBIN',
        'ctl00$ContentPlaceHolder1$DMY': 'rdbDaily',
        'ctl00$ContentPlaceHolder1$txtFromDate': '02/11/1980',
        'ctl00$ContentPlaceHolder1$txtToDate': '20/11/2020'
    }

    response = bse.post('https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx', headers=headers,
                        data=data)

    print(response.text)


def list_of_scripts():
    view_state, event_validation = get_historical_form_data("https://www.bseindia.com/corporates/List_Scrips.aspx")
    data = {
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$lnkDownload',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': 'CF507786',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': event_validation,
        'ctl00$ContentPlaceHolder1$hdnCode': '',
        'ctl00$ContentPlaceHolder1$ddSegment': 'Equity',
        'ctl00$ContentPlaceHolder1$ddlStatus': 'Active',
        'ctl00$ContentPlaceHolder1$getTExtData': '',
        'ctl00$ContentPlaceHolder1$ddlGroup': 'Select',
        'ctl00$ContentPlaceHolder1$ddlIndustry': 'Select',
        'ctl00$ContentPlaceHolder1$btnSubmit': 'Submit'
    }

    response = bse.post('https://www.bseindia.com/corporates/List_Scrips.aspx', headers=headers, data=data)
    view_state, event_validation = get_view_state_and_event_validator(response.text)

    data = {
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$lnkDownload',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': 'CF507786',
        '__EVENTVALIDATION': event_validation,
        'ctl00$ContentPlaceHolder1$hdnCode': '',
        'ctl00$ContentPlaceHolder1$ddSegment': 'Equity',
        'ctl00$ContentPlaceHolder1$ddlStatus': 'Active',
        'ctl00$ContentPlaceHolder1$getTExtData': '',
        'ctl00$ContentPlaceHolder1$ddlGroup': 'Select',
        'ctl00$ContentPlaceHolder1$ddlIndustry': 'Select',
    }
    response = bse.post('https://www.bseindia.com/corporates/List_Scrips.aspx', headers=headers, data=data)
    print(response.text)


# list_of_scripts()
