import sys
import tweepy
import datetime
import urllib
import signal
import json
consumer_key = "47fJitjFeX8ZYypIMgRo1TSiS"
consumer_secret = "Iux0CexhSJc61FyK2cuCNQF1xJztGU9U9kO3OnT61oJEGiacWe"

access_token = "301139223-YuwBh0WF5p8to52p5h9zHPcLMjxDUtTP7q2Mp0sa"
access_token_secret = "cv49Rti3qM62S41ZjtbMbuJdz5VYUqGhQjUX9LnCBcwTp"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)import pymongo
from pymongo import MongoClient
#conn=pymongo.MongoClient('mongodb://recipe:recipe@ds053370.mongolab.com:53370/recipemaker')
conn =pymongo.MongoClient()
db = conn.recipemaker
coll = db.tweets
cGood = db.goodURLs
cBad = db.badURLs
cError = db.errorURLs
print "connected to db"
import urllib2
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize
from collections import defaultdict
from urlparse import urlparse

q="recipe"
for tweet in tweepy.Cursor(api.search,q=q,
                      # since="2015-04-08",
                       #until="2015-04-15",
                       lang="en").items(100000):
     for url in tweet.entities['urls']:
            try:
                u = urlparse(urllib2.urlopen(url['expanded_url']).url)
                netloc = u.netloc
                print "Begin:" + netloc
                content = urllib2.urlopen(url['expanded_url']).read()
                soup = BeautifulSoup(content)
                for script in soup(["script", "style"]):
                    script.extract()    # rip it out
                text = soup.get_text()
                rawtokens = word_tokenize(text)
                start = False
                end = False
                for x in rawtokens:
                    if start == True and end == False:
                        tokens.add(x)
                        #print x
                    if start == True and (x.lower() == "directions" or x.lower()=="prepartions" or x.lower()=="instructions"):
                        end = True
                    #If ingredient list is twice use 2nd list only. Most sites have a summary at the end.    
                    if x.lower() == "ingredients" and end == False:
                        start = True
                        tokens = set()
                if end == True:
                     cGood.insert({'url':netloc})  
                else:
                    cBad.insert({'url':netloc} )
            except:
                print "exception" + url['expanded_url']
                cError.insert({'url':url['expanded_url']})
