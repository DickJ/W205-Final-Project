__author__ = 'Rich Johnson'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import recipeItem

class FoodSpider(CrawlSpider):
    name = 'food'
    allowed_domains = ['food.com']
    start_urls = []
    for i in range(5): # 50376
        start_urls.append("http://www.food.com/recipe?pn="+str(i))

    rules = (
        Rule(LinkExtractor(allow=".*/recipe/.+\d+"),
              callback='parse_item'),
        #Rule(LinkExtractor(allow=""))
    )

    def __init__(self):
        super(FoodSpider, self).__init__()
        self.seen_recipes = set()

    # JS Is messing up spider ... url to recipe is stored in an array with
    # key "record_url"
    def parse_item(self, response):
        item = recipeItem()
        item['url'] = response.url
        if item['url'] not in self.seen_recipes:
            self.seen_recipes.add(item['url'])
            return item