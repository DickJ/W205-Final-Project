__author__ = 'Rich Johnson'

from datetime import datetime, tzinfo
import re
from hb_items import recipeItem
import logging
from hb_pipelines import ExtractIngredientsPipeline, MongoWriterPipeline
import Queue
from scrapy.exceptions import DropItem
from hb_settings import settings
import threading
import urllib2
import time
import pymongo

NUMTHREADS = 1
START_URL = "http://www.food.com/recipe?exclude=ass&pn=1"
NUM_PAGES = 50401
NXT_PAGE = "http://www.food.com/recipe?exclude=ass&pn="
RECIPE = re.compile("http://www\.food\.com/recipe/[\w\d-]+-\d+",
                    flags=re.MULTILINE)

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


def run(start_page, stop_page, coll, mongo_queue, progress_q):

    logging.info("Scraping pages %d:%d." % (start_page, stop_page))
    extractor = ExtractIngredientsPipeline()
    for link in get_recipe_links(start_page, stop_page):
        if not coll.find_one({'url': link}):
            try:
                item = extractor.process_item(parse_item(form_response(link)),
                                              None)
            except DropItem as e:
                print e
            except KeyError as e:
                print e
            except Exception as e:
                print e
            else:
                try:
                    mongo_queue.put(item)
                    progress_q.put(1)
                except Exception as e:
                    print e
        else:
            logging.debug("%s already in database." % (link,))

def mongo_writer(mongo_queue):
    logging.info("Mongo thread started.")
    mongo = MongoWriterPipeline(settings)
    while True:
        try:
            item = mongo_queue.get()
            if item == "END":
                return
            else:
                logging.info("adding %s" % (item['url'],))
                mongo.process_item(item, None)
        except:
            pass

def progress(q):
    logging.info("Progress thread started.")
    counter = 0
    print "Started at %s: " % (datetime.now().isoformat(' '), )
    while True:
        try:
            c = q.get()
            if c == "END":
                return 0
            else:
                counter += int(c)
        except:
            pass
        else:
            if counter % 2000 == 0:
                print "%s: Acquired %d recipes" % (
                    datetime.now().isoformat(' '), counter)


if __name__ == '__main__':
    q = Queue.Queue()
    mongo_q = Queue.Queue()
    conn = pymongo.MongoClient(settings['MONGODB_SERVER'],
                               settings['MONGODB_PORT'])
    db = conn[settings['MONGODB_DB']]
    db.authenticate(settings['MONGODB_USER'], settings['MONGODB_PW'])
    coll = db[settings['MONGODB_COLLECTION']]
    logging.basicConfig(level=settings['LOG_LEVEL'])

    for i in range(NUMTHREADS + 1):
        thread = threading.Thread(target=run,
                                  args=((NUM_PAGES // NUMTHREADS) * i,
                                        (NUM_PAGES // NUMTHREADS) * (i + 1),
                                        coll, mongo_q, q))
        logging.debug("Starting thread %d" % (i, ))
        thread.start()
    logging.info("All threads started.")

    progress_thread = threading.Thread(target=progress, args=(q,))
    progress_thread.start()

    mongo_thread = threading.Thread(target=mongo_writer, args=(mongo_q,))
    mongo_thread.start()

    for i in range(NUMTHREADS):
        thread.join()
        logging.info("Thread %d joined." % (i,))
        q.put("END")
        mongo_q.put("END")

    thread.join()
    thread.join()