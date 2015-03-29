# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bs4 import BeautifulSoup
import pymongo
from pymongo.errors import AutoReconnect
import re
from scrapy.conf import settings
from scrapy.exceptions import DropItem
import urllib2

class RecipeScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class ExtractRecipeBoxPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        pass


class ExtractIngredientsPipeline(object):
    def __init__(self):
        """
        Initialize ingredient extraction heuristics
        """
        self.heur = [] # recipe box location heuristics
        self.heur.append(re.compile('<div .*itemprop="ingredients?".*>(?P<ingred>.*)</div>'))
        self.heur.append(re.compile('<li .*class="ingredients?".*>(?P<ingred>.*)</li>'))
        self.heur.append(re.compile('<li .*itemprop="ingredients?".*>(?P<ingred>.*)</li>'))
        self.heur.append(re.compile('<li .*id="liIngredients?".*>(?P<ingred>[\s\S]*?)</li>'))

    @classmethod
    def _process_results(cls, r):
        """
        DEPRECATED: re.findall() returns a list
        :param r: A MatchObject instance containing ingredients
        :return: a tuple containing all ingredients found
        """
        ing = []
        for i in r:
            ing.append(i.group('ingred'))
        return tuple(ing)

    def process_item(self, item, spider):
        page = urllib2.urlopen(item['url']).read()
        soup = BeautifulSoup(page)
        item['title'] = soup.title.string
        for h in self.heur:
            results = [m.groupdict() for m in h.finditer(page)]
            if results:
                item['ingred'] = results
                return item

        raise DropItem("Unable to find ingredients in %s for spider %s" %
                       (item['url'], spider))

class MongoWriterPipeline(object):
    def __init__(self):
        conn = pymongo.MongoClient(settings['MONGODB_SERVER'],
                                   settings['MONGODB_PORT'])
        db = conn[settings['MONGODB_DB']]
        db.authenticate(settings['MONGODB_USER'], settings['MONGODB_PW'])
        self.coll = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        for i in range(5):
            try:
                self.coll.insert(dict(item))
                return item
            except AutoReconnect:
                print "Reconnection attempt %d" % (i,)  # Change to logging
        raise DropItem