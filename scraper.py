#couldnt get this thing to work
#!/usr/bin/env python
# coding=utf-8
import sys
import sqlite3 as lite
import requests
import time
from bs4 import BeautifulSoup
import dataset
import time
import datetime
import urllib

db = dataset.connect('sqlite:///./database/data.sqlite')
db.begin()

date_start= '01/01/2014'
date_end ='15/07/2014'
request_session = requests.Session()
user_agent = {}
user_agent['Cache-Control']= 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
user_agent['Connection ']= 'Keep-Alive'
user_agent['Content-Type ']= 'text/html'
user_agent['Pragma ']= 'no-cache'

data_url = "http://218.248.45.171/fms/?module=public&action=workbillreport1"

html_get_src = request_session.get(data_url)


#check http://218.248.45.171/fms/includes/include/etamine.com/ajax/etamineajax.js
#does some magic

data_url = "http://218.248.45.171/fms/?module=public&action=workbillreport1"
payload = {"ifrom":str(date_start),"ito":str(date_end),"pmsid":":309"}
html_post_src = request_session.get(data_url,data=payload, headers = user_agent, cookies=html_get_src.cookies)


soup = BeautifulSoup(html_get_src.content)
table = ((soup.find_all("table", class_="mGrid"))[0]).contents[1]
rows = table.contents
for row in rows:
    if header:
        header = True
    elif rows != None and str(rows).strip() != "" and str(rows).strip() != "\n":
        continue
    else:
        columns = row.contents
        print columns

db.commit()
time.sleep(3)

    
