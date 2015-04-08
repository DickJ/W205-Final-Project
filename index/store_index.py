import boto
from pymongo import MongoClient, errors
import re
import ast
from settings import *
import logging


client = MongoClient(MONGODB_URI)
pattern = re.compile('out/part-*')
db = client.get_default_database()
recipe_index = db[index_db]

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

keys = bk.get_all_keys()
for k in keys:
    if re.match(pattern, k.key):
        for line in download_from_s3(k):
            ingred, val = line.split('\t')
            ingred = ast.literal_eval(ingred)
            psts = ast.literal_eval(val)
            data = dict(zip(['ingredient','postinglist'],[ingred,psts]))
            for attempt in range(5):
                try:
                    recipe_index.insert(data)
                    break
                except errors.AutoReconnect:
                    wait_t = 0.5 * pow(2, attempt)
                    logging.warning("""
                            PyMongo auto-reconnecting...Attempt {}.
                            Waiting {} seconds.""".format(attempt, wait_t))
                    time.sleep(wait_t)              
