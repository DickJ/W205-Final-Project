__author__ = 'rich'
"""
This file is specialized for one directory. It is included for reference if
it becomes useful to someone. It will need to be re-coded for general use.

This scrip takes a directory with a large number of input files and
partitions them so that processing may be done easier. After the files are
partitioned, a shell script is generated for a MapReduce job to be performed
on each partition. Finally, the output of the MapReduce jobs are aggregated
via another MapReduce job that will produce one final output file."
"""

import os
import glob
import shutil

from mrjob.job import MRJob

class ReJob(MRJob):
    def mapper(self, _, line):
        a = line.split("\t")
        a[0].strip('\\"')
        yield (a[0], int(a[1]))

    def combiner(self, key, value):
        yield (key, sum(value))

    def reducer(self, key, value):
        yield(key, sum(value))


def movefiles():

    olddir = os.getcwd()
    os.chdir('/media/sf_Desktop/recipes/allrecipes/')
    i = 0
    for recipe in glob.iglob("*.html"):
        folder = ''.join(("recipes", str(i%100)))
        if not os.path.exists(folder): os.mkdir(folder)
        shutil.move(recipe, os.path.join(folder, recipe))
        i += 1
    os.chdir(olddir)

def writebash():
    with open("kill.sh", "w") as sf:
        sf.write("#!/bin/sh\n")
        countdir = 1
        alldirs = os.walk("/media/sf_Desktop/recipes/allrecipes/")
        outdir = ''.join(("scrape/data/out/", str(countdir)))
        ad = next(alldirs)
        for d in ad[1]:
            dir = ''.join(('/media/sf_Desktop/recipes/allrecipes/', d))
            c = ''.join(('python extract_ingredients_allrecipes.py ', dir,
                         ' --no-output --output-dir ', outdir, "\n"))
            sf.write(c)
            countdir += 1

def cfiod(): #combine files in one directory
    a = os.walk("data/out")
    b = next(a)
    outdirs = b[1]
    count = 0
    #for dir in range(1:101)
    for dir in outdirs:
        ofn = ''.join(("data/out/", str(count), ".txt"))
        shutil.move(os.path.join("data/out", dir, "part-00000"), ofn)
        count += 1

if __name__ == '__main__':
    movefiles()
    writebash()
    cfiod()
    ReJob.run()
