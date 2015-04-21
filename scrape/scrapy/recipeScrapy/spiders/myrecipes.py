__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem


class CookingLightSpider(CrawlSpider):
    name = 'myrecipes'
    allowed_domains = ['myrecipes.com']
    start_urls = ["http://myrecipes.com/"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipe/.*"), callback="parse_item"),
        Rule(LinkExtractor(deny=[".*/how-to/video/.*", ".*/r/.*",
                                 ".*/about-us/.*", ".*/contact-us/.*",
                                 ".*/frequently-asked-questions/.*",
                                 ".*/press/.*", ".*/rss/.*", ".*/sitemap/.*"]))
    )

    def __init__(self):
        super(CookingLightSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item