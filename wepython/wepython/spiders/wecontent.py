#coding:utf-8
#@author:hya1101@126.com

from scrapy_redis.spiders import RedisSpider
from wepython.items import WepythonLoader, WepythonItem
from redis import Redis
from time import sleep
from scrapy.selector import Selector

class WeContentSpider(RedisSpider):
    name = 'wecon'
    redis_key = 'wepy:list'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(WeContentSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        print "^^^^\n"+response.url+"\n^^^^"
        item = WepythonItem()
        selector = Selector(response)

        titles = selector.xpath('//*[@id="history"]/div/div[@class="weui_msg_card_bd"]/div[@class="weui_media_box appmsg"]/div[@class="weui_media_bd"]')
        i = 1
        for each_title in titles:
            print i
            i =  i+1
            name = each_title.xpath('h4/text()').extract()[0]
            time = each_title.xpath('p[@class="weui_media_extra_info"]/text()').extract()[0]
            summary = each_title.xpath('p[@class="weui_media_desc"]/text()').extract()
            print name.strip()
            print time
            if summary:
                print summary[0]
                item['summary'] = summary[0]
            else:
                item['summary'] = '\0'
            item['title'] = name.strip()
            item['time'] = time
            yield item
