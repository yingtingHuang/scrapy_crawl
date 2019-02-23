# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gushiwen.items import GushiwenItem

class GushiwenSpider(CrawlSpider):
    name = 'gushiwen'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org/shiwen/default_4A444444444444A1.aspx']
    # 我们想提取的是链接中有以下字符串的链接
    sublink = "default_4A444444444444A1.aspx"
#    ["default_4A111111111111A1.aspx","default_4A222222222222A1.aspx",
#               "default_4A333333333333A1.aspx","default_4A444444444444A1.aspx"]
    
    rules = (
        # allow：提取符合对应正则表达式的链接
        Rule(LinkExtractor(), callback='parse_item', follow=True),
        # restrict_xpaths：使用xpath表达式与allow共用作用提取出同时符合对应xpath表达式和对应正则表达式的链接
        Rule(LinkExtractor(restrict_xpaths='//*[@id="FromPage"]/div/a[1]'))  # 实现翻页
    )

    def parse_item(self, response):
        item = GushiwenItem()
        divs = response.xpath('//div[@class="main3"]/div[@class="left"]/div[@class="sons"]')
        nums = len(divs.extract())  # 每页的文章数目
        for d in divs:
            item["genre"] = "文言文"
            item["title"] = d.xpath('//div[@class="cont"]/p[1]/a/b').extract()
            item["dynasty"] = d.xpath('//div[@class="cont"]/p[2]/a[1]').extract()
            item["author"] = d.xpath('//div[@class="cont"]/p[2]/a[2]').extract()
            content = ''
            for p in d.xpath('//div[@class="contson"]//p/text()'):
                content = content + p.extract().strip()
            item["content"] = content
            print("======================================content",item["content"])
            yield item
 
            
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        
