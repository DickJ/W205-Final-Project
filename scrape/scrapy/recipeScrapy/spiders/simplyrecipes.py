__author__ = 'Rich Johnson'

from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

from ..items import recipeItem

class MySpider(Spider):
    name = 'simplyrecipes'
    start_urls = [""]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        domains = hxs.select('XPATH CODE')

        items = []
        for section in domains:
            item = findDomainsItem()
            item['url'] = section.select('XPATH CODE').extract()
            items.append(item)

        return items