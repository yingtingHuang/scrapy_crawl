# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from gushiwen.items import GushiwenItem
from scrapy.http import Request

class GushiwenSpider(CrawlSpider):
    name = 'gushiwen'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org/shiwen/default_4A444444444444A1.aspx']
    # 我们想提取的是链接中有以下字符串的链接
    # sublink = "default_4A111111111111A.*?.aspx" # 文言文
    # sublink = ["default_4A111111111111A1.aspx","default_4A222222222222A1.aspx","default_4A333333333333A1.aspx","default_4A444444444444A1.aspx"]
    
    rules = (
        # allow：提取符合对应正则表达式的链接
        Rule(LinkExtractor(), callback='parse_item', follow=True),
        # restrict_xpaths：使用xpath表达式与allow共用作用提取出同时符合对应xpath表达式和对应正则表达式的链接
        Rule(LinkExtractor(restrict_xpaths='//*[@id="FromPage"]/div//a[contains(., "下一页")]'))  # 实现翻页
    )
    
    def parse_item(self, response):
        item = GushiwenItem()
        divs = response.xpath('//div[@class="sons"]')
        nums = len(divs)
        for i in range(nums):
            d = response.xpath('/html/body/div[2]/div[1]/div['+str(2*i+1)+']')
            item["genre"] = ""
            try:
                item["title"] = d.xpath('./div[1]/p[1]/a/b/text()').extract()[0].strip()
            except:
                continue
            try:
                item["dynasty"] = d.xpath('./div[1]/p[2]/a[1]/text()').extract()[0].strip()
            except:
                continue
            try:
                item["author"] = d.xpath('./div[1]/p[2]/a[2]/text()').extract()[0]
            except:
                continue
            
            content = ''
            for p in d.xpath('.//div[@class="contson"]//p/text()'):
                content = content + p.extract().strip()
            if content == '':
                content = d.xpath('.//div[@class="contson"]/text()').extract()[0].strip()
            item["content"] = content
            yield item  # 将item提交至管道
 
            
