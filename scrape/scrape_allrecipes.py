__author__ = 'Rich Johnson'

from httplib import BadStatusLine
import logging
import os
import Queue
import re
import threading
import time

from bs4 import BeautifulSoup
import pickle
import urllib2


def get_recipe_links():
    """
    This function returns a list of links to all the recipes on allrecipes.com
    This function spiders allrecipes.com list of recipes. Only 20 recipes are
    displayed per page. The spider runs through all pages to extract links to
    every recipe. A Queue of links is created and returned. This function has
    been updated to multi-thread the request of pages of recipes.
    Returns:
        a Queue of all the recipe links as BeautifulSoup objects
    Raises:
        All exceptions are logged and handled, none are raised
    """

    def find_links(page_queue, links_queue):
        """
        Downloads individual recipe links from a recipe index page
        This functions pulls an item off of page_queue, requests the page,
        extracts the links to recipes from the page, and adds each link (as a
        BeautifulSoup object) to the queue links_queue
        Parameters:
            page_queue: A queue of index pages containing links to recipes
            links_queue: a queue for placing urls for individual recipes
        Raises:
            All exceptions are logged and handled, none are raised
        """

        while not page_queue.empty():
            page = page_queue.get()
            logging.info("get_recipe_links():find_links(): processing page "
                         "%s" % page)
            recipe_list = BeautifulSoup(urllib2.urlopen(page).read())
            all_links = recipe_list.find_all('a')
            url_re = re.compile('(^(?P<url>http://allrecipes.com/(r|R)ecipe/.+)/.*$)')
            for link in all_links:
                try:
                    if (re.search(
                            r"ctl00_CenterColumnPlaceHolder_RecipeContainer_rptGridView_ctl\d\d_ucGridItem_lnkTitle",
                            link['id'])
                    ):
                        recipe_url = ''.join(('http://allrecipes.com',
                                              link['href']))
                        # Remove the trailing parts of the url leaving only
                        # http://allrecipes.com/Recipe/recipe-name/
                        recipe_url = url_re.match(recipe_url).group(2)
                        logging.info("get_recipe_links():find_links(): adding"
                                     " link %s to links_queue" % recipe_url)
                        links_queue.put(recipe_url)
                except KeyError:
                    # logging.exception(
                    # "%s on page %s does not have an 'id' tag" %
                    # (link['href'], page))
                    pass
                except AttributeError:
                    # logging.exception("Attribute Error: %s" % link)
                    pass

    recipe_list_pages = Queue.Queue()
    recipe_links = Queue.Queue()
    numthreads = 8
    logging.info("get_recipe_links(): Number of threads = %d" % numthreads)

    for i in range(1, 2522):  # 2521 is currently the last page. (16 Feb 15)
        url = 'http://allrecipes.com/recipes/main.aspx?Page=' + str(i) + \
              '#recipes'
        recipe_list_pages.put(url)
        logging.info("get_recipe_links(): %s added to recipe_list_pages queue"
                     % url)

    for i in range(numthreads):
        thread = threading.Thread(target=find_links, args=(recipe_list_pages,
                                                           recipe_links))
        thread.daemon = True
        logging.info("get_recipe_links(): Starting thread %d" % i)
        thread.start()
    for i in range(numthreads):
        # noinspection PyUnboundLocalVariable
        thread.join()
        logging.info("get_recipe_links(): Thread %d has joined" % i)
    logging.info("get_recipe_links(): All threads have joined")

    time.sleep(2)
    logging.info("get_recipe_links(): Returning ~%d recipe links" %
                 recipe_links.qsize())
    return recipe_links


def download_recipes(recipe_links):
    """
    Downloads and saves to disk full page recipes from allrecipes.com
    Each link will be popped off the list (stack), downloaded, and saved to
    disk for later analysis. For the time being, I will single thread it so as
    not to irritate allrecipes.com with 2000 requests/second.
    This function can realize a significant performance increase by
    multi-threading both the queries and the writes to disk
    Parameters:
        recipe_links: a queue of recipes from allrecipes.com
    Returns:
        None
    """

    def download_recipe(links_queue):
        """
        Thread function to download individual recipes
        Parameters:
            links_queue: a queue of urls to individual recipes (as strings)
        """

        while not links_queue.empty():
            recipe_url = links_queue.get()
            recipe_name = recipe_url.split('/')[4]
            recipe_file_name = ''.join(('recipes/allrecipes/', recipe_name,
                                        '.html'))
            if not os.path.isfile(recipe_file_name):
                try:
                    recipe = BeautifulSoup(urllib2.urlopen(recipe_url))
                    logging.info("Downloading recipe: %s" % recipe_file_name)
                    with open(recipe_file_name, 'w') as recipe_file:
                        recipe_file.write(recipe.prettify('utf-8', 'ignore'))
                except BadStatusLine:
                    logging.error("ERROR: Could not download %s at %s. Trying"
                                  " one more time" % (recipe_name, recipe_url))
                    time.sleep(2)
                    try:
                        recipe = BeautifulSoup(urllib2.urlopen(recipe_url))
                        logging.info(
                            "Downloading recipe: %s" % recipe_file_name)
                        with open(recipe_file_name, 'w') as recipe_file:
                            recipe_file.write(
                                recipe.prettify('utf-8', 'ignore'))
                    except BadStatusLine:
                        logging.error("ERROR: Attempt 2 to download %s "
                                      "failed" % recipe_url)
            else:
                logging.info("%s already downloaded" % recipe_file_name)

    numthreads = 8

    for i in range(numthreads):
        thread = threading.Thread(target=download_recipe, args=(recipe_links,))
        thread.daemon = True
        logging.info("download_recipe(): Starting thread %d" % i)
        thread.start()
    for i in range(numthreads):
        thread.join()
        logging.info("download_recipe(): Thread %d has joined" % i)
    logging.info("download_recipe(): All threads have joined")
    time.sleep(2)


def dump_queue(queue):
    """
    Takes a Queue and returns it as a list

    This function is pretty straightforward with the one problem that
    queue.get() removes the results from the queue. This is remedied by
    re-enqueuing each item before returning from the function.

    :param queue: A Queue of items
    :return: a list containing the contents of queue
    """
    result = []
    # This is going to empty the queue, as such, we will need to requeue
    # everything before returning from this function
    while not queue.empty():
        result.append(queue.get())
    for entry in result:
        queue.put(entry)
    return result


if __name__ == '__main__':
    # Set up directory structure to ensure no errors are thrown
    if not os.path.exists("./recipes/allrecipes"):
        os.makedirs("./recipes/allrecipes")  # makedirs is recursive
    if not os.path.exists("./logs/"):
        os.mkdir("./logs/")
    if not os.path.exists("./data/"):
        os.mkdir("./data/")


    RUN_LOG = ''.join(('logs/run_log_', str(time.time()), '.log'))
    RECIPE_LINKS_PICKLE_FILE = 'data/recipe_links.pkl'
    a = Queue.Queue()

    logging.basicConfig(filename=RUN_LOG, level=logging.INFO,
                        format='%(asctime)s %(message)s')
    logging.info("RECIPE LINKS PICKLE FILE: %s" % RECIPE_LINKS_PICKLE_FILE)

    # Download the recipes if the pickle file doesn't exist. If the pickle file
    # does exist, just load it up and continue from there.
    if not os.path.isfile(RECIPE_LINKS_PICKLE_FILE):
        a = get_recipe_links()
        with open(RECIPE_LINKS_PICKLE_FILE, 'w') as pickle_file:
            a_list = dump_queue(a)
            pickle.dump(a_list, pickle_file)
        logging.info("main: downloaded all recipe links")
    else:
        with open(RECIPE_LINKS_PICKLE_FILE, 'r') as pickle_file:
            a_list = pickle.load(pickle_file)
            for b in a_list: a.put(b)
        logging.info("main: loaded all recipe links")

    print("Downloading started at %s" % time.asctime())
    logging.info("main: Downloading recipes started")
    download_recipes(a)
    logging.info("main: Downloading recipes completed")
