__author__ = 'rich'
import re
from mrjob.job import MRJob
#from nltk.corpus import stopwords

class Job(MRJob):

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
        # remove hyphens (-)
        line = re.sub(r'[!"#$%&\'()*+,./:;<=>?@[\\\]^_`{|}~]', '', line)
        return line

    def mapper_init(self):
        """
        Set class variables that will be useful to our mapper:
            filename: the path and filename to the current recipe file
            previous_line: The line previously parsed. We need this because the
              ingredient name is in the line after the tag
        """

        #self.filename = os.environ["map_input_file"]  # Not currently used
        self.previous_line = "None yet"
        # Determining if an item is in a list is O(n) while determining if an
        #  item is in a set is O(1)
        #self.stopwords = set(stopwords.words('english'))
        # I changed it to this so we do not have to bootstrap nltk.corpus when
        #  we run on EMR
        self.stopwords_list = ['i', 'me', 'my', 'myself', 'we', 'our',
                          'ours',  'ourselves', 'yo', 'your', 'yours',
                          'yourself', 'yourselves', 'he', 'him', 'his',
                          'himself', 'she', 'her', 'hers', 'herself',
                          'it', 'its', 'itself', 'they', 'them', 'their',
                          'theirs', 'themselves', 'what', 'which', 'who',
                          'whom', 'this', 'that', 'these', 'those', 'am',
                          'is', 'are', 'was', 'were', 'be', 'been',
                          'being', 'have', 'has', 'had', 'having', 'do',
                          'does', 'did', 'doing', 'a', 'an', 'the',
                          'and', 'but', 'if', 'or', 'because', 'as',
                          'until', 'while', 'of', 'at', 'by', 'for',
                          'with', 'about', 'against', 'between', 'into',
                          'through', 'during', 'before', 'after', 'above',
                          'below', 'to', 'from', 'up', 'down', 'in',
                          'out', 'on', 'off', 'over', 'under', 'again',
                          'further', 'then', 'once', 'here', 'there',
                          'when', 'where', 'why', 'how', 'all', 'any',
                          'both', 'each', 'few', 'more', 'most', 'other',
                          'some', 'such', 'no', 'nor', 'not', 'only',
                          'own', 'same', 'so', 'than', 'too', 'very',
                          's', 't', 'can', 'will', 'just', 'don',
                          'should', 'now']
        self.stopwords = set(self.stopwords_list) # For O(1) searching


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

        # TODO is there a better way to get the tag?
        if re.search(r'span class="ingredient-name" id="lblIngName"',
                     self.previous_line):
            self.previous_line = line
            line = self.process_text(line)
            line_list = set(line.split())
            for word in line_list:
                if word not in self.stopwords:
                    yield (word, 1)
        else:
            self.previous_line = line

        yield ('', 0)
        '''
        words = line.split()
        for word in words:
            yield (word, 1)'''

    def combiner(self, word, counts):
        yield (word, sum(counts))

    def reducer(self, word, counts):
        yield (word, sum(counts))


if __name__ == '__main__':
    Job.run()
    # python test_try.py -r emr s3://rich-johnson-artest/ --conf-path mrjob.conf --no-output --output-dir s3://rich-johnson-w205-finalproject/out/
