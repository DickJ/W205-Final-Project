__author__ = 'rich'

# Standard Library
import logging
import re

# Installed libraries
from mrjob.job import MRJob

# TODO This would be much better if it were alphabetized
# TODO There has to be a better way to implement this
thesaurus = {
    "barbeque sauce": "barbecue sauce",
    "salt and black pepper": "salt and pepper",
    "salt and black pepper to taste": "salt and pepper",
    "salt and freshly ground black pepper": "salt and pepper",
    "salt and freshly ground black pepper to taste": "salt and pepper",
    "salt and ground black pepper to taste": "salt and pepper",
    "salt and pepper to taste": "salt and pepper",
    "salt to taste": "salt",
    "freshly ground black pepper": "black pepper",
    "freshly ground pepper to taste": "black pepper",
    "boneless, skinless chicken breast halves": "chicken breast",
    "skinless, boneless chicken breast halves": "chicken breast",
    "skinless, boneless chicken breast halves - cubed": "chicken breast",
    "skinless, boneless chicken breast halves - cut into 1 inch cubes": "chicken breast",
    "skinless, boneless chicken breast halves - cut into 1 inch strips": "chicken breast",
    "skinless, boneless chicken breast halves - cut into bite-size pieces": "chicken breast",
    "skinless, boneless chicken breast halves - cut into thin strips": "chicken breast",
    "skinless, boneless chicken breast halves, cut into 1-inch cubes": "chicken breast",
    "skinless, boneless chicken breast halves, sliced": "chicken breast",
    "chopped, unsalted dry-roasted peanuts": "dry roasted peanuts",
    "warm water (110 degrees f)": "water",
    "warm water (110 degrees f/45 degrees c)": "water",
    "broken pieces vermicelli pasta": "vermicelli"
}


class IngredientJob(MRJob):
    def __init__(self, args=None):
        """

        :param args:
        :return:
        """
        self.previous_line = "None yet"
        super(IngredientJob, self).__init__(args)

    @staticmethod
    def process_text(line):
        """

        :param line:
        :return:
        """
        # NOTE \u00ae is TM symbol

        line = line.strip().lower()
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

        # TODO is everything that ends in 's' a plural ingredient?
        if re.search('(s$)', line):
            logging.info(line)

        line = line.strip()  # Clean up in case my regex missed a space
        return line

    def mapper(self, _, line):
        """

        :param _:
        :param line:
        :return:
        """
        if re.search(r'span class="ingredient-name" id="lblIngName"',
                     self.previous_line):
            self.previous_line = line
            line = self.process_text(line)
            if re.search("salt and pepper", line):
                yield "salt", 1
                yield "pepper", 1
            else:
                yield line, 1
        else:
            self.previous_line = line
        yield '', 0

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
    # usage: python extract_ingredients_allrecipes.py <source dir>
    #        --no-output --outputdir <output dir>
    IngredientJob.run()