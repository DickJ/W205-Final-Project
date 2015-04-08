import os


AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

host = 'ds053370.mongolab.com'
port = '53370'
db = 'recipemaker'
MONGODB_USER = 'recipe'
MONGODB_PW = 'recipe'
MONGODB_URI = 'mongodb://{usr}:{pw}@{host}:{port}/{dbname}'.format(host=host,
                                                                port=port,
                                                                dbname=db,
                                                                usr=MONGODB_USER,
                                                                pw=MONGODB_PW)
index_db = 'recipe_index'
