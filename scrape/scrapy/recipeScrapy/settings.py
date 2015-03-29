# -*- coding: utf-8 -*-

# Scrapy settings for recipeScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'recipeScrapy'

LOG_LEVEL = "INFO"
SPIDER_MODULES = ['recipeScrapy.spiders']
NEWSPIDER_MODULE = 'recipeScrapy.spiders'
ROBOTSTXT_OBEY = True
DOMAIN_DEPTHS = {'bettycrocker.com' : 7}

MONGODB_SERVER = 'ds053370.mongolab.com'
MONGODB_PORT = 53370
MONGODB_USER = 'recipe'
MONGODB_PW = 'recipe'
MONGODB_DB = 'recipemaker'
MONGODB_COLLECTION = 'recipURLs'

ITEM_PIPELINES = {'recipeScrapy.pipelines.ExtractIngredientsPipeline': 300,
                  'recipeScrapy.pipelines.MongoWriterPipeline': 400}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'recipeScrapy'
