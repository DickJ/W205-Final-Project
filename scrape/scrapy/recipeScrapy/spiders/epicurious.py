__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import RecipeItem

class EpicuriousSpider(CrawlSpider):
    name = 'epicurious'
    allowed_domains = ['epicurious.com']
    start_urls = ["http://www.epicurious.com/recipesmenus/browse"]
    rules = (
        Rule(LinkExtractor(allow=".*/recipes/food/views/[\w\d-]+\d+"),
              callback='parse_item'),
        Rule(LinkExtractor(allow=[".*\.com/tools/searchresults\?type=simple&att=\d+&search=.*",
                                  ".*/searchresults\?type=simple&att=\d+&search=[\w\d]+&pageNumber=\d+&pageSize=\d+&resultOffset=\d+"]))
    )

    def __init__(self):
        super(EpicuriousSpider, self).__init__()
        self.seen_recipes = set()

    def parse_item(self, response):
        item = RecipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item