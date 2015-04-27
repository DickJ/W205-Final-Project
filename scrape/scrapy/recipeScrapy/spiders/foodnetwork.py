__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem

class FoodNetworkSpider(CrawlSpider):
    name = 'foodnetwork'
    allowed_domains = ['foodnetwork.com']
    start_urls = ["http://www.foodnetwork.com/recipes/a-z.html"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipes/.*",
                           deny=[".*/recipes/a-z\.\w+\.\d+\.html",
                                 ".*/recipes/a-z\.\d+\.\d+\.html"]),
              callback='parse_item'),
        Rule(LinkExtractor(allow=[".*/recipes/a-z\.\w+\.\d+\.html",
                                  ".*/recipes/a-z\.\d+\.\d+\.html"]))
    )

    def __init__(self):
        super(FoodNetworkSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item