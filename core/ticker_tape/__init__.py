import json

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_financials_income_data():
    response = requests.get(
        "https://www.tickertape.in/stocks/acc-ACC/financials?period=quarter&statement=income&view=normal")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(data.string)
    income_statement = data["props"]["pageProps"]["financialStatement"]
    result = []
    for statement in income_statement:
        dict_statement = {"display_period": statement["displayPeriod"], "date": statement["endDate"],
                          "total_revenue": statement["qIncTrev"], "ebitda": statement["qIncEbi"],
                          "pbit": statement["qIncPbi"], "net_income": statement["qIncNinc"],
                          "eps": statement["qIncEps"]}
        result.append(dict_statement)
    print(result)


def get_financials_balance_sheet_data():
    response = requests.get(
        "https://www.tickertape.in/stocks/reliance-industries-RELI/financials?period=annual&statement=balancesheet&view=normal")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(data.string)
    balance_sheet = data["props"]["pageProps"]["financialStatement"]
    result = []
    for statement in balance_sheet:
        dict_statement = {"display_period": statement["displayPeriod"], "date": statement["endDate"],
                          "current_assets": {"cash_and_short_term_investments": statement["balCsti"],
                                             "total_receivables": statement["balTrec"],
                                             "total_inventory": statement["balTinv"],
                                             "other_assets": statement["balOca"]},
                          "non_current_assets": {"loans_and_advances": statement["balNetl"],
                                                 "property": statement["balNppe"],
                                                 "goodwill_and_intangibles": statement["balGint"],
                                                 "long_term_investments": statement["balLti"],
                                                 "deferred_tax_assets": "",
                                                 "other_assets": statement["balOtha"]},
                          "current_liabilities": {"accounts_payable": statement["balAccp"],
                                                  "total_deposits": statement["balTdep"],
                                                  "other_current_liabilities": statement["balOcl"]},
                          "non_current_liabilities": {"total_long_term_debt": statement["balTltd"],
                                                      "deferred_tax_liabilities": statement["balDit"],
                                                      "other_liabilities": statement["balOthl"]},
                          "total_equity": {"common_stock": statement["balComs"],
                                           "additional_paid_in_capital": statement["balApic"],
                                           "reserves_and_surplus": statement["balRtne"],
                                           "minority_interest": statement["balMint"],
                                           "other_equity": statement["balOeq"]
                                           },
                          "total_liabilities_and_shareholders_equity": statement["balTlse"],
                          "total_common_shares_outstanding": statement["balTcso"]}
        result.append(dict_statement)
    print(result)


def get_financials_cash_flow_data():
    response = requests.get(
        "https://www.tickertape.in/stocks/reliance-industries-RELI/financials?period=annual&statement=cashflow")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(data.string)
    cash_flow = data["props"]["pageProps"]["financialStatement"]
    result = []
    for statement in cash_flow:
        dict_statement = {"display_period": statement["displayPeriod"], "date": statement["endDate"],
                          "Net Change in Cash": {"Cash from Operating Activities": statement["cafCfoa"],
                                                 "Cash from Investing Activities": statement["cafCfia"],
                                                 "Cash from Financing Activities": statement["cafCffa"]},
                          "Changes in Working Capital": statement["cafCiwc"],
                          "Capital Expenditures": statement["cafCexp"],
                          "Free Cash Flow": statement["cafFcf"]}
        result.append(dict_statement)
    print(result)


def get_isin(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find("script", {"id": "__NEXT_DATA__"})
    data = json.loads(data.string)
    sector = data["props"]["pageProps"]["securityInfo"]["gic"]["sector"]
    industry = data["props"]["pageProps"]["securityInfo"]["gic"]["industry"]
    isin = data["props"]["pageProps"]["securityInfo"]["isin"]
    return str(sector), str(industry), str(isin)


def get_stocks_list(name):
    result = []
    base = "https://www.tickertape.in"
    response = requests.get(f"https://www.tickertape.in/stocks?filter={name}")
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("a", {"class": "jsx-1528870203"})
    for a in data:
        result.append([a.string, base + a.get("href")])

    return result


def list_of_all_stocks():
    arr = []
    for x in range(26):
        x += 97
        arr.append(chr(x))
    arr.append("others")
    all_list = []
    for a in tqdm(arr):
        all_list += get_stocks_list(a)
    with open("list", "w") as f:
        for x in all_list:
            f.write(x[0] + "," + x[1] + "\n")


def process_list():
    with open("list", "r") as f:
        i = 0
        for line in tqdm(f.readlines()):
            i += 1
            if i < 147:
                continue
            line = line.split(",")
            link = line[1].strip()
            name = line[0].strip()
            sector, industry, isin = get_isin(link)

            with open("finalList", "a+") as f1:
                f1.write(name + "," + sector + "," + industry + "," + isin + "," + link + "\n")


# process_list()
# # list_of_all_stocks()
# # x = get_stocks_list("others")
# # print(x)
# # print(get_isin("https://www.tickertape.in/stocks/reliance-industries-RELI/"))


def generate_all_urls(base_url):
    overview = base_url
    forecast = base_url + "/forecasts?section=price"
    financial1 = base_url + "/financials?statement=income&view=normal&period=annual"
    financial2 = base_url + "/financials?period=quarter&statement=income&view=normal"
    financial3 = base_url + "/financials?period=annual&statement=balancesheet&view=normal"
    financial4 = base_url + "/financials?period=annual&statement=cashflow"
    peers = base_url + "/peers?table=valuation"
    news = base_url + "/news?type=mixed"
    holding = base_url + "/holdings?history=mfPctT&type=mixed"
    dividend = base_url + "/events?type=dividends"
    corp_action = base_url + "/events?type=corpActions"
    announce = base_url + "/events?type=announcements"
    legal_order = base_url + "/events?type=legal"
    url = [overview, forecast, financial1, financial2, financial3, financial4, peers, news, holding,
           dividend, corp_action, announce, legal_order]
    return url
