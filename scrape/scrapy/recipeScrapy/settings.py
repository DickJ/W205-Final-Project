# -*- coding: utf-8 -*-
BOT_NAME = 'recipeScrapy'
ITEM_PIPELINES = {'recipeScrapy.pipelines.ExtractIngredientsPipeline': 300,
                  'recipeScrapy.pipelines.MongoWriterPipeline': 400,
                  }
LOG_LEVEL = "INFO"
MONGODB_SERVER = 'ds029142-a0.mongolab.com'
MONGODB_PORT = 29142
MONGODB_USER = 'scraper'
MONGODB_PW = 'scraper'
MONGODB_DB = 'scraper'
MONGODB_DROPPED_DB = 'droppedURLs1'
MONGODB_COLLECTION = 'recipeURLs1'
NEWSPIDER_MODULE = 'recipeScrapy.spiders'
ROBOTSTXT_OBEY = True
SPIDER_MODULES = ['recipeScrapy.spiders']
USER_AGENT = 'recipeScrapy'