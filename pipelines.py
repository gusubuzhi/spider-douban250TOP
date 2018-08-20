# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class DoubanPipeline(object):
    def __init__(self):
        self.host = settings['MONGODB_HOST']
        self.port = settings['MONGODB_PORT']
        self.dbname = settings['MONGODB_DBNAME']
        self.sheetname = settings['MONGODB_SHEETNAME']

        client = pymongo.MongoClient(self.host, self.port)
        db = client[self.dbname]
        self.post = db[self.sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

# ----------------------------------------------------
# import codecs
# import json
#
# class DoubanPipeline(object):
#     def __init__(self):
#         self.filename = codecs.open("dongguan.json",'w',encoding='utf-8')
#
#     def process_item(self, item, spider):
#         content = json.dumps(dict(item),ensure_ascii=False) +"\n"
#         self.filename.write(content)
#         return item
#
#     def close_spider(self,spider):
#         self.filename.close()