__author__ = 'cjllop'

import ast
import json
import os
from math import log

# Note: We could probably do this more effectively by having Joan's InvIndex code update as
    # master count of the corpus size and num docs whenever it adds to the index.
# Note: Current InvIndex lists the doc size in each count, however this data is replicated
    # for each postings list. This could be more effectively saved elsewhere, for example in a
    # document that contains: DocID, Hyperlink, Word Count, Title
def get_corpus_length():
# Assumption: Each file in "data/" is a JSON file with file information on a unique
# element of the posting list
    corpus_length = 0
    for filename in os.listdir('data/'):
        try:
            f = open('data/' + filename, 'r')
            f_data = json.loads(f.readline())
            corpus_length += len(f_data[u'contents'].split())
        except Exception:
            print "Trouble opening one of the raw data file. Skipping."
            pass
    return corpus_length


if __name__ == '__main__':

    # corpus length needed for IDF calculation
    corpus_length  = get_corpus_length()

    # This can be replaced by a loop through mrout when we have more than one file (Hadoop)
    for line in open("mrout/part-00000",'r'):
        post_term, post_list = line.split('\t', 1)
        post_list = ast.literal_eval(post_list)
        #print post_term
        #print post_list

        # Calculate IDF for term
        try:
            idf = 1.0 + log(float(corpus_length) / len(post_list))
        except ZeroDivisionError:
            idf = 1.0

        # Calculate TF and TF-IDF for document
        for posting in post_list:
            tf = float(posting[1]) / posting[3]
            print "Document " + str(posting[0]) + " has term " + post_term + " " + str(posting[1]) + " times."
            #print "The TF is: " + str(tf)
            #print "The IDF is: " + str(idf)
            tf_idf = tf * idf
            print "The TF-IDF is: " + str(tf_idf)
            posting.append(tf_idf)
            #print posting

        # Save postings list with appended rank

        #print post_list
        outline = post_term + '\t' + str(post_list)
        with open("rankedout/part-00000", 'a') as outfile:
            outfile.write(outline + '\n')
        #print
        print
