__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class RecipeLandSpider(CrawlSpider):
    name = 'recipeland'
    allowed_domains = ['recipeland.com']
    start_urls = ["https://recipeland.com/recipes/list"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipe/v/.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*/recipes/list\?.*page=\d+"))
    )

    def __init__(self):
        super(RecipeLandSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item