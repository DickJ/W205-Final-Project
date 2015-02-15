__author__ = 'joan'

from bs4 import BeautifulSoup
from scrape.extract_ingredients_allrecipes import thesaurus
import re
import os
import glob
import pandas as pd
import numpy as np
"""
Extract ingredients from html files (html files from Rich's Google Drive)
Clean up ingredients (using Rich's code)
Create inverted index: {ingredients : [html1, html2,...]} using a naive method

Notes:
    1.the inverted index method follows the 5-step in asynch with an assumption
      that one ingredient won't appear in a recipe multiple times. Therefore,
      step3 (aggregate count by term and doc#) is ignored
    2. html_name should be the actual site address in the final product
    3. restricted to allrecipe.com html format
    4. multi-keyword search not yet supported (next step)
"""
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
    line = line.split(",")[0]  # remove adj: ex. "tomatoes, chopped"
    line = line.split(" - ")[0]  # remove adj: ex. "avocado - peeled"
    if line in thesaurus.keys():  # ex. "salt" vs. "salt to taste"
        line = thesaurus[line]
    line = re.sub('^((fresh(ly)?)|(finely)) ((grated )|(ground ))?', '',
                    line)
    line = re.sub('^(diced )|(chopped )|(minced )', '',
                    line)  # remove preparation techniques
    line = re.sub(' to taste$', '', line)
    line = re.sub('(cooked)|(uncooked)', '', line)  # remove cooked status
    return line

# creates a mapping from ingredients to html filename
def ingredient_to_file(ingredients, fname):
    return {ingredient:fname for ingredient in ingredients}

# ingredient count
def igd_count(igd_sr):
    return igd_sr.groupby(by=igd_sr.index).count()



# read files from recipe folder
path = './recipe/'
s = pd.Series()
for filename in os.listdir(path):
    if glob.fnmatch.fnmatch(filename,'*.html'):
        f = open(filename, 'r')
        html = f.readlines()
        ingredients = get_ingredients(''.join(html))
        clean_ingredients = []
        for ingredient in ingredients:
            clean_ingredients.append(norm_ingredient(ingredient))
        ingredient_file_mapping = ingredient_to_file(clean_ingredients, filename)
        s = s.append(pd.Series(ingredient_file_mapping))

# step 2: sort by ingredients
sorted_map = s.sort_index()

# step 4: create frequency count (#doc associated = freq by assumption in notes)
count = igd_count(sorted_map)

# step 5: create ingredient mapping ({ingredient: [html1, html2,...]})
inv_ind = {}
for igd in count.index:
    inv_ind[igd] = np.array(sorted_map[igd])
