import mrjob
from mrjob.job import MRJob
import ast
import nltk
from nltk import PorterStemmer
from nltk.tokenize import RegexpTokenizer, word_tokenize

def clean_str(line):
    line = line.strip()
    line = line.replace('\\t','')
    line = line.replace('\\n','')
    line = line.replace('\\r','')
    return line

measures = ['ounce','ounces','cup','cups','pound','pounds','kilos',\
            'grams','gram','kilo','bag','bags','teaspoon',\
            'teaspoons','tablespoon','tablespoons','tbsp','tbsps',\
            'lbs','kg','kilogram','kilograms','can','cans',\
            'tsp','tsps','oz','pint','pt','pints','pack','packs','packed']

english_sw = nltk.corpus.stopwords.words('english')

methods = ['grounded','crushed', 'chopped']

def extract_key_ingred(ingredient):
    ingredient = ingredient.strip().lower()
    #print "original ingredients {}".format(ingredient)
    tokenizer = RegexpTokenizer(r'\w+')
    tkn = tokenizer.tokenize(ingredient)
    ps = PorterStemmer()
    tkn = [ps.stem(t) for t in tkn if t not in measures and t not in methods and t not in english_sw]
    #print tkn
    tagged = nltk.pos_tag(tkn)
    #print tagged
    key_words = [w for w,tag in tagged if tag != 'LS' and tag != 'CD']
    np = [w for w,tag in tagged if tag == 'NN'] # noun phrase
    np = ' '.join(np)
    if len(np) > 0 and np not in key_words:
        key_words.append(np)
    return key_words
    
class Indexing(MRJob):
    
    def mapper(self, _, line):
        if len(line) > 0:
            l = clean_str(line)
            data = ast.literal_eval(l)
            url, ingredients, title = data['url'],data['ingred'],data['title']
            #tf = {}
            #tpos = {}
            #pos = 0
            for ingred in ingredients:
                for term in extract_key_ingred(ingred):
                    yield term, (url, title)
                    #tf[term] = tf.get(term,0) + 1
                    #if term in tpos:
                    #    tpos[term].append(pos)
                    #else:
                    #    tpos[term] = [pos]
                    #pos += 1
                #for term in tf:
                    #yield term, (url, tf[term], tpos[term], pos+1)

    def combiner(self, term, postings):
        p = []
        for post in postings:
            p.append(post)
        yield term, p

    def reducer(self, term, postings):
        p = []
        for post in postings:
            p.append(post)
        yield term, p
    
    #def steps(self):
    #    return [MRStep(mapper=self.index_mapper,
    #                   combiner = self.index_combiner,
    #                   reducer=self.index_reducer)
    #            ]
                       
if __name__ == '__main__':
    Indexing.run()
