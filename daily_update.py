from core import nse
import json

instruments = ["SBIN", "RELIANCE", "ASHOKLEY", "BHARTIARTL", "PVR", "IRCTC", "ITC", "INFY", "POWERGRID", "ACC"]

investing_index = ["17940", "39929", "14958", "166", "172", "175", "40820", "37426"]


def symbol_info(symbol):
    instrument_info = json.loads(nse.equity_info(symbol))
    instrument_trade_info = json.loads(nse.equity_trade_info(symbol))
    return {**instrument_info, **instrument_trade_info}


x = symbol_info("SBIN")

cc = {'symbol': 'SBIN', 'companyName': 'State Bank of India', 'industry': 'BANKS', 'activeSeries': ['EQ'],
      'debtSeries': ['N5', 'N6'], 'tempSuspendedSeries': ['IL', 'N1', 'N2', 'N3', 'N4'],
      'isin': 'INE062A08066',
      'series': 'EQ', 'status': 'Listed',
      'listingDate': '01-Mar-1995', 'lastUpdateTime': '14-Nov-2020 19:35:00',
      'pdSectorPe': 27.34, 'pdSymbolPe': 12.51,
      'pdSectorInd': 'NIFTY BANK',
      'boardStatus': 'Main', 'tradingStatus': 'Active', 'tradingSegment': 'Normal Market',
      'classOfShare': 'Bond',
      'faceValue': 1, 'issuedCap': 8924611534,

      'lastPrice': 228.05, 'change': -1.3999999999999773, 'pChange': -0.6101547178034332,
      'previousClose': 229.45,
      'open': 232, 'close': 229.65,
      'vwap': 230.97,
      'lowerCP': '206.55',
      'upperCP': '252.35',
      'pPriceBand': 'No Band',
      'basePrice': 229.45,
      'intraDayHighLow': {'min': 227.75, 'max': 232.9, 'value': 228.05},

      'preOpenMarket': {
        'preopen': [{'price': 210, 'buyQty': 0, 'sellQty': 10}, {'price': 213.4, 'buyQty': 0, 'sellQty': 258},
                    {'price': 220.5, 'buyQty': 0, 'sellQty': 502}, {'price': 221, 'buyQty': 0, 'sellQty': 200},
                    {'price': 232, 'buyQty': 0, 'sellQty': 0, 'iep': True}, {'price': 245, 'buyQty': 239, 'sellQty': 0},
                    {'price': 248, 'buyQty': 100, 'sellQty': 0}, {'price': 250, 'buyQty': 50, 'sellQty': 0},
                    {'price': 252.35, 'buyQty': 102, 'sellQty': 0}], 'ato': {'buy': 72159, 'sell': 10036}, 'IEP': 232,
        'totalTradedVolume': 124405, 'finalPrice': 232, 'finalQuantity': 124405,
        'lastUpdateTime': '14-Nov-2020 18:07:09', 'totalBuyQuantity': 387724, 'totalSellQuantity': 466383,
        'atoBuyQty': 72159, 'atoSellQty': 10036}, 'noBlockDeals': True,
      'bulkBlockDeals': [{'name': 'Session I'}, {'name': 'Session II'}],
      'marketDeptOrderBook': {'totalBuyQuantity': 0, 'totalSellQuantity': 44707,
                              'bid': [{'price': 0, 'quantity': 0}, {'price': 0, 'quantity': 0},
                                      {'price': 0, 'quantity': 0}, {'price': 0, 'quantity': 0},
                                      {'price': 0, 'quantity': 0}],
                              'ask': [{'price': 229.65, 'quantity': 44707}, {'price': 0, 'quantity': 0},
                                      {'price': 0, 'quantity': 0}, {'price': 0, 'quantity': 0},
                                      {'price': 0, 'quantity': 0}],
                              'tradeInfo': {'totalTradedVolume': 7753219, 'totalTradedValue': 17907.61,
                                            'totalMarketCap': 20352576.6, 'ffmc': 8813009.2667673, 'impactCost': 0.03},
                              'valueAtRisk': {'securityVar': 18.1, 'indexVar': 0, 'varMargin': 18.1,
                                              'extremeLossMargin': 3.5, 'adhocMargin': 18.4, 'applicableMargin': 40},
                              'securityWiseDP': {'quantityTraded': 7753219, 'deliveryQuantity': 2345791,
                                                 'deliveryToTradedQuantity': 30.26,
                                                 'seriesRemarks': None, 'secWiseDelPosDate': '14-NOV-2020 EOD'}}

# print(x)
# influx_data = f"day,symbol={data['symbol']},series={data['series']},market_type={data['market_type']}," \
#               f"exchange=NSE,isin={ISIN[symbol]}" \
#               f" open={data['open']},high={data['high']},low={data['low']},close={data['close']}," \
#               f"prev_close={data['prev_close']},total_volume={data['total_volume']}," \
#               f"total_value={data['total_value']},total_trade={0 if data['total_trade'] is None else data['total_trade']}" \
#               f" {data['time']}"
