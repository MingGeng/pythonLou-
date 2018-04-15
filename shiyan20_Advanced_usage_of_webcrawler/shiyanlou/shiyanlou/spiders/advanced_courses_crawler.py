# -*- coding: utf-8 -*-
import scrapy


class AdvancedCoursesCrawlerSpider(scrapy.Spider):
    name = 'advanced_courses_crawler'
#    allowed_domains = ['shiyanlou.com']
    start_urls = ['http://www.shiyanlou.com/courses/63']

    def parse(self, res):
        yield {
                'name': res.xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/h4/span[1]/text()'),
                'auther': res.jxpajth('/html/body/div[4]/div/div[2]/div[2]/div[2]/div[1]/div[1]/strong/text()').extract_first()
        }
        for url in res.xpath('/html/body/div[3]/div/div[2]/div[6]/div[2]/a[1]/@href'):
            yield res.follow(url, callback=self.parse)
