__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class Food52Spider(CrawlSpider):
    name = 'food52'
    allowed_domains = ['food52.com']
    start_urls = ["http://food52.com/recipes"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipes/\d+-.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*/recipes\?.*page=\d+.*"))
    )

    def __init__(self):
        super(Food52Spider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item