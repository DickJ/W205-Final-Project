__author__ = 'cjllop'

from math import log
from nltk.corpus import inaugural

def tf(term, doc, normalize=True):
    doc = doc.lower().split()
    if normalize:
        return doc.count(term.lower()) / float(len(doc))
    else:
        return doc.count(term.lower()) / 1.0


def idf(term, corpus):
    num_doc_with_term = len([True for text in corpus if term.lower() in text.lower().split()])
    try:
        return 1.0 + log(float(len(corpus)) / num_doc_with_term)
    except ZeroDivisionError:
        return 1.0

def tf_idf(term, doc, corpus):
    return tf(term, doc) * idf(term, corpus)

corpus = \
    {'1':str(inaugural.raw('1789-Washington.txt')), \
    '2':str(inaugural.raw('1789-Washington.txt')), \
    '3':str(inaugural.raw('1797-Adams.txt')), \
    '4':"this is a sample string"}

corpus_list = [corpus['1'], corpus['2'], corpus['3']]

#print corpus['1']
print tf('apology', corpus['1'])
print tf('apology', corpus['2'])
print tf('apology', corpus['3'])
print idf('apology', corpus_list)

def query(term1, term2):
    for i in range(1,4):
        print tf_idf(term1, corpus[str(i)], corpus_list) \
                + tf_idf(term2, corpus[str(i)], corpus_list)

query('states','revolution')
