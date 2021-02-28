import csv
import io
import requests


def get_techinical_data(date):
    url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_" + date + ".csv"
    req = requests.get(url)
    url_content = req.content
    reader = csv.DictReader(io.StringIO(url_content.decode("utf-8")))
    return list(reader)

print(get_techinical_data("22022021"))

#Rustyt Start
import csv

csvFilePath = r'bhav.csv'
keys = ['SYMBOL', 'SERIES', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'LAST', 'PREVCLOSE', 'TOTTRDQTY', 'TOTTRDVAL', 'TIMESTAMP',
        'TOTALTRADES', 'ISIN']


def make_bhav_json_symbol_and_series(csvFilePath):
    # create a dictionary
    i=0
    x=''
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)


        for rows in csvReader:
            a=rows['SYMBOL']
            b=rows['SERIES']
            # print('{'+a+','+b+'}'+',')
            x=x+('{'+'"'+keys[0]+'"'+':'+'"'+a+'"'+','+'"'+keys[1]+'"'+':'+'"'+b+'"'+'}'+',')
        print(x)
        f = open(f"SymbolSeries.json",'w')
        f.write('['+x+']')




# Call the make_json function

def make_bhav_json(csvFilePath, jsonFilePath):
    # create a dictionary
    i=0
    a=[]
    x=''
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)


        for rows in csvReader:
            for b in keys:
             if b=='SYMBOL':
                 x = x + ("{"+'"' + b + '"' + ':' + '"' + rows[b] + '"' + ',')
             elif b=='ISIN':
                 x=x+('"'+b+'"'+':'+'"'+rows[b]+'"')
             else :
                 x=x+('"'+b+'"'+':'+'"'+rows[b]+'"'+',')
            x=x+'}'+','
            a.append(x)
        print(x)
        f = open(f"{jsonFilePath}",'w+')
        f.write("["+x+']')
# make_bhav_json(csvFilePath, 'bhav1.json')
# make_bhav_json_symbol_and_series(csvFilePath)


#Rustyt End


