__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class ToriAveySpider(CrawlSpider):
    name = 'toriavey'
    allowed_domains = ['toriavey.com']
    start_urls = ["http://toriavey.com/toris-kitchen/recipes/?filter=alphabetical"]
    rules = (
        Rule(LinkExtractor(allow=".*toriavey\.com/toris-kitchen/\d{4}/\d{1,2}/"),
              callback='parse_item'),
        #Rule(LinkExtractor(allow=""))
    )

    def __init__(self):
        super(ToriAveySpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item