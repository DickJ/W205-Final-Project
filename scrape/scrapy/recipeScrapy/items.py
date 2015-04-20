__author__ = "Rich Johnson"

import scrapy

class findDomainsItem(scrapy.Item):
    domain_name = scrapy.Field()
    link = scrapy.Field()

class recipeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    ingred = scrapy.Field()
    is_indexed = scrapy.Field()