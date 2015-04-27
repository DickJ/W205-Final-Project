__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem
import re

class FoodRepublicSpider(CrawlSpider):
    name = 'foodrepublic'
    allowed_domains = ['foodrepublic.com']
    start_urls = ["http://www.foodrepublic.com/recipes"]
    rules = (
        Rule(LinkExtractor(allow=".*\.com/\d{4}/\d{2}/\d{2}/.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*/recipes\?.*page=\d+&?.*"))
    )

    def __init__(self):
        super(FoodRepublicSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item