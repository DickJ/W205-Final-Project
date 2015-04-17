__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem

class SpoonfulSpider(CrawlSpider):
    name = 'spoonful'
    allowed_domains = ['spoonful.comm', 'family.disney.com', 'disney.com']
    start_urls = ["http://family.disney.com/recipes"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipes/page/.*")),
        Rule(LinkExtractor(allow=".*/recipes/.*",
                           deny=[".*/recipes/page/.*"]),
             callback='parse_item')

    )

    def __init__(self):
        super(SpoonfulSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item