import json
from threading import Thread

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from queue import Queue

import core.ticker_tape

data = Queue()
urls = Queue()


def download():
    while True:
        print(urls.qsize())
        url = urls.get()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        jsondata = soup.find("script", {"id": "__NEXT_DATA__"})
        jsondata = json.loads(jsondata.string)
        data.put(json.dumps(jsondata))
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


process_list()

for i in range(10):
    worker = Thread(target=download)
    worker.setDaemon(True)
    worker.start()

urls.join()

print("DONE...")
f = open("raw", 'w')
while not data.empty():
    txt = data.get()
    f.write(txt + "\n")

f.close()
print("FINISHED")
