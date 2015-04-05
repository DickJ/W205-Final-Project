import boto
from pymongo import MongoClient
import re
import ast
from settings import *


client = MongoClient(MONGODB_URI)
pattern = re.compile('out/part-*')
db = client.get_default_database()
recipe_index = db[index_db]

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bk = conn.get_bucket('joan-qiu-w205-finalproject-index')
keys = bk.get_all_keys()
for k in keys:
    if re.match(pattern, k.key):
        print "downloading {}...".format(k.key)
        f = k.get_contents_as_string()
        print "Finish downloading."
        for line in f.strip().split('\n'):
            ingred, val = line.split('\t')
            ingred = ast.literal_eval(ingred)
            psts = ast.literal_eval(val)
            for ps in psts:
                posts = [{'url':p[0], 'title':p[1]} for p in ps]
                data = {'ingredient':ingred, 'postinglist': posts}
                recipe_index.insert(data)