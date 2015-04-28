import mrjob
from mrjob.job import MRJob
import json
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
    return tkn
    
class Indexing(MRJob):
    
    def mapper(self, _, line):
        if len(line) > 0:
            #l = clean_str(line)
            data = json.loads(line.strip())
            uid, ingredients = data['_id']['$oid'],data['ingred']
            for ingred in ingredients:
                for term in extract_key_ingred(ingred):
                    yield (term, uid)

    def reducer(self, term, postings):
        p = []
        for ps in postings:
            p.append(ps)
        yield (term, p)
    
                       
if __name__ == '__main__':
    Indexing.run()
