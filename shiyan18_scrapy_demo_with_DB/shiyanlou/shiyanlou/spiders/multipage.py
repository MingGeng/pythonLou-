# -*- coding: utf-8 -*-
import scrapy


class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    allowed_domains = ['www.shiyanlou.com/multipage']
    start_urls = ['http://www.shiyanlou.com/multipage/']

    def parse(self, response):
        pass
