# -*- coding: utf-8 -*-

# Scrapy settings for findDomains project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'recipeScrapy'

SPIDER_MODULES = ['recipeScrapy.spiders']
NEWSPIDER_MODULE = 'recipeScrapy.spiders'
ROBOTSTXT_OBEY = True
DOMAIN_DEPTHS = {'bettycrocker.com' : 7}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'findDomains (+http://www.yourdomain.com)'
