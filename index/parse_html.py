import urllib2
from HTMLParser import HTMLParser
import lxml

def extract_html(url):
    response = urllib2.urlopen(url)
    html = response.read()
    response.close()
    return html

def extract_text(html):
    return lxml.html.fromstring(html).text_content()

def extract_ingredients(html):
    texts = extract_text(html)
    ingred = []
    for line in texts.split('\n'):
        for word in line.split():
            if word in ing_dic:
                ingred.append(word)
    return ' '.join(ingred)
               
ing_dic = {}
with open('full-ingred-word-list.txt') as f:
    lines = f.read()
    for ing in lines.split('\r'):
        ing_dic[ing] = 1

#url = "http://www.food.com/recipe/crock-pot-chicken-with-black-beans-cream-cheese-89204"
#url = "http://allrecipes.com/Recipe/Brown-Sugar-Meatloaf/Detail.aspx?evt19=1&referringHubId=1"
#url = "http://www.yummly.com/recipe/Marinated-Eggplant-627903?columns=5&position=17%2F35"
#url = "http://www.chow.com/recipes/31280-orecchiette-spicy-sausage-brown-butter-sage"
#url = "http://www.simplyrecipes.com/recipes/celery_root_fennel_soup/"
#url = "http://www.bettycrocker.com/recipes/impossibly-easy-mini-chicken-pot-pies/9a1006cf-5b40-4c87-acd8-9c3436210129"
url = "http://www.kraftrecipes.com/recipes/tater-topped-casserole-111257.aspx"

html = extract_html(url)
extract_ingredients(html)