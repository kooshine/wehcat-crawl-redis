# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from sched import scheduler

import scrapy
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class WepythonItem(Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    time = scrapy.Field()
    summary = scrapy.Field()
    pass

class WepythonLoader(ItemLoader):
    default_item_class = WepythonItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
