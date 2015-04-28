import boto
from pymongo import MongoClient, errors
import re
import ast
from settings import MONGODB_URI,index_db
import logging
import time


client = MongoClient(MONGODB_URI)
pattern = re.compile('out/part-*')
db = client.get_default_database()
recipe_index = db['recipe_index']

MAX_AUTO_RECONNECT_ATTEMPTS = 5

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bk_name = 'joan-qiu-w205-finalproject-index'
bk = conn.get_bucket(bk_name)

def download_from_s3(key):
    print "downloading from s3://{}/{}...".format(bk_name,key.key)
    f = key.get_contents_as_string()
    print "Finish downloading."
    lines = f.strip().split('\n')
    del(f)
    for line in lines:
        yield line

#keys = bk.get_all_keys()
#for k in keys:
#    if re.match(pattern, k.key):
#        for line in download_from_s3(k):
datalist = []
for i in range(3):
    fname = 'data/part-0000{}'.format(i)
    print fname
    with open(fname) as f:     
        for line in f:
            ingred, psts = map(ast.literal_eval,line.split('\t'))
            data = dict(zip(['ingredient','postinglist'],[ingred,psts]))
            datalist.append(data)
    
recipe_index.insert(datalist)
