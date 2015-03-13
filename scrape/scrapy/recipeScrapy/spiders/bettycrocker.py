__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem

class bettyCrockerSpider(CrawlSpider):
    name = 'bettycrocker'
    allowed_domains = ["bettycrocker.com"]
    start_urls = ["http://www.bettycrocker.com/sitemap"]
    rules = (
        Rule(LinkExtractor(allow=".*bettycrocker.com/recipes/.*/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}.*"),
             callback='parse_item'),
        # This rule is more of a hammer than a scalpel, it could
        # probably be pared down quite a bit. I was assuming robots.txt would
        # take care of most of the work, but it still can be simplified
        Rule(LinkExtractor(allow=".*bettycrocker.com/recipes/.*"))
    )

    def __init__(self):
        super(bettyCrockerSpider, self).__init__()
        self.seen_recipes = set()


    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            # if memory is an issue, we can remove
            # http://www.bettycrocker.com/recipes/ and leave only the
            # pertinent document name, this should ~halve the size of the
            # set, particularly because python can have substantial memory
            # cost on sets as they grow larger.
            self.seen_recipes.add(item['url'])
            return item
