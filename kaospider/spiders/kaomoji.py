import scrapy
import re
from ..items import Kaomojiitem2
from scrapy import Selector


class kaomoji(scrapy.Spider):
    name = "kaomoji"
    allowed_domains = ["kaomojiya.com/"]
    start_urls = [
        "http://kaomojiya.com"
    ]

    def parse(self, response):
        html = response.xpath("//div[@id='cate_table']")
        links = html.xpath("//dl//a/@href").extract()
        for link in links:
            l = u'http://' + self.allowed_domains[0] + link
            yield scrapy.Request(l, callback=self.parse_item, dont_filter=True)
    
    def parse_item(self, response):
        main = response.xpath('//div[@id="main"]')
        text_japanese = main.xpath('//p//strong/text()').extract()[0].split(' ')[-1]
        tr = main.xpath('//table//tr').extract()
        table = response.url.replace('?','/').split("/")[-2]
        for td in tr:
            item = Kaomojiitem2()
            kaomoji = Selector(text=td).xpath('//text()').extract()[0].encode().decode()
            item['kaomoji'] = kaomoji
            item['text_japanese'] = text_japanese
            item['table'] = table
            yield item
