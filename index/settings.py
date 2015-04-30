import os


AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

host = 'ds059651.mongolab.com'
port = '59651'
db = 'scraper'
MONGODB_USER = 'scraper'
MONGODB_PW = 'scraper'
MONGODB_URI = 'mongodb://{usr}:{pw}@{host}:{port}/{dbname}'.format(host=host,
                                                                port=port,
                                                                dbname=db,
                                                                usr=MONGODB_USER,
                                                                pw=MONGODB_PW)
index_db = 'recipe_index'
