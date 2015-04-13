__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class IAdoreFoodSpider(CrawlSpider):
    name = 'iadorefood'
    allowed_domains = ['iadorefood.com']
    start_urls = ["http://www.iadorefood.com/recipes/"]
    rules = (
        Rule(LinkExtractor(allow=".*iadorefood.com/recipes/.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*iadorefood\.com/recipes/page/\d+"))
    )

    def __init__(self):
        super(IAdoreFoodSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item