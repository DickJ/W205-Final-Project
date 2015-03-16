__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem


class BettyCrockerSpider(CrawlSpider):
    name = 'bettycrocker'
    allowed_domains = ["bettycrocker.com"]
    start_urls = ["http://www.bettycrocker.com/sitemap"]
    rules = (
        Rule(LinkExtractor(allow=".*bettycrocker.com/recipes/.*/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}.*"),
             callback='parse_item'),
        Rule(LinkExtractor(allow=".*bettycrocker.com/recipes/.*"))
    )

    def __init__(self):
        super(BettyCrockerSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item
