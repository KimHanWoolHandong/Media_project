import csv

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from datetime import datetime, timedelta

exception_title = ['A', 'C', 'D']
exception_title2 = ['전면광고', '스포츠', '소설', '스포츠·소설', '주식시세', '정보통신', 'TV프로', '소설',
                    '바둑', '운세', '미술', '만화·운세·바둑', '책/문학', '책/신간', '책/학술', '책/어린이', '바둑/외국어/운세',
                    '바둑/외국어/옘세', '국제', '공연' ,'투데이', '오피니언', '자동차', 'TV프로그램',
                    'TV프로그램/바둑/외국어/운세', 'TV프로그램/운세/외국어/바둑', '만화/바둑/외국어',
                    'TV프로그램/운세/바둑/외국어', 'TV프로그램/외국어/운세/바둑']

datetime_obj = datetime.strptime('2000-01-01', '%Y-%m-%d')
before_link = 'https://www.donga.com/news/Pdf?ymd='

data = []
error_list = []
while str(datetime_obj.year) != '2020':
    years = str(datetime_obj.year)
    months = str(datetime_obj.month).zfill(2)
    days = str(datetime_obj.day).zfill(2)
    date = years+months+days
    link = before_link+date
    print(date)
    try:
        with urllib.request.urlopen(link) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            # content > div.section_kind > div:nth-child(3) > ul > li:nth-child(1) > div
            #name = soup.select('content > div.section_kind > div:nth-child(3) > ul')
            #print(name)

            all_divs = soup.find_all("div", {'class': 'section_txt'})
            #print(all_divs)
            for i, line in enumerate(all_divs):
                #print(i)
                title = line.find("span", {'class': 'tit'})
                #print(title.text)
                title_list = title.text.split()
                if title_list[1] == "경제" or (title_list[0][0] not in exception_title and title_list[1] not in exception_title2):
                    for text in line:
                        value = text.text
                        if len(value) == 0:
                            pass
                        elif value[0] in ['A', 'B', 'C', 'D']:
                            pass
                        else:
                            for report in text:
                                news = '동아일보'
                                #print(report.text)
                                data.append([date, news, report.text])
                else:
                    pass
    except Exception as err:
        error_list.append([date])

    datetime_obj = datetime_obj + timedelta(days=1)


file = open('donga.csv', 'w', encoding='utf-8', newline='')
csvfile = csv.writer(file)
for row in data:
    csvfile.writerow(row)
file.close()

print(error_list)


"""
    try:
        with urllib.request.urlopen(link) as response:
            html = response.read()  
            soup = BeautifulSoup(html, 'html.parser')
            
            all_divs = soup.find_all("div", {'class': 'section_text'})
            print(all_divs)
            for i, line in enumerate(all_divs):
                if line.text == "":
                    pass
                else:
                    date = str(datetime_obj.year) + str(datetime_obj.month).zfill(2) + str(datetime_obj.day).zfill(2)
                    news = '동아일보'
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