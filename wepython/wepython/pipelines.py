# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class WepythonPipeline(object):
    def process_item(self, item, spider):
        with open('redis.txt', 'a') as fp:
            fp.write(item['title'].encode('utf-8'))
            fp.write(item['summary'].encode('utf-8'))
            fp.write(item['time'].encode('utf-8'))
        return item
