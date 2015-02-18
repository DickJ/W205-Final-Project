__author__ = 'rich'

# Standard Library
import re
import sys
# Our libraries
from IngredientJob import IngredientJob


def make_list(path):
    """
    Takes a path containing MapReduce output and creates a list of items in it

    We expect that the MapReduce file is named "part-00000" and that it
    contains data in the format '"ingredient_name"\tcount'. We assume any
    trailing punctuation has been stripped off the ingredient name already.
    After the regex matches the ingredient word should be stored in group(1).
    Finally, all of the ingredient words are written to a txt file.

    :param path: a path containing a emr output file to process
    """
    items = []
    with open(''.join((path, 'part-00000')), 'r') as fh:
        for line in fh:
            i = re.match('^"(\w+)"\t', line)
            if i:
                items.append(i.group(1))

    with open("data/ingredients.txt", "w") as wf:
        for ingr in items:
            wf.write(ingr + "\n")


if __name__ == '__main__':
    # usage: python extract_ingredients_allrecipes.py <source dir>
    #        --no-output --output-dir <output dir>
    IngredientJob.run()
    # This should probably go in a separate script
    make_list(sys.argv[4])