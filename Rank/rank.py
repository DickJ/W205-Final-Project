import pymongo
from pymongo import MongoClient
from collections import defaultdict

#conn=pymongo.MongoClient('mongodb://recipe:recipe@ds053370.mongolab.com:53370/recipemaker')
conn =pymongo.MongoClient()
db = conn.recipemaker
coll = db.ingIndex

# Get all the ingredients
ingredients= coll.find()
recipes = defaultdict(list)
recipeIngreds = defaultdict(list)
#For each recipe put in the number of times other recipes use that same ingredient
for i in ingredients:
    ingred_count = len(i['postinglist'])
    for p in set(i['postinglist']):
        recipes[p].append(ingred_count)
        recipeIngreds[p].append(i['ingredient'])

#Get original recipe information
coll = db.recipeURLs
URL = defaultdict()
title = defaultdict()
rawIngred = defaultdict()
origColl = coll.find()
#For each recipe put in the number of times other recipes use that same ingredient
for c in origColl:
    strID = str(c['_id'])
    rawIngred[strID] = c['ingred']
    URL[strID] = c['url']
    title[strID] = c['title']

# Create new Rank collection every time
db.recipe_rank.drop()
coll = db.recipe_rank

#replace ingredient count with a rank

for r in recipes:
    countI=0
    multI = 1
    for c in recipes.get(r):
            multI = multI * int(c)
            countI = countI+1
    rankvalue = int(multI ** (1/float(countI)))
    #rank[r] = rankvalue
    doc = {"recipe":r, "rank":rankvalue,"URL":URL[r],"title":title[r],"rawIngred":rawIngred[r],"ingred":recipeIngreds[r]}
    coll.insert(doc)
