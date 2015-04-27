# This code probably should not exist. It should be replaced with a single
# mongoexport call. i.e.:
# $ mongoexport --host ds059651.mongolab.com --port 59651 --username fuggedaboutit
#   --password dontryit --db scraper --collection recipeURLs
#   --query {is_indexed : false} --csv
#   --fields _id,url,title,ingred,is_indexed --out ./output_location/file.csv



import pymongo

conn = pymongo.MongoClient('ds029142-a0.mongolab.com', 29142)
db = conn.scraper
db.authenticate('scraper', 'scraper')
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