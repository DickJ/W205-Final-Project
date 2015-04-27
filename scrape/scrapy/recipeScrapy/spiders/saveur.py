__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem
import re

class SaveurSpider(CrawlSpider):
    name = 'saveur'
    allowed_domains = ['saveur.com']
    start_urls = ["http://www.saveur.com/recipe-collections?sort=1&page=0"]
    rules = (
        Rule(LinkExtractor(allow=".*saveur\.com/article/(r|R)ecipes/[\w\d-]"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=[".*saveur\.com/recipe-collections\?page=\d+&sort=1",
                                  ".*saveur\.com/article/.*"]))
    )

    def __init__(self):
        super(SaveurSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item