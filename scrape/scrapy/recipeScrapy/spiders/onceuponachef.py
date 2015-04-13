__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class OnceUponSpider(CrawlSpider):
    name = 'onceupon'
    allowed_domains = ['onceuponachef.com']
    start_urls = ["http://www.onceuponachef.com/recipes"]
    rules = (
        Rule(LinkExtractor(allow=".*onceuponachef\.com/\d{4}/\d{2}/.*\.html"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=[".*onceuponachef\.com/recipes/\w/?",
                                  ".*onceuponachef\.com/recipes/\w/page/\d+"]))
    )

    def __init__(self):
        super(OnceUponSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item