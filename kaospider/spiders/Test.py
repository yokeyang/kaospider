import scrapy
import re
from ..items import KaospiderItem
from scrapy import Selector

class Test(scrapy.Spider):
    name = "Test"
    allowed_domains = ["emojipedia.org/"]
    start_urls = [
        "https://emojipedia.org"
    ]
    def parse(self, response):
        html = response.xpath('//div[@class="sidebar"]//div[@class="block"]').extract()[0]
        selector = Selector(text=html)
        ul = selector.xpath("//ul//li").extract()
        for li in ul:
            a = 'https://emojipedia.org' + Selector(text=li).xpath('//a/@href').extract()[0]
            yield scrapy.Request(a, callback=self.parse_item, dont_filter=True)
            print(a)
    
    def parse_item(self, response):
        content = response.xpath('//div[@class="content"]')
        table = content.xpath('//h1/text()').extract()[-1].replace(' ','').replace('&','_')
        emoji_list = content.xpath('//ul[@class="emoji-list"]//li').extract()
        for li in emoji_list:
            emoji = Selector(text=li).xpath("//span[@class='emoji']/text()").extract()[0]
            text_english = Selector(text=li).xpath("//a/text()").extract()[0]
            item = KaospiderItem()
            item['emoji'] = emoji
            item['table'] = table
            item['text_english'] = text_english
            yield item
