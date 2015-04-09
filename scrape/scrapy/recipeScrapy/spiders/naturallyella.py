__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class NaturallyEllaSpider(CrawlSpider):
    name = 'naturallyella'
    allowed_domains = ['naturallyella.com']
    start_urls = ["http://naturallyella.com/recipes/"]
    rules = (
        Rule(LinkExtractor(allow=".*naturallyella\.com/\d{4}/\d{2}/\d{2}/.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*naturallyella\.com/recipes/\w/?"))
    )

    def __init__(self):
        super(NaturallyEllaSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item