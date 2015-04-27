__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem
import re

class DavidLebovitzSpider(CrawlSpider):
    name = 'davidlebovitz'
    allowed_domains = ['davidlebovitz.com']
    start_urls = ["http://www.davidlebovitz.com/category/recipes/"]
    rules = (
        Rule(LinkExtractor(allow="http://www.davidlebovitz.com/\d{4}/\d{2}/[\w-]/?"),
              callback='parse_item'),
        Rule(LinkExtractor(allow="http://www.davidlebovitz.com/category/recipes/\w/?"))
    )

    def __init__(self):
        super(DavidLebovitzSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item