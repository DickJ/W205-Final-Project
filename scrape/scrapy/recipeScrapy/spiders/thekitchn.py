__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem

class TheKitchnSpider(CrawlSpider):
    name = 'thekitchn'
    allowed_domains = ['thekitchn.com']
    start_urls = ["http://www.thekitchn.com/recipes/all"]
    rules = (
        Rule(LinkExtractor(allow=".*-\d{6}"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=".*/recipes/.*"))
    )

    def __init__(self):
        super(TheKitchnSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item