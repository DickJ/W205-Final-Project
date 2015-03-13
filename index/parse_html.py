import urllib2
from HTMLParser import HTMLParser
import lxml.html as LH
import re


def extract_html(url):
    response = urllib2.urlopen(url)
    html = response.read()
    response.close()
    return html


def extract_text(htm):
    # I was getting errors with lxml.html. ... so I changed the import (see
    # above) and rewrote it as this. It works for me this way. Does anyone
    # understand why this happens?

    return LH.fromstring(htm).text_content()


def extract_ingredients(html, ing):
    """

    :param html: a webpage
    :param ing: a set (changed from a dict in prev version)
    :return:
    """
    texts = extract_text(html)
    ingred = []
    for line in texts.split('\n'):
        for word in line.split():
            # Clean each word before attempting to look for it
            word = word.strip().lower()
            word = re.sub(r'[!"#$%&\'()*+,./:;<=>?@[\\\]^_`{|}~]', '', word)
            # TODO I need to look in to why empty strings are present, but I
            # haven't looked yet.
            if word in ing and word != u'':
                ingred.append(word)
    # Just my preference for a list rather than a concatenated string. Feel
    # free to change
    return ingred
    # return ' '.join(ingred)


if __name__ == '__main__':
    # I made this a set because we aren't holding anything of use in the
    # dictionary value and all we need are the keys.
    ing_set = set()
    # My filename is different so I changed that here, if you get an error,
    # double check your filename.
    with open('full_ingredient_list.txt') as f:
        lines = f.read()
        # Why did you split on \r? The file looks like it uses \n for newlines
        for ing in lines.split('\n'):
            ing_set.add(ing)

    # The list just makes it easier for me to select which one I want or to
    # iterate over all of them. Feel free to change.
    url = [
        "http://www.food.com/recipe/crock-pot-chicken-with-black-beans-cream-cheese-89204",
        "http://allrecipes.com/Recipe/Brown-Sugar-Meatloaf/Detail.aspx?evt19=1&referringHubId=1",
        "http://www.yummly.com/recipe/Marinated-Eggplant-627903?columns=5&position=17%2F35",
        "http://www.chow.com/recipes/31280-orecchiette-spicy-sausage-brown-butter-sage",
        "http://www.simplyrecipes.com/recipes/celery_root_fennel_soup/",
        "http://www.bettycrocker.com/recipes/impossibly-easy-mini-chicken-pot-pies/9a1006cf-5b40-4c87-acd8-9c3436210129",
        "http://www.kraftrecipes.com/recipes/tater-topped-casserole-111257.aspx"
    ]

    html = extract_html(url[1])
    a = extract_ingredients(html, ing_set)
    print a