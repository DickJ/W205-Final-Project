__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem
import re

class HomesickTexanSpider(CrawlSpider):
    name = 'homesicktexan'
    allowed_domains = ['homesicktexan.com']
    start_urls = ["http://www.homesicktexan.com/p/recipe-index.html"]
    rules = (
        Rule(LinkExtractor(allow=".*homesicktexan\.com/\d{4}/\d{2}/.*\.html"),
              callback='parse_item'),
        #Rule(LinkExtractor(allow=""))
    )

    def __init__(self):
        super(HomesickTexanSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        item['url'] = re.sub("\?.*", "", item['url'])
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item