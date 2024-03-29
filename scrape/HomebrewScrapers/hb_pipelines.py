# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import logging
import pymongo
import pymongo.errors
import re
import scrapy.exceptions
from scrapy import log
from time import sleep
import urllib2


class ExtractIngredientsPipeline(object):
    """
    ExtractIngredientsPipeline provides the basis for locating and extracting
    ingredients from a given recipe page.
    """

    def __init__(self):
        """
        Initialize ingredient extraction heuristics
        """
        self.heur = [self._div_tag_parser, self._li_tag_parser,
                     self._span_tag_parser]

    @classmethod
    def _div_tag_parser(cls, page):
        """
        Runs ingredient checking heuristics that look for <div> tags

        Each page is scanned for ingredients which are put in a list of dicts in
        the format [{ingred: "Ingred 1"}, ..., {ingred: "Ingred n"}]
        This list is then passed to _process_results for cleaning and the
        resulting tuple is returned.

        :param page: a string containing HTML code for a webpage
        :return: A tuple containing the ingredients extracted from the webpage,
                 if found. Otherwise, it returns None.
        """
        h = [re.compile(
                '<div [^>]*itemprop=["\']ingredients?["\'][^>]*>(?P<ingred>[\s\S]*?)</div>',
                flags=re.IGNORECASE),
             re.compile(
                '<div [^>]*class=["\']ingredients? recipe-ingredients?["\'][^>]*>(?P<ingred>[\s\S]*?)</div>',
                flags=re.IGNORECASE),
             re.compile(
                 '<div [^>]*class=["\']fr-ing-text["\'][^>]*>(?P<ingred>[\s\S]*?)</div>',
                 flags=re.IGNORECASE),
             ]
        for r in h:
            results = [m.groupdict() for m in r.finditer(page)]
            if results:
                return cls._process_results(results)
        return None


    @classmethod
    def _li_tag_parser(cls, page):
        """
        Runs ingredient checking heuristics that look for <li> tags

        Each page is scanned for ingredients which are put in a list of dicts in
        the format [{ingred: "Ingred 1"}, ..., {ingred: "Ingred n"}]
        This list is then passed to _process_results for cleaning and the
        resulting tuple is returned.

        :param page: a string containing HTML code for a webpage
        :return: A tuple containing the ingredients extracted from the webpage,
                 if found. Otherwise, it returns None.
        """
        h = [re.compile(
                '<li [^>]*class=["\']ingredients?["\'][^>]*>(?P<ingred>[\s\S]*?)</li>',
                flags=re.IGNORECASE),
             re.compile(
                '<li [^>]*itemprop=["\']ingredients?["\'][^>]*>(?P<ingred>[\s\S]*?)</li>',
                flags=re.IGNORECASE),
             re.compile(
                '<li [^>]*id=["\']liIngredients?["\'][^>]*>(?P<ingred>[\s\S]*?)</li>',
                flags=re.IGNORECASE),
             re.compile(
                '<dl [^>]*itemprop=["\']ingredients?["\'][^>]*>(?P<ingred>[\s\S]*?)</dl>',
                flags=re.IGNORECASE)]

        for r in h:
            results = [m.groupdict() for m in r.finditer(page)]
            if results:
                return cls._process_results(results)
        return None


    @classmethod
    def _span_tag_parser(cls, page):
        """
        Runs ingredient checking heuristics that look for <span> tags

        Due to the nature of span tags, these are processed in a different
        manner than <div> and <li> tags. Errors may arise from nested <span>
        tags, as such, pages are processed in to BeautifulSoup to search for
        possible ingredients.

        Each page is scanned for ingredients which are put in a list of dicts in
        the format [{ingred: "Ingred 1"}, ..., {ingred: "Ingred n"}]
        This list is then passed to _process_results for cleaning and the
        resulting tuple is returned.

        :param page: a string containing HTML code for a webpage
        :return: A tuple containing the ingredients extracted from the webpage,
                 if found. Otherwise, it returns None.
        """
        results = []

        h = [
            re.compile(
                '<span [^>]*itemprop=["\']ingredients?["\'][^>]*>',
                flags=re.IGNORECASE),
            re.compile(
                '<span [^>]*class=["\']ingredients?["\'][^>]*>',
                flags=re.IGNORECASE)]

        for r in h:
            if r.search(page):
                spans = BeautifulSoup(page).find_all('span')
                for span in spans:
                    if r.match(str(span)):
                        results.append({'ingred' : span})
                return cls._process_results(results)

        return None


    @classmethod
    def _process_results(cls, r):
        """
        This function takes a list of dicts, cleans it, and returns a clean tuple

        :param r: A list of dictionaries in the format [{ingred: "Ing 1"}, ..., {ingred: "Ing n"}]
        :return: a tuple containing all ingredients found after they have been cleaned
        """
        ing = []
        for i in r:
            tmp = i['ingred']
            tmp = re.sub(r'<[^>]+>', '', str(tmp))  # Remove HTML tags
            tmp = re.sub('[\n\r]', '', tmp)  # Remove excessive newlines
            tmp = re.sub('\s{2,}', ' ', tmp)  # Remove excessive whitespace
            tmp = re.sub(u'\xc2\xa0', ' ', tmp) # Get rid of no-break spaces
            tmp = tmp.strip() # removing leading/trailing whitespace, tabs, etc.
            if tmp is not '':
                ing.append(tmp)
        return tuple(ing)

    def process_item(self, item, spider):
        """
        :param item: a RecipeItem object containing an entry for the 'url' field
        :param spider: A CrawlSpider object
        :return: Returns RecipeItem containing the title and ingredients list
                 for a given recipe

        :raises: scrapy.exceptions.DropItem if the url is unable to be retrieved
                 or if ingredients are not found in the retrieved page.
        """
        try:
            # Bypass user-agent filtering
            req = urllib2.Request(item['url'], headers={'User-Agent' : 'Mozilla/5.0'})
            page = urllib2.urlopen(req).read()
        except TypeError:
            raise scrapy.exceptions.DropItem("No object received this time.")
        except:
            logging.info("Couldn't open %s. Will retry in 10s." % (item['url'],))
            sleep(10)
            req = urllib2.Request(item['url'], headers={'User-Agent' : 'Magic Browser'})
            page = urllib2.urlopen(req).read()
        else:
            title_m = re.search('<title>(?P<title>.*?)</title>', page)
            try:
                item['title'] = title_m.group('title')
            except Exception as e:
                logging.info("Page %s has no title" % (item['url']))

            for h in self.heur:
                results = h(page)
                if results:
                    item['ingred'] = results
                    return item
            raise scrapy.exceptions.DropItem(
                "Unable to find ingredients in %s for spider %s" %
                (item['url'], spider))


class MongoWriterPipeline(object):
    def __init__(self, s):
        try:
            conn = pymongo.MongoClient(s['MONGODB_SERVER'], s['MONGODB_PORT'])
            db = conn[s['MONGODB_DB']]
            db.authenticate(s['MONGODB_USER'], s['MONGODB_PW'])
            self.coll = db[s['MONGODB_COLLECTION']]
            self.possibles = db[s['MONGODB_DROPPED_DB']]
        except pymongo.errors.ConnectionFailure:
            log.msg("Could not connect to mongodb %s:%d"
                    % (s['MONGODB_SERVER'], s['MONGODB_PORT']),
                    level=log.CRITICAL)

    def process_item(self, item, spider):
        """
        Inserts item into a MongoDB
        """
        item['is_indexed'] = False
        for i in range(5):
            try:
                if 'ingred' in item.keys():
                    self.coll.insert(dict(item))
                    return item
                else:
                    self.possibles.insert(dict(item))
                    raise scrapy.exceptions.DropItem(
                        "Unable to find ingredients in %s for spider %s" %
                        (item['url'], spider))
            except pymongo.errors.AutoReconnect:
                log.msg("Reconnection attempt %d" % (i,), level=log.WARNING) # Change to logging
        raise scrapy.exceptions.DropItem(
            "Could not insert %s in spider %s into mongoDB"
            % (item['url'], spider))


########## TESTS ##########
def MongoWriterPipeline_test():
    import hb_items
    dbsettings = {'MONGODB_SERVER':'127.0.0.1', 'MONGODB_PORT':27017,
                  'MONGODB_DB':'recipemaker', 'MONGODB_COLLECTION':'recipeURLs'}
    item = hb_items.recipeItem()
    item['url'] = 'http://www.test.com'
    item['title'] = 'test title'
    item['ingred'] = ('first ingred', 'second ingred', 'third ingred')
    item['is_indexed'] = False
    mw = MongoWriterPipeline(dbsettings)
    mw.process_item(item, None)


def ExtractIngredientsPipeline_test():
    page = '''
    <html> stuff here ... </html>
    '''
    res = []
    extract = ExtractIngredientsPipeline()
    res.append(extract._div_tag_parser(page))
    res.append(extract._li_tag_parser(page))
    res.append(extract._span_tag_parser(page))
    extract._process_results(res[0])
    extract._process_results(res[1])
    extract._process_results(res[2])


def ExtractFromli_test():
    from hb_items import recipeItem
    item = recipeItem()
    k = ExtractIngredientsPipeline()
    item['url'] = 'http://naturallyella.com/2013/05/08/grilled-asparagus-and-chili-orange-quinoa-spring-rolls/'

    ExtractIngredientsPipeline.process_item(k, item, None)

def ExtractFromSpan_test():
    # Test <span itemprop="ingredients"> tag extraction
    import hb_items
    item1 = hb_items.recipeItem()
    item1['url'] = 'http://www.kraftrecipes.com/recipes/creamy-citrus-chive-asparagus-114730.aspx'
    extract = ExtractIngredientsPipeline()
    item = extract.process_item(item1, None)
    print item['ingred']

if __name__ == '__main__':
    # MongoWriterPipeline_test()
    # ExtractIngredientsPipeline_test()
    ExtractFromli_test()

    print "Tests complete."