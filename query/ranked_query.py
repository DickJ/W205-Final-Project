__author__ = 'cjllop'

# TODO: FIRST DRAFT OF CODE STILL IN PROGRESS - DOES NOT WORK (YET)
import re
import ast
from operator import itemgetter

def get_query():
    query = raw_input("What ingredients do you have (separated by spaces): ")
    # TODO: Remove invalid input
    return query

def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search



if __name__ == '__main__':
    query = get_query()

    # TODO: Think thru if we can sort the postings list in a way to reduce the query time.
    # TODO:     any such sorting will need to be coordinated with the MapReduce output
    # TODO:     (perhaps via rank_index.py).


    query_postings = []
    # Check ranked postings list, save postings to one list for all that match query
    for line in open("../index/rankedout/part-00000",'r'):
        post_term, post_list = line.split('\t', 1)
        post_term = re.sub('"', '', post_term)
        if find_whole_word(post_term)(query) is not None:
            post_list = ast.literal_eval(post_list)
            #post_term_list = [post_term, post_list]
            #for posting in post_list:
            query_postings = query_postings + post_list

    # Sort results list
    #print sorted(query_postings)
    #print sorted(query_postings, reverse=True)
    #print sorted(query_postings, key= itemgetter(1))
    query_postings = sorted(query_postings)
    print query_postings

    # Add up tf-idf rank for each document
    last_posting = []
    query_tfidf = []
    summer = 0.0

    for posting in query_postings:
        # Once all postings for a document are summed, save to query_tfidf and move to next document
        if last_posting == [] or posting[0] != last_posting[0]:
            if last_posting != []:
                query_tfidf.append([last_posting[0], summer])
            last_posting = posting
            summer = 0.0
        # Add rank data for same document
        summer = summer + posting[1]

    #print query_tfidf
    #print sorted(query_postings, key= itemgetter(1))
    #print sorted(query_postings, key= itemgetter(1), reverse=True)
    sorted_results = sorted(query_postings, key= itemgetter(1), reverse=True)

    print
    print "Search results for: " + query
    for result in sorted_results:
        print "Recipe #" + str(result[0]) + " (" + str(result[1]) + ")"

    # TODO: Think thru some sample queries to improve ranking algorithm