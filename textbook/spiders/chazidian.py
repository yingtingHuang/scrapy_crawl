# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from textbook.items import TextbookItem


class ChazidianSpider(CrawlSpider):
    name = 'chazidian'  # 爬虫名称
    allowed_domains = ['zuowen.chazidian.com']  # 输入域名,而非urls。
    start_urls = ['https://zuowen.chazidian.com/']
    # 链接提取器：会去起始url响应回来的页面中提取指定的url
    # sublink =["gaoyi_xieren",	"gaoyi_xushi",	"gaoyi_xiejing",	"gaoyi_zhuangwu",	"gaoyi_shuomingwen",	"gaoyi_shuxin",	"gaoyi_riji",	"gaoyi_dushubiji",	"gaoyi_yanjianggao",	"gaoyi_yilunwen",	"gaoyi_gongwen",	"gaoyi_duhougan",	"gaoyi_zawen",	"gaoyi_sanwen",	"gaoyi_xiaoshuo",	"gaoyi_shige",	"gaoyi_huati",	"gaoyi_xiangxiang",	"gaoyi_xuxiegaixie",	"gaoyi_kantu",	"gaoyi_tonghuayuyan",	"gaoyi_shenqingshu",	"gaoyi_shuqing",	"gaoyi_yingyongwen",	"gaoer_xieren",	"gaoer_xushi",	"gaoer_xiejing",	"gaoer_zhuangwu",	"gaoer_shuomingwen",	"gaoer_shuxin",	"gaoer_riji",	"gaoer_dushubiji",	"gaoer_yanjianggao",	"gaoer_yilunwen",	"gaoer_gongwen",	"gaoer_duhougan",	"gaoer_zawen",	"gaoer_sanwen",	"gaoer_xiaoshuo",	"gaoer_shige",	"gaoer_huati",	"gaoer_xiangxiang",	"gaoer_xuxiegaixie",	"gaoer_kantu",	"gaoer_tonghuayuyan",	"gaoer_shenqingshu",	"gaoer_shuqing",	"gaoer_yingyongwen",	"gaosan_xieren",	"gaosan_xushi",	"gaosan_xiejing",	"gaosan_zhuangwu",	"gaosan_shuomingwen",	"gaosan_shuxin",	"gaosan_riji",	"gaosan_dushubiji",	"gaosan_yanjianggao",	"gaosan_yilunwen",	"gaosan_gongwen",	"gaosan_duhougan",	"gaosan_zawen",	"gaosan_sanwen",	"gaosan_xiaoshuo",	"gaosan_shige",	"gaosan_huati",	"gaosan_xiangxiang",	"gaosan_xuxiegaixie",	"gaosan_kantu",	"gaosan_tonghuayuyan",	"gaosan_shenqingshu",	"gaosan_shuqing",	"gaosan_yingyongwen"]
    # sublink = ["chuyi_xieren",	"chuyi_xushi",	"chuyi_xiejing",	"chuyi_zhuangwu",	"chuyi_shuomingwen",	"chuyi_shuxin",	"chuyi_riji",	"chuyi_dushubiji",	"chuyi_yanjianggao",	"chuyi_yilunwen",	"chuyi_gongwen",	"chuyi_duhougan",	"chuyi_zawen",	"chuyi_sanwen",	"chuyi_xiaoshuo",	"chuyi_shige",	"chuyi_huati",	"chuyi_xiangxiang",	"chuyi_xuxiegaixie",	"chuyi_kantu",	"chuyi_tonghuayuyan",	"chuyi_shenqingshu",	"chuyi_shuqing",	"chuyi_yingyongwen",	"chuer_xieren",	"chuer_xushi",	"chuer_xiejing",	"chuer_zhuangwu",	"chuer_shuomingwen",	"chuer_shuxin",	"chuer_riji",	"chuer_dushubiji",	"chuer_yanjianggao",	"chuer_yilunwen",	"chuer_gongwen",	"chuer_duhougan",	"chuer_zawen",	"chuer_sanwen",	"chuer_xiaoshuo",	"chuer_shige",	"chuer_huati",	"chuer_xiangxiang",	"chuer_xuxiegaixie",	"chuer_kantu",	"chuer_tonghuayuyan",	"chuer_shenqingshu",	"chuer_shuqing",	"chuer_yingyongwen",	"chusan_xieren",	"chusan_xushi",	"chusan_xiejing",	"chusan_zhuangwu",	"chusan_shuomingwen",	"chusan_shuxin",	"chusan_riji",	"chusan_dushubiji",	"chusan_yanjianggao",	"chusan_yilunwen",	"chusan_gongwen",	"chusan_duhougan",	"chusan_zawen",	"chusan_sanwen",	"chusan_xiaoshuo",	"chusan_shige",	"chusan_huati",	"chusan_xiangxiang",	"chusan_xuxiegaixie",	"chusan_kantu",	"chusan_tonghuayuyan",	"chusan_shenqingshu",	"chusan_shuqing",	"chusan_yingyongwen"]
    sublink = ["yinianji_xieren",	"yinianji_xushi",	"yinianji_xiejing",	"yinianji_zhuangwu",	"yinianji_shuomingwen",	"yinianji_shuxin",	"yinianji_riji",	"yinianji_dushubiji",	"yinianji_yanjianggao",	"yinianji_yilunwen",	"yinianji_gongwen",	"yinianji_duhougan",	"yinianji_zawen",	"yinianji_sanwen",	"yinianji_xiaoshuo",	"yinianji_shige",	"yinianji_huati",	"yinianji_xiangxiang",	"yinianji_xuxiegaixie",	"yinianji_kantu",	"yinianji_tonghuayuyan",	"yinianji_shenqingshu",	"yinianji_shuqing",	"yinianji_yingyongwen",	"ernianji_xieren",	"ernianji_xushi",	"ernianji_xiejing",	"ernianji_zhuangwu",	"ernianji_shuomingwen",	"ernianji_shuxin",	"ernianji_riji",	"ernianji_dushubiji",	"ernianji_yanjianggao",	"ernianji_yilunwen",	"ernianji_gongwen",	"ernianji_duhougan",	"ernianji_zawen",	"ernianji_sanwen",	"ernianji_xiaoshuo",	"ernianji_shige",	"ernianji_huati",	"ernianji_xiangxiang",	"ernianji_xuxiegaixie",	"ernianji_kantu",	"ernianji_tonghuayuyan",	"ernianji_shenqingshu",	"ernianji_shuqing",	"ernianji_yingyongwen",	"liunianji_xieren",	"liunianji_xushi",	"liunianji_xiejing",	"liunianji_zhuangwu",	"liunianji_shuomingwen",	"liunianji_shuxin",	"liunianji_riji",	"liunianji_dushubiji",	"liunianji_yanjianggao",	"liunianji_yilunwen",	"liunianji_gongwen",	"liunianji_duhougan",	"liunianji_zawen",	"liunianji_sanwen",	"liunianji_xiaoshuo",	"liunianji_shige",	"liunianji_huati",	"liunianji_xiangxiang",	"liunianji_xuxiegaixie",	"liunianji_kantu",	"liunianji_tonghuayuyan",	"liunianji_shenqingshu",	"liunianji_shuqing",	"liunianji_yingyongwen",	"wunianji_xieren",	"wunianji_xushi",	"wunianji_xiejing",	"wunianji_zhuangwu",	"wunianji_shuomingwen",	"wunianji_shuxin",	"wunianji_riji",	"wunianji_dushubiji",	"wunianji_yanjianggao",	"wunianji_yilunwen",	"wunianji_gongwen",	"wunianji_duhougan",	"wunianji_zawen",	"wunianji_sanwen",	"wunianji_xiaoshuo",	"wunianji_shige",	"wunianji_huati",	"wunianji_xiangxiang",	"wunianji_xuxiegaixie",	"wunianji_kantu",	"wunianji_tonghuayuyan",	"wunianji_shenqingshu",	"wunianji_shuqing",	"wunianji_yingyongwen",	"sinianji_xieren",	"sinianji_xushi",	"sinianji_xiejing",	"sinianji_zhuangwu",	"sinianji_shuomingwen",	"sinianji_shuxin",	"sinianji_riji",	"sinianji_dushubiji",	"sinianji_yanjianggao",	"sinianji_yilunwen",	"sinianji_gongwen",	"sinianji_duhougan",	"sinianji_zawen",	"sinianji_sanwen",	"sinianji_xiaoshuo",	"sinianji_shige",	"sinianji_huati",	"sinianji_xiangxiang",	"sinianji_xuxiegaixie",	"sinianji_kantu",	"sinianji_tonghuayuyan",	"sinianji_shenqingshu",	"sinianji_shuqing",	"sinianji_yingyongwen",	"sannianji_xieren",	"sannianji_xushi",	"sannianji_xiejing",	"sannianji_zhuangwu",	"sannianji_shuomingwen",	"sannianji_shuxin",	"sannianji_riji",	"sannianji_dushubiji",	"sannianji_yanjianggao",	"sannianji_yilunwen",	"sannianji_gongwen",	"sannianji_duhougan",	"sannianji_zawen",	"sannianji_sanwen",	"sannianji_xiaoshuo",	"sannianji_shige",	"sannianji_huati",	"sannianji_xiangxiang",	"sannianji_xuxiegaixie",	"sannianji_kantu",	"sannianji_tonghuayuyan",	"sannianji_shenqingshu",	"sannianji_shuqing",	"sannianji_yingyongwen"]
    page_link=set() #保存下一页页面url
    content_link=set() #保存页面内所有可获得的url
    
    # rules元组中存放的是不同的规则解析器（封装好了某种解析规则)
    rules = (
        # 规则解析器。根据链接提取器中提取到的链接，根据指定规则提取解析器链接网页中的内容。
        Rule( LinkExtractor(allow = sublink), callback='parse_item', follow=True),
    )

    
    # 解析方法
    def parse_item(self, response):
        #自动获取下一页的url
        try:
            nextpage_link = response.xpath('//div[@class="pages"]/a[@class="pre"]/@href').extract()[-1]  # 分析路径里面有两个，第一个是上一页，最后一个是下一页
        except:
            nextpage_link = response.xpath('//div[@class="pages"]/a[@class="pre"]/@href').extract()
        if nextpage_link:
            self.page_link.add(nextpage_link)
            yield Request(nextpage_link, callback=self.parse_item)

        divs = response.xpath('//*[@id="show"]')
        nums = len(divs.xpath('./ul/li').extract())
        
        for i in range(nums):
            try:
                genre = divs.xpath('./ul/li['+str(i+1)+']/p[1]/em/text()').extract()[0]
            except:
                genre = divs.xpath('./ul/li['+str(i+1)+']/p[1]/em/text()').extract()

            try:
                title = divs.xpath('./ul/li['+str(i+1)+']/p[1]/a/text()').extract()[0]
            except:
                title = divs.xpath('./ul/li['+str(i+1)+']/p[1]/a/text()').extract()

            try:
                url = divs.xpath('./ul/li['+str(i+1)+']/p[1]/a/@href').extract()[0]
            except:
                url = divs.xpath('./ul/li['+str(i+1)+']/p[1]/a/@href').extract()
                
            
            yield Request(url, callback = self.get_content, meta = {'title': title, 'url': url, 'genre': genre})
            
    def get_content(self, response):
        item = TextbookItem()
        divs = response.xpath('//*[@id="print_content"]')
        body = ''
        for p in divs.xpath('.//p/text()'):
            body = body + p.extract().strip()
        # print ('body:', body)
        item['genre'] = response.meta['genre']
        item['url'] = response.meta['url']
        item['title'] = response.meta['title']
        item['content'] = body
        return item