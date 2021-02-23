import csv
import io
import json

import requests


def get_techinical_data(date):
    url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_" + date + ".csv"
    req = requests.get(url)
    url_content = req.content
    reader = csv.DictReader(io.StringIO(url_content.decode("utf-8")))
    return list(reader)

print(get_techinical_data("22022021"))
