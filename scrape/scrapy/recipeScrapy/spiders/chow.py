__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem

class chowSpider(CrawlSpider):
    name = 'chow'
    allowed_domains = ['chow.com']
    start_urls = ["http://www.chow.com/recipes"]
    rules = (
        Rule(LinkExtractor(allow=".*chow.com/recipes/\d.*"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=[".*chow.com/recipes\?page=\d+",
                                  ".*chow.com/recipes/category/.*"]))
    )

    def __init__(self):
        super(chowSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item