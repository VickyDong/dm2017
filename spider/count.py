import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
news = client['news']
mil_list = news['mil_list']

while True:
    print(mil_list.find().count())
    time.sleep(5)