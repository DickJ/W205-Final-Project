__author__ = "Rich Johnson"
# -*- coding: utf-8 -*-

from scrapy import Item, Field

class recipeItem(Item):
    url = Field()
    title = Field()
    ingred = Field()
    is_indexed = Field()