__author__ = 'rich'

import logging
import os
import cPickle
import sys

from bs4 import BeautifulSoup


def process_file(filename):
    """
    Opens an html file and returns a list of all the ingredients in it

    :param filename: a filehandle for a single html recipe file
    :return: a list of ingredients found in the file
    """
    ingredient_list = []
    soup = BeautifulSoup(open(filename))
    for ingred in soup.find_all(id="lblIngName"):
        ingredient_string = ingred.text.strip().lower()  # these are unicode
        ingredient_list.append(ingredient_string)
    return ingredient_list


if __name__ == '__main__':
    # usage: ./extract_ingredients_allrecipes.py <path to recipes>
    #  /Users/rich/Desktop/recipes/allrecipes/

    logging.basicConfig(level=logging.INFO)
    pickle_file = "data/ingredients.pkl"

    ingredient_dict = {}

    for recipe_file in os.listdir(sys.argv[1]):
        logging.info("Processing %s" % recipe_file)
        ingredients = process_file(''.join((sys.argv[1], recipe_file)))
        for ingredient in ingredients:
            if ingredient in ingredient_dict.keys():
                ingredient_dict[ingredient] += 1
            else:
                ingredient_dict[ingredient] = 1

    with open(pickle_file, 'w') as p:
        cPickle.dump(ingredient_dict, p)