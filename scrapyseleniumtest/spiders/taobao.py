# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import quote
from..items import ProductItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    # start_urls = ['http://www.taobao.com/']
    base_url = 'http://s.taobao.com/search?q='

    def parse(self, response):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        products = response.xpath(
            '//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]')
        # for product in products:
        for i in range(0,1):
            item = ProductItem()
            # item['price'] = ''.join(product.xpath('.//div[contains(@class, "price")]//text()').extract()).strip()
            # item['title'] = ''.join(product.xpath('.//div[contains(@class, "title")]//text()').extract()).strip()
            # item['shop'] = ''.join(product.xpath('.//div[contains(@class, "shop")]//text()').extract()).strip()
            # item['image'] = ''.join(product.xpath('.//div[@class="pic"]//img[contains(@class, "img")]/@data-src')
            #                         .extract()).strip()
            # item['deal'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()').extract_first()
            # item['location'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
            # item = {"qq": "q", "ww": "w"}
            item['qq'] = "q"
            item['ww'] = "w"
            yield item

    def start_requests(self):
        print("----------------------------------------------------------------------------------------------------------")

        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):

                url = self.base_url + quote(keyword)
                print("#################################################################: %s" % url)
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)



