#coding=gbk
import requests
from bs4 import BeautifulSoup
import pymongo
import re

client = pymongo.MongoClient('localhost',27017)
news = client['news']
mil_list = news['mil_list']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}


#抓取文章链接
def get_links_from(year,month,day):
    try:

        list_view = 'http://roll.mil.news.sina.com.cn/col/zgjq/{}-{}-{}.shtml'.format(str(year),
                                                                                        str(month).zfill(2),
                                                                                        str(day).zfill(2))
        web_data = requests.get(list_view, headers=headers, timeout=10)
        if int(web_data.status_code)==404:
            pass
        else:
            web_data.encoding = 'gbk'
            soup = BeautifulSoup(web_data.text, 'lxml')
            urls = soup.select('.linkNews > li > a')
            for url in urls:
                link = url.get('href')
                print(link)
                mil_list2.insert_one({'url':link})

    except :
        pass


for month in range(1,13):
    for day in range(0,32):
        get_links_from(2016,month,day)