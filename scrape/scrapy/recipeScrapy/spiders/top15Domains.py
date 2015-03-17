__author__ = 'Rich Johnson'

# //*[@id='content"]/div/div//p[*]/a

from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

from ..items import findDomainsItem

class MySpider(Spider):
    name = 'finddomains'
    start_urls = ["http://www.ebizmba.com/articles/recipe-websites"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        domains = hxs.select('//*[@id="content"]/div/div/p')

        items = []
        for section in domains:
            item = findDomainsItem()
            item['domain_name'] = section.select('a/strong/text()').extract()
            item['link'] = section.select('a/@href').extract()
            if len(item['domain_name']) > 0:
                # There is an exception to the formatting where a line is
                # missing a space and therefore the split index is one off.
                try:
                    item['domain_name'] = [item['domain_name'][0].split()[2]]
                except:
                    item['domain_name'] = [item['domain_name'][0].split()[1]]
                items.append(item)

        return items