#!/usr/bin/env python2
import sys
import argparse
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
import urllib2
import nltk
from bs4 import BeautifulSoup
from nltk import word_tokenize
from collections import defaultdict
from urlparse import urlparse

def getGoodIngredients():
    print "goodingredients"
    cIngred = db.goodIngredients
    print "query db"
    goodIngred = set()
    ingred = cIngred.find()
    for ing in ingred:
        for i in ing['ingred']:
            goodIngred.add(stemmer.stem(i))
    return goodIngred

def isNewURL(url,recipeURLs):
    returnVal = False
    #excldue blanks and comments
    if url != "" and "#" not in url:
        newset = set()
        newset.add(url)    
        if newset.issubset(recipeURLs) == False:
            recipeURLs.add(url)
            returnVal = True
            #print "new=" + url
    #else:
        #print "old=" + url
    return returnVal
        
def getsoup(url):
    soup = ""
    try:
        if url[0:4]=="http":
            content = urllib2.urlopen(url).read()
        else:
            content = urllib2.urlopen("http://"+url).read()
        soup = BeautifulSoup(content)
        for script in soup(["script", "style"]):
                    script.extract()    # rip it out
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        cError.insert({'url':url})
    return soup

def getURLs(soup,site,recipeURLs):
    links = set()
    for anchor in soup.findAll('a', href=True):
        url = ""
	if len(anchor['href'])>1:
		if anchor['href'][0] == "/":
		    url = site+anchor['href']
		    
		else:
		    parsedURL = urlparse(anchor['href'])
		    netloc = parsedURL.netloc
		    #only add links from home site.
		    #otherwise would search entire web.
		    if netloc == site:
		        url = anchor['href']
		if isNewURL(url,recipeURLs):
		    links.add(url)
    #print links
    return links

def getTokens(soup):
    text = soup.get_text()
    rawtokens = word_tokenize(text)
    start = False
    end = False
    tokens = set()
    #print u
    for t in rawtokens:
        if start == True and end == False:
            tokens.add(stemmer.stem(t))
            #print x
        #end at directions, or similar words
        if start == True and (t.lower() == "directions" or t.lower()=="prepartions" or t.lower()=="instructions"):
            end = True
        #start at ingredients   
        if t.lower() == "ingredients" and start == False:
            start = True
    return tokens


                
def recurseURL(URL,site,recipeURLs): #add lastedit 
    #print URL
    soup = getsoup(URL)
    if soup != "":
        tokens = getTokens(soup)
        if len(tokens) > 0:
             title = soup.title.string
             doc = {"url":URL,"ingred": list(tokens & ingred),"title":title}
             cRecipe.insert(doc)  
             print "good" + URL
        #else:
            #cBad.insert({'url':URL})
            #print "bad" + url
        URLs = getURLs(soup,site,recipeURLs)
        x=0
        for u in URLs:
            recurseURL(u,site,recipeURLs)
            x+=1
        if x>0:
            print str(x) +  "loops"       

def isNewSite(netloc,sites):
    returnVal = False
    #excldue blanks and comments
    print "netloc" + netloc
    if netloc != "":
        newset = set()
        newset.add(netloc)  
        
        if newset.issubset(sites) == False:
            sites.add(netloc)
            returnVal = True
            #print "new=" + url
    #else:
        #print "old=" + url
    return returnVal

if __name__ == "__main__":
    
    #define global variables
    conn =pymongo.MongoClient()
    db = conn.recipemaker
     #conn=pymongo.MongoClient('mongodb://recipe:recipe@ds053370.mongolab.com:53370/recipemaker')
    coll = db.tweets
    cGood = db.good4
    cBad = db.badURL2
    cError =db.errorURL3
    cRecipe = db.recipeURL3
    cSite = db.sites
    cTweets = db.tweetsites
    from nltk.stem import PorterStemmer
    stemmer=PorterStemmer()
    recipeURLs = set()
    #startcode
    ingred = getGoodIngredients()
    #call twitter
    # pretend jennifsikora is first url returned by twitter
    #twitterurl = sys.argv[1]#"http://jennifersikora.com/"
    #call sites
    sites = set()
    sitesinDB = cSite.find()
    for s in sitesinDB:
        sites.add(s['url'])   
    #call existingrecipes
    tweets = cTweets.find()
    for t in tweets:
        twitterurl = t['url']    
        parsedURL = urlparse(twitterurl)
        print twitterurl
        print parsedURL
        netloc = parsedURL.path
        if isNewSite(netloc,sites):
            print twitterurl
            cSite.insert({'url':twitterurl})
            if isNewURL(twitterurl,recipeURLs):
                recurseURL(twitterurl,netloc,recipeURLs)    
    print "done!"

