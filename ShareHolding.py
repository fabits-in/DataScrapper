import nse
import requests
from bs4 import BeautifulSoup

response = nse.holding_shares('table2')
soup = BeautifulSoup(response,'html.parser')
keys={}
values=[]
str=''

for body in soup.findAll('table',{'width':'450'}):
    for a in body.findAll('tr'):
        key = a.find('td',{'class':'tablehead'})
        value = a.find('td',{'class':'t1'})
        keys[key.text]= value.text
for body in soup.findAll('table',{'width':['620' , '760'] }):
     for a in body.findAll('tr'):
         for key in range(len(a.findAll('td',{'class':'t1'}))):
          if key == 1:
           for value in a.findAll('td',{'class':'t0'}):
            str+=value.text + ','
           keys[a.findAll('td',{'class':'t1'})[key].text] = '['+str +']'
           str=''
print(keys)