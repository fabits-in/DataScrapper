from datetime import datetime, timedelta
import requests
import json
import re
from bs4 import BeautifulSoup


def get_bhavcopy_csv(day):
    csv_data = requests.get(f"https://archives.nseindia.com/products/content/sec_bhavdata_full_{day}.csv", timeout=10)
    return csv_data.text
