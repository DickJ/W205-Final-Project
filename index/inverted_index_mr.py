#!/usr/bin/env python

from mrjob.job import MRJob
import json

class InvertedIndex(MRJob):

    def mapper(self,docid,doc):
        doc = json.loads(doc)
        tf = {}
        tpos = {}
        pos = 0
        for term in doc['contents'].split():
            tf[term] = tf.get(term,0) + 1
            if term in tpos:
                tpos[term].append(pos)
            else:
                tpos[term] = [pos]
            pos += 1
        for term in tf:
            yield term, (doc['doc_id'], tf[term], tpos[term], pos+1)
        
    def reducer(self, term, postings):
        p = []
        for posting in postings:
            p.append(posting)
        yield term, p

if __name__=='__main__':
    InvertedIndex.run()
