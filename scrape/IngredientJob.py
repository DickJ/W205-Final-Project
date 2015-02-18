__author__ = 'rich'
# Standard libraries
import os
import re
# Installed libraries
from nltk.corpus import stopwords
from mrjob.job import MRJob


# noinspection PyAbstractClass
class IngredientJob(MRJob):
    # noinspection PyAttributeOutsideInit
    def mapper_init(self):
        """
        Set class variables that will be useful to our mapper:
            filename: the path and filename to the current recipe file
            previous_line: The line previously parsed. We need this because the
              ingredient name is in the line after the tag
        """

        self.filename = os.environ["map_input_file"]
        self.previous_line = "None yet"
        # Determining if an item is in a list is O(n) while determining if an
        #  item is in a set is O(1)
        self.stopwords = set(stopwords.words('english'))

    @classmethod
    def process_text(cls, line):
        """
        This function makes all pre-processing modifications to line

        Currently, the only modifications being made are to strip leading and
        trailing whitespace as well as make the line lowercase. If, later,
        we decide to make more in-depth modifications, they can be created in
        this function

        :param line: a line of text as a str
        :return: a cleaned line of text
        """
        line = line.strip().lower()
        # I'm not using string.punctuation because I don't necessarily want to
        #  remove hyphens (-)
        line = re.sub(r'[!"#$%&\'()*+,./:;<=>?@[\\\]^_`{|}~]', '', line)
        return line

    # noinspection PyAttributeOutsideInit
    def mapper(self, _, line):
        """
        Takes a line from an html file and yields ingredient words from it

        Given a line of input from an html file, we check to see if it
        contains the identifier that it is an ingredient. Due to the
        formatting of our html files from allrecipes.com, the ingredient name
        is actually found on the following line. Therefore, we save the
        current line so that it can be referenced in the next pass of the
        function to determine if we are on an ingredient line.

        :param line: a line of text from the html file as a str
        :yield: a tuple containing each word in the ingredient as well as a
            counter for each word. The counter is not currently being used,
            but is left in for future development. e.g. "chicken breast" would
            yield "chicken" and "breast"
        """
        if re.search(r'span class="ingredient-name" id="lblIngName"',
                     self.previous_line):
            self.previous_line = line
            line = self.process_text(line)
            line_list = set(line.split())
            for word in line_list:
                if word not in self.stopwords:
                    yield word, 1
        else:
            self.previous_line = line
        yield '', 0

    def combiner(self, word, counts):
        """
        Combines counts of each word to pass to the reducer

        :param word:
        :param counts:
        :return:
        """
        yield (word, sum(counts))

    def reducer(self, word, counts):
        """
        The reducer

        :param word:
        :param counts:
        :return:
        """
        yield (word, sum(counts))
