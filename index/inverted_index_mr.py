import mrjob
from mrjob.job import MRJob
import ast
import re
import nltk
from nltk import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from recipewords import fullIngredients, measures, methods

def clean_str(line):
    line = line.strip()
    line = line.replace('\\t','')
    line = line.replace('\\n','')
    line = line.replace('\\r','')
    return line

def patch_ingred(ingredient):
    ingredient = ingredient.replace("&#174","")
    ingredient = re.sub(r'-','',ingredient)
    ingredient = re.sub(r'[\xf1]','n',ingredient)
    ingredient = re.sub(r'[^\x00-\x7F]',' ', ingredient)
    ingredient = re.sub(r'&nbsp','',ingredient)
    ingredient = re.sub(r'&#[0-9]+','',ingredient)
    ingredient = re.sub(r'&nbsp|&rarr|&larr','',ingredient)
    return ingredient

english_sw = nltk.corpus.stopwords.words('english')

def extract_key_ingred(ingredient):
    ingredient = ingredient.strip().lower()
    ingredient = patch_ingred(ingredient)
    #print "original ingredients {}".format(ingredient)
    tokenizer = RegexpTokenizer(r'\w+')
    tkn = tokenizer.tokenize(ingredient)
    ingredientList = list(set(fullIngredients.split('\n')))
    tkn = [t for t in tkn if \
           t in ingredientList and \
           t not in measures and \
           t not in methods and \
           t not in english_sw]
    ps = PorterStemmer()
    tkn = [ps.stem(t) for t in tkn]
    #tagged = nltk.pos_tag(tkn)
    #key_words = [w for w,tag in tagged if tag != 'LS' and tag != 'CD']
    #np = [w for w,tag in tagged if tag == 'NN'] # noun phrase
    #np = ' '.join(np)
    #if np not in key_words and len(np) > 0 and len(np.split()) <= 3:
    #    key_words.append(np)
    return tkn
    
class Indexing(MRJob):
    
    def mapper(self, _, line):
        if len(line) > 0:
            l = clean_str(line)
            data = ast.literal_eval(l)
            uid, ingredients = data['_id'],data['ingred']
            #tf = {}
            #tpos = {}
            #pos = 0
            for ingred in ingredients:
                for term in extract_key_ingred(ingred):
                    yield (term, uid)
                    #tf[term] = tf.get(term,0) + 1
                    #if term in tpos:
                    #    tpos[term].append(pos)
                    #else:
                    #    tpos[term] = [pos]
                    #pos += 1
                #for term in tf:
                    #yield term, (url, tf[term], tpos[term], pos+1)

    def reducer(self, term, postings):
        p = []
        for ps in postings:
            p.append(ps)
        yield (term, p)
    
    #def steps(self):
    #    return [MRStep(mapper=self.index_mapper,
    #                   combiner = self.index_combiner,
    #                   reducer=self.index_reducer)
    #            ]
                       
if __name__ == '__main__':
    Indexing.run()
