# -*- coding: utf-8 -*-

# Scrapy settings for recipeScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'recipeScrapy'
ITEM_PIPELINES = {'recipeScrapy.pipelines.ExtractIngredientsPipeline': 300,
                  'recipeScrapy.pipelines.MongoWriterPipeline': 400,
                  }
LOG_LEVEL = "INFO"
MONGODB_SERVER = 'ds059651.mongolab.com'
MONGODB_PORT = 59651
MONGODB_USER = 'scraper'
MONGODB_PW = 'scraper'
MONGODB_DB = 'scraper'
MONGODB_DROPPED_DB = 'droppedURLs'
MONGODB_COLLECTION = 'recipeURLs'
NEWSPIDER_MODULE = 'recipeScrapy.spiders'
#ROBOTSTXT_OBEY = True
SPIDER_MODULES = ['recipeScrapy.spiders']
USER_AGENT = 'recipeScrapy'
