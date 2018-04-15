# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseItem

class CoursesSpider(scrapy.Spider):
    name = 'adv_courses'
#    allowed_domains = ['shiyanlou.com']
#    start_urls = ['http://shiyanlou.com/']

    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_tmpl.format(i) for i in range(1,24))

    def parse(self, res):
        for course in res.css('div.course-body'):
            item = CourseItem({
                'name': course.css('div.course-name::text').extract_first(),
                'description': course.css('div.course-desc::text').extract_first(),
                'type': course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
                })
            yield item


