import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanlou-gitlab'

#    def start_requests(self):
#        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=Python&page={}'
#        urls = (url_tmpl.format(i) for i in range(1, 7))
#        for url in urls:
#            yield scrapy.Request(url=url, callback=self.parse)


    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=Python&page={}'
        url_tmpl2 = 'https://github.com/shiyanlou?tab=repositories&page={}'
        return (url_tmpl2.format(i) for i in range(1, 4))

    def parse(self, response):
        for repository in response.xpath("//div[@id='user-repositories-list']/ul/li"):
            yield {
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first() 
            }