import nse

instrument_info = nse.equity_info("SBIN")
instrument_trade_info = nse.equity_trade_info("SBIN")

print(instrument_info)
print(instrument_trade_info)

#
# "symbol"
# "isin"
# "status"
# "date of listing"
# "Industry"
# "P/E"
# "Sectoral_Index P/E"
# "Sectoral_Index"
# "Board Status"
# "Trading Status"
# "Trading Segment"
# "Session No."
# "SLB"
# "Class of Shares"
# "Derivatives"
# "Face Value"
# "List Issued Capital"
# "Surveillance"
# "Total Market Cap"
# "Free Float Market Cap"
# "Impact cost"
# -----
# "PREV. CLOSE"
# "OPEN"
# "HIGH"
# "LOW"
# "CLOSE"
# "VWAP"
# "LOWER BAND"
# "UPPER BAND"
# "PRICE BAND"
# "ADJUSTED PRICE"
# "Traded Volume"
# "Traded Value"
# "Value at Risk"
# "Security VaR"
# "Index VaR"
# "VaR Margin"
# "Extreme Loss Rate"
# "Adhoc Margin"
# "Applicable Margin Rate"
# ----
# "52_OPEN"
# "52_HIGH"
# "52_LOW"
# "52_CLOSE"
