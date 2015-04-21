__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem
import re

class RachaelRayMagSpider(CrawlSpider):
    name = 'rachaelraymag'
    allowed_domains = ['rachaelraymag.com']
    start_urls = ["http://www.rachaelraymag.com/help/site-map"]
    rules = (
        Rule(LinkExtractor(allow=".*rachaelraymag\.com/recipe/.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=[".*rachaelraymag\.com/recipes/.*/",
                           ".*rachaelraymag\.com/recipes/searchResults\.jsp.*"]))
    )

    def __init__(self):
        super(RachaelRayMagSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item