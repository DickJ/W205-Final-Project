__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class SeriousEatsSpider(CrawlSpider):
    name = 'seriouseats'
    allowed_domains = ['seriouseats.com']
    start_urls = ["http://www.seriouseats.com/search?term=&site=recipes&offset=0"]
    rules = (
        Rule(LinkExtractor(allow='.*seriouseats\.com/recipes/.*'),
              callback='parse_item'),
        Rule(LinkExtractor(allow='seriouseats\.com/search\?term=&site=recipes&offset='))
    )

    def __init__(self):
        super(SeriousEatsSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item