__author__ = 'joan'

from bs4 import BeautifulSoup
from scrape.extract_ingredients_allrecipes import thesaurus
import re
import os
import glob

"""
Extract ingredients from html files (html files from Rich's Google Drive)
Clean up ingredients (using Richard's txt file)
Create inverted index: {ingredients : [html1, html2,...]} using a naive method

Notes:
    1.the inverted index method follows the 5-step in asynch with an assumption
      that one ingredient won't appear in a recipe multiple times. Therefore,
      step3 (aggregate count by term and doc#) is ignored
    2. html_name should be the actual site address in the final product
    3. restricted to allrecipe.com html format
"""
# all_ingredients: file -> {all ingredients scraped}
def all_ingredients(igd_fl):
    all_igd = {}
    with open(igd_fl) as f:
        igds = f.read().split()
        for igd in igds:
            all_igd[igd] = 1
    return all_igd

# get_ingredients takes in one html and returns the ingredients from the site
def get_ingredients(html):
    soup = BeautifulSoup(''.join(html))
    ingredients = []
    for tag in soup.find_all('span',{'class':'ingredient-name', 'id':"lblIngName"}):
        ingredients.append(tag.text.strip())
    return ingredients

# normalize ingredients
def norm_ingredient(ingredient):
    line = ingredient.strip().lower()
    line = re.sub(r'[!"#$%&\'()*+,./:;<=>?@[\\\]^_`{|}~]', '', line)
    return line

# create_index directory of html files -> {ingredient: set(html_files)}
def create_index(path):
    # loop through directory for all .html files
    ind = {}
    for filename in os.listdir(path):
        if glob.fnmatch.fnmatch(filename,'*.html'):
            f = open(path+filename, 'r')
            html = f.readlines()
            ingredients = get_ingredients(''.join(html))  
            for ingredient in ingredients:
                # tokenize ingredients
                tokens = ingredient.split(' ')
                for token in tokens:
                    clean_igd = norm_ingredient(token)
                    all_igds = all_ingredients('index/full-ingred-word-list.txt')
                    if clean_igd in all_igds:
                        if clean_igd not in ind:
                            ind[clean_igd] = set([filename])
                        else:
                            ind[clean_igd] |= set([filename])
    return ind    

# read files from recipe folder
if __name__ == '__main__':
    path = './recipe/'
    create_index(path)

################################################################
""" 
the following are just for analytical purpose
for instance, figure out the highest frequency of ingredients
which can help us do the page ranking, adding stop words etc.
"""
#s = pd.Series(inv_ind)

## create a data frame of with ingredient being index
## two columns: links and count
#s['count'] = s.links.map(lambda x: len(x))
#s.sort(['count'], ascending = False, inplace = True)

## step 2: sort by ingredients
# sorted_map = s.sort_index()

# step 4: create frequency count (#doc associated = freq by assumption in notes)
# count = igd_count(sorted_map)

# step 5: create ingredient mapping ({ingredient: [html1, html2,...]})
    
