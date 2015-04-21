__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem
import re

class Spider(CrawlSpider):
    name = ''
    allowed_domains = ['']
    start_urls = [""]
    rules = (
        Rule(LinkExtractor(allow=""),
              callback='parse_item'),
        Rule(LinkExtractor(allow=""))
    )

    def __init__(self):
        super(+++++++++Spider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item