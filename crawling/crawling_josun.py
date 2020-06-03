import csv

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from datetime import datetime, timedelta

with open("example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

datetime_obj = datetime.strptime('2003-02-23', '%Y-%m-%d')
before_link = 'http://srchdb1.chosun.com/pdf/i_service/index_new.jsp?'

data = []
error_list = []
while str(datetime_obj.year) != '2020':
    years = 'Y=' + str(datetime_obj.year)+'&'
    months = 'M=' + str(datetime_obj.month)+'&'
    days = 'D=' + str(datetime_obj.day)+'&'
    link = before_link+years+months+days+'S=B'
    print(datetime_obj)

    try:
        with urllib.request.urlopen(link) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')

            all_divs = soup.find_all("a", {'target': '_blank'})
            for i, line in enumerate(all_divs):
                if line.text == "":
                    pass
                else:
                    date = str(datetime_obj.year) + str(datetime_obj.month).zfill(2) + str(datetime_obj.day).zfill(2)
                    news = '조선일보'
                    data.append([date, news, line.text])
    except Exception as err:
        error_list.append([date])


    datetime_obj = datetime_obj + timedelta(days=1)


file = open('josun.csv', 'w', encoding='utf-8', newline='')
csvfile = csv.writer(file)
for row in data:
    csvfile.writerow(row)
file.close()

print(error_list)

"""

import requests
from bs4 import BeautifulSoup

url = 'http://srchdb1.chosun.com/pdf/i_service/index_new.jsp?Y=2020&M=05&D=25&S=B'

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

name = soup.select('LeftContent > div:nth-child(6) > div > ul')
print(name)
#LeftContent > div:nth-child(6) > div > ul > li:nth-child(1) > a
"""