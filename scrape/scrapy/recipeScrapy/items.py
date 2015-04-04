__author__ = "Rich Johnson"
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class findDomainsItem(scrapy.Item):
    domain_name = scrapy.Field()
    link = scrapy.Field()

class recipeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    recipe_box = scrapy.Field()
    ingred = scrapy.Field()
    is_indexed = scrapy.Field()