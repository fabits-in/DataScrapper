import nse
from bs4 import BeautifulSoup

response = nse.financial_results()
soup = BeautifulSoup(response, 'html.parser')
keys = {}
values = []
str = ''
test={}

for i in range(len(soup.findAll('table', {'class': 'viewTable'}))):
     body = soup.findAll('table', {'class': 'viewTable'})[i]
     if i==0:
        for value in range(len(body.findAll('td'))):
             if value%2==0:
                  keys[body.findAll('td')[value].text]=body.findAll('td')[value+1].text
     elif i==1:
        for a in body.findAll('tr'):
               key=a.find('td', {'class': 't1'})
               value =a.find('td', {'class': 't0'})
               if key and value:
                test[key.text] = value.text
        keys['Part1']=test
     elif i==2:
        for b in range(len(body.findAll('td',{'class':'t0'}))):
            if body.findAll('td',{'class':'t0'})[b].text.find('Segment'):
                   values.append(body.findAll('td', {'class': 't0'})[b].text)
        for i in range(len(values)):
            if i%2==0:
                   test[values[i]]=values[i+1]
        keys['Segment']=test
print(keys)