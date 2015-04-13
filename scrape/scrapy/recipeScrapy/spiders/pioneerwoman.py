__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class PioneerWomanSpider(CrawlSpider):
    name = 'pioneerwoman'
    allowed_domains = ['thepioneerwoman.com']
    start_urls = ["http://thepioneerwoman.com/cooking/category/all-pw-recipes/?posts_per_page=60"]
    rules = (
        Rule(LinkExtractor(allow=".*thepioneerwoman\.com/cooking/\d{4}/\d{1,2}/.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*thepioneerwoman\.com/cooking/category/all-pw-recipes/page/\d+/.*"))
    )

    def __init__(self):
        super(PioneerWomanSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item