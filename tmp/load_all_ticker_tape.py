import json
from threading import Thread

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from queue import Queue

import core.ticker_tape

data = Queue()
urls = Queue()

import logging

logpath = "raw"
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
ch = logging.FileHandler(logpath)
ch.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(ch)


def download():
    while True:
        print(urls.qsize())
        url = urls.get()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        json_data = soup.find("script", {"id": "__NEXT_DATA__"})
        if json_data:
            json_data = json.loads(json_data.string)
            logger.info(url + " #### " + json.dumps(json_data))
        urls.task_done()


def process_list():
    with open("list", "r") as f:
        for line in tqdm(f.readlines()):
            line = line.split(",")
            link = line[1].strip()
            name = line[0].strip()
            url = core.ticker_tape.generate_all_urls(link)
            for x in url:
                urls.put(x)


# process_list()
#
# for i in range(10):
#     worker = Thread(target=download)
#     worker.setDaemon(True)
#     worker.start()
#
# urls.join()
#
# print("DONE...")

f = open("raw")
i = 1
c = 0
f1 = open(f"s{i}", 'w')
chunk = 5000
line = f.readline()
while line != '':
    f1.write(line)
    c += 1
    if c == chunk:
        c = 0
        i += 1
        f1.close()
        f1 = open(f"s{i}", 'w')
    line = f.readline()
f.close()
f1.close()
