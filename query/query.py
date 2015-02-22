__author__ = 'joan'
import index.inverted_index as ii
import operator
"""
"""
# we can come up with a ranking system later
# potentially we want to put the more important ingredients in the front
# e.g. salt, tomato, chicken -> chicken, tomato, salt
def rank_ingredients(igds):
    return igds

def sort_by_rank(p):
    # sort pages by rank
    pages = sorted(p.items(),key=operator.itemgetter(1), reverse = True)
    return [page[0] for page in pages]

def tokenize(search_txt):
    clean_search = ii.norm_ingredient(search_txt)
    return clean_search.strip().split(' ')

# query takes in a list of ingredients
# returns a list of pages, can be empty
def query(search, ind):
    igds = tokenize(search)
    # if no ingredients queried is found, return []
    if not filter(lambda x: x in ind, igds):
         return []
    count = len(igds)
    pages = {}
    # for now ranking is a dummy function
    ranked_igds = rank_ingredients(igds)
    # for each token, find corresponding link in ind
    for igd in ranked_igds:
        if igd in ind:
            #print igd
            # convert np.array to list
            for page in ind[igd]:
                if page in pages:
                    # count here takes into account the order of input
                    # we can add other factors in here to surface up
                    # good matches
                    pages[page] += count + 1
                else:
                    pages[page] = count + 1
        count -= 1
    return pages

path = 'recipe/'
ind = ii.create_index(path)

test_igds_1 = 'chicken, sweet potato'
test_igds_2 = 'noodles, shrimp, sprouts'
test_igds_3 = 'mahi mahi, tomato'

p = query(test_igds_3, ind)
if p:
    print sort_by_rank(p)
