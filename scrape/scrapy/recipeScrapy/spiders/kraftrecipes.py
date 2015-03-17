__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem

class KraftRecipesSpider(CrawlSpider):
    name = 'kraftrecipes'
    allowed_domains = ['kraftrecipes.com']
    start_urls = ["http://www.kraftrecipes.com/recipes/main.aspx"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipes/.*-\d+\.aspx"),
              callback='parse_item'),
        Rule(LinkExtractor(deny=[".*/[cC]ontrols/.*", ".*/[cC]ommunity/.*",
                                 ".*true%26pf.*"]))
    )

    def __init__(self):
        super(KraftRecipesSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item