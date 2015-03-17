__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class KraftRecipesSpider(CrawlSpider):
    name = 'allrecipes'
    allowed_domains = ['allrecipes.com']
    start_urls = ["http://allrecipes.com/recipes"]
    rules = (
        Rule(LinkExtractor(allow=".*/Recipe/.*/Detail\.aspx.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*/recipes/main.aspx\?Page=\d+.*"))
    )

    def __init__(self):
        super(KraftRecipesSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item