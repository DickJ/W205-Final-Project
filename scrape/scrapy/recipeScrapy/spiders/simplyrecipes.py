__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.exceptions import DropItem
from ..items import RecipeItem
from scrapy import log

class SimplyRecipesSpider(CrawlSpider):

    name = 'simplyrecipes'
    allowed_domains = ['simplyrecipes.com']
    start_urls = ["http://www.simplyrecipes.com/index"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipes/.*", deny=[".*/recipes/.*/.*/"]),
             callback='parse_item'),
        Rule(LinkExtractor(allow=".*/recipes/ingredient/.*"))
    )

    def __init__(self):
        super(SimplyRecipesSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item
        else:
            raise DropItem