import pymongo
from pymongo import MongoClient
#conn=pymongo.MongoClient('mongodb://recipe:recipe@ds053370.mongolab.com:53370/recipemaker')
conn =pymongo.MongoClient()
db = conn.recipemaker
cIndex = db.recipe_index
cRecipe = db.recipeURLs
from collections import defaultdict
# Get all the ingredients
totalIngred = 0
ingredients= cIndex.find()
listIngredCount = defaultdict(list)
ingreds = defaultdict(list)
ingredCount= defaultdict()
#For each recipe put in the number of times other recipes use that same ingredient
for i in ingredients:
    #The number of recipes that use the ingredient.
    ingredCount[i['ingredient']] = (len(i['postinglist']))
    totalIngred += int(ingredCount[i['ingredient']])
    for p in set(i['postinglist']):
        listIngredCount[p].append(ingredCount[i['ingredient']])
        ingreds[p].append(i['ingredient'])

import math
x=0
totalIDF =defaultdict()
recipeMean = defaultdict()
for r in listIngredCount:
    product = 1
    totalIDF[r] = float(0)   
    IDF = defaultdict()
    for c in listIngredCount.get(r):
            product = product * (int(c)** (1/float(len(ingreds[r]))))
            IDFCalc = 1/float(len(ingreds[r]))*math.log(totalIngred/(1+int(c)))
            totalIDF[r] += IDFCalc
    #geometric mean    
    recipeMean[r] = int(product)

cRank =db.rank3
ingredients= cIndex.find()
minIDF = -1
maxIDF = 0
minMean = -1
maxMean = 0
minLength =-1
maxLength =0
minIngred = -1
maxIngred = 0
ingIDF = 0
for i in ingredients:
    recipeRank = defaultdict(list)
    for p in set(i['postinglist']):
        recipeRank[p].append(totalIDF[p])
        recipeRank[p].append(recipeMean[p])
	recipeRank[p].append(len(ingreds[p]))
	if totalIDF[p] > maxIDF:
		maxIDF=totalIDF[p]
	if totalIDF[p] < minIDF or minIDF==-1:
		minIDF=totalIDF[p]
	if recipeMean[p]> maxMean:
		maxMean=recipeMean[p]
	if recipeMean[p] < minMean or minMean==-1:
		minMean=recipeMean[p]
	if len(ingreds[p])> maxLength:
		maxLength=len(ingreds[p])
	if len(ingreds[p]) < minLength or minLength==-1:
		minLength=len(ingreds[p])	
    ingIDF = math.log(totalIngred/(1+int(len(set(i['postinglist']))))) 
    doc = {"ingredient":i['ingredient'],"ingredIDF":ingIDF,"postinglistIDFRankCount":recipeRank}
    if ingIDF > maxIngred:
		maxIngred=ingIDF
    if ingIDF < minIDF or minIngred==-1:
		minIngred=ingIDF
    try:
	cRank.insert(doc)   
    except:
        print "ingredient" + i['ingredient']
	print recipeMean[p]
#write min/max values into database to speed up query.
cMaxMin =db.MaxMin
doc = {'maxIDF':maxIDF,'minIDF':minIDF,'maxLength':maxLength,'minLength':minLength, 'maxIngred':maxIngred,'minIngred':minIngred,'maxMean':maxMean,'minMean':minMean}
cMaxMin.insert(doc)

