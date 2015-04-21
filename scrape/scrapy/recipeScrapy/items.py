__author__ = "Rich Johnson"

import scrapy

class RecipeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    ingred = scrapy.Field()
    is_indexed = scrapy.Field()