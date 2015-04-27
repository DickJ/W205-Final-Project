__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem
import re

class SteamyKitchenSpider(CrawlSpider):
    name = 'steamykitchen'
    USER_AGENT = "Mozilla/4.0"
    allowed_domains = ['steamykitchen.com']
    start_urls = ["http://steamykitchen.com/category/recipes"]
    rules = (
        Rule(LinkExtractor(allow=".*\.com/\d+-.*\.html"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*/category/recipes/page/\d+"))
    )

    def __init__(self):
        super(SteamyKitchenSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item