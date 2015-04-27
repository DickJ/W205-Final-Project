__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem

class KraftRecipesSpider(CrawlSpider):
    name = 'kraftrecipes'
    allowed_domains = ['kraftrecipes.com']
    start_urls = ["http://www.kraftrecipes.com/recipes/search/SearchResults.aspx?searchtext=1&u2=1&start=1&photo=y&"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipes/.*-\d+\.aspx"),
              callback='parse_item'),
        Rule(LinkExtractor(
            allow='.*kraftrecipes\.com/recipes/search/SearchResults\.aspx\?searchtext=1.*')))

    def __init__(self):
        super(KraftRecipesSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item