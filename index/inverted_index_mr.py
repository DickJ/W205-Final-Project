# -*- coding: utf-8 -*-
import mrjob
from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class Indexing(MRJob):
    
    def configure_options(self):
        super(Indexing, self).configure_options()
        self.add_passthrough_option('--source',\
                                    help="Source location of recipe data (s3 or local)")
    
    def index_mapper(self, _, line):
        if len(line) > 0:
            docid, doc = line.split('\t')
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
                yield term, (docid, tf[term], tpos[term], pos+1)

    def index_reducer(self, term, postings):
        p = []
        for posting in postings:
            p.append(posting)
        yield term, p
    
    def steps(self):
        return [#MRStep(mapper=self.normalize),
                MRStep(mapper=self.index_mapper,
                       reducer=self.index_reducer)
                ]
                       
if __name__ == '__main__':
    Indexing.run()

