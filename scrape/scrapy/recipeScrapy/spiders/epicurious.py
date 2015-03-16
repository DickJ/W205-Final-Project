__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem

class EpicuriousSpider(CrawlSpider):
    name = 'epicurious'
    allowed_domains = ['']
    start_urls = [""]
    rules = (
        Rule(LinkExtractor(allow=""),
              callback='parse_item'),
        Rule(LinkExtractor(allow=""))
    )

    def __init__(self):
        super(EpicuriousSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item