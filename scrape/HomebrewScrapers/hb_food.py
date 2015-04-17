__author__ = 'Rich Johnson'

import re
from hb_items import recipeItem
import logging
from hb_pipelines import ExtractIngredientsPipeline, MongoWriterPipeline
from scrapy.exceptions import DropItem
from hb_settings import settings
import threading
import urllib2

START_URL = "http://www.food.com/recipe?exclude=ass&pn=1"
NUM_PAGES = 50401
NXT_PAGE = "http://www.food.com/recipe?exclude=ass&pn="
RECIPE = re.compile("http://www\.food\.com/recipe/[\w\d-]+-\d+", flags=re.MULTILINE)

counter = set()
seen_recipes = set()


def parse_item(response):
    item = recipeItem()
    item['url'] = response['url']
    item['url'] = re.sub("\?.*", "", item['url'])
    return item


def get_recipe_links(start_page, stop_page):
    recipe_links = []
    for i in range(start_page, stop_page):
        url = NXT_PAGE + str(i)
        try:
            page = urllib2.urlopen(url).read()
        except Exception as e:
            print e
        else:
            for link in RECIPE.findall(page):
                if link and link not in seen_recipes:
                    seen_recipes.add(link)
                    yield link



def form_response(url):
    return {'url': url}


def run(start_page, stop_page):
    logging.info("Scraping pages %d:%d." % (start_page, stop_page))
    extractor = ExtractIngredientsPipeline()
    mongo = MongoWriterPipeline(settings)
    counter = 0
    for link in get_recipe_links(start_page, stop_page):
        try:
            item = extractor.process_item(parse_item(form_response(link)), None)

        except DropItem as e:
            print e
        except KeyError as e:
            print e
        except Exception as e:
            print e
        else:
            try:
                mongo.process_item(item, None)
                counter += 1
                if counter % 1000 == 0:
                    print "Recipe count: %d" % (counter,)
            except Exception as e:
                print e


if __name__ == '__main__':
    NUMTHREADS = 8
    #NUM_PAGES = 1
    logging.basicConfig(level=logging.INFO)

    for i in range(NUMTHREADS+1):
        thread = threading.Thread(target=run, args=((NUM_PAGES//NUMTHREADS) * i,
                                                    (NUM_PAGES//NUMTHREADS) * (i+1)))
        logging.info("Starting thread %d" % (i, ))
        thread.start()

    logging.info("All threads started.")

    for i in range(NUMTHREADS):
        thread.join()
        logging.info("Thread %d joined." % (i,))

