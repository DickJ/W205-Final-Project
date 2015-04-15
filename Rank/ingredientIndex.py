import pymongo
from pymongo import MongoClient
from collections import defaultdict
#conn=pymongo.MongoClient('mongodb://recipe:recipe@ds053370.mongolab.com:53370/recipemaker')
conn =pymongo.MongoClient()
db = conn.recipemaker
cIngredient = db.ingredients
cIndex = db.ingIndex
cRecipe = db.recipeURLs

#Get list of known good ingredients
ingredients= cIngredient.find()

#For each recipe put in the number of times other recipes use that same ingredient
# space in regex is to get whole word matches, not parts of words: ale vs. kale.
for i in ingredients:
    matched = cRecipe.find({'ingred': {'$regex': ' '+i['ingredient']}})
    recipes = list()
    for m in matched:
        recipes.append(str(m['_id']))
    doc = {"ingredient":i['ingredient'], "postinglist":recipes}
    cIndex.insert(doc)
      



