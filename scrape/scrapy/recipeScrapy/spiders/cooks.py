__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem
import re

class CooksSpider(CrawlSpider):
    name = 'cooks'
    USER_AGENT = "Mozilla/5.0"
    allowed_domains = ['cooks.com']
    start_urls = ["http://www.cooks.com/rec/browse/"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipe/[\w\d]{8}/[\w\d-]+\.html"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*/rec/new_recipes_\w+\.html"))
    )

    def __init__(self):
        super(CooksSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item