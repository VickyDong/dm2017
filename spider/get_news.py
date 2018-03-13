import pymongo
from bs4 import BeautifulSoup
import requests

client = pymongo.MongoClient('localhost',27017)
news = client['news']
mil_list = news['mil_list']
mil_test = news['mil_test']


def get_news(url, data=None):
    try:
        web_data = requests.get(url, timeout=10)
        if int(web_data.status_code)==404:
            pass
        else:
            web_data.encoding = 'gbk'
            soup = BeautifulSoup(web_data.text,'lxml')
            title = soup.select('#cont_1_1_2 > h1')
            contents = soup.select('.left_zw > p')
            news = ''
            for i in range(len(contents)):
                news = news + contents[i].get_text().strip().replace('\u3000', '') + ' '
                data = {
                    'title': title[0].text.strip(),
                    'content': news,
                    'url':url,
                }
            if data != None:
                mil_test.insert_one(data)

    except :
        pass

db_urls = [item['url'] for item in mil_list.find()]
yi = [item['url'] for item in mil_test.find()]
y = set(yi)
x = set(db_urls)
rest = x-y


for item in rest:
    get_news(item)

