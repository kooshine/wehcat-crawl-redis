#coding:utf-8
#@author:hya1101@126.com

from scrapy_redis.spiders import RedisSpider
#from wepython.items import WepythonLoader
from redis import Redis
from time import sleep

class WepythonSpider(RedisSpider):
    name = 'wepy'
    redis_key = 'wepy:start_urls'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(WepythonSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        base_url = "http://weixin.sogou.com/weixin"
        print "**** url ****"+ response.url
        r = Redis()

        ContextUrls = response.xpath('//p[@class="tit"]/a/@href').extract()
        print "***********"
        print ContextUrls
        print "************"

        for url in ContextUrls:
            r.lpush('wepy:list', url)
            sleep(1)
        pass     
