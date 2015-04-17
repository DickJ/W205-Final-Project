import pymongo

conn = pymongo.MongoClient('ds053370.mongolab.com', 53370)
db = conn.recipemaker
db.authenticate('recipe', 'recipe')
c = db.recipeURLs


with open('d.out', 'w') as fp:
     for a in c.find({'is_indexed' : False}, {'url':1, 'title':1, 'ingred':1, '_id':1}):
         a['_id'] = str(a['_id'])
         fp.write(str(a))
         fp.write("\n")
'''
i = 0
for a in c.find({}):


import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
'''