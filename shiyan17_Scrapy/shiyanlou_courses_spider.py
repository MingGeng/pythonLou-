# -*- coding:utf-8 -*-
# encoding=utf-8
#import sys
#reload(sys)
#sys.setdaulftencoding('utf-8')
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanlou-courses'

#    def start_requests(self):
#        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=Python&page={}'
#        urls = (url_tmpl.format(i) for i in range(1, 7))
#        for url in urls:
#            yield scrapy.Request(url=url, callback=self.parse)


    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=Python&page={}'
        return (url_tmpl.format(i) for i in range(1, 2))

    def parse(self, res):
        for course in res.css('div.course-body'):
            yield {
                    'name': course.css('div.course-name::text').extract_first(),
                    'description': course.css('div.course-desc::text').extract_first(),
                    'type': course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
                    'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')
                    }
            
