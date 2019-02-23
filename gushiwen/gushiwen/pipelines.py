# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GushiwenPipeline(object):
    def __init__(self):
        self.fp = None
        
    def open_spider(self,spider):
        print('开始爬虫……')
        self.fp = open('./data.txt','w')
        
    def process_item(self, item, spider):
        #将爬虫文件提交的item写入文件进行持久化存储
        self.fp.write(item['genre']+'\t'+item['dynasty']+'\t'+item['author']+'\t'+item['title']+'\t'+item['content']+'\n')
        return item
    
    def close_spider(self,spider):
        print('结束爬虫~~~')
        self.fp.close()