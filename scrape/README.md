#List of Folders
##HomebrewScrapers
HomebrewScrapers contains scrapers that were developed to fill gaps left by 
Scrapy. 
##InitialScraperOfAllrecipes
InitialScraperOfAllrecipes contains code pertaining to our first scrape, that
 of allrecipes.com. This scraped data was used to develop our initial 
 ingredients list.
##scrapy
scrapy contains all files associated with our scrapy project RecipeScrapy

#List of Files
*   pymongo_pipe.py contains code for exporting our scraped data from a MongoDB 
to an output file usable by the indexer.
*   scraped_data_export.sh contains a single call to mongoexport for 
exporting our scraped data from a mongoDB to an output file usable by the 
indexer
  
 