# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KaospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    emoji = scrapy.Field()
    text_english = scrapy.Field()
    table = scrapy.Field()

class Kaomojiitem2(scrapy.Item):
    kaomoji = scrapy.Field()
    text_japanese = scrapy.Field()
    table = scrapy.Field()
