mongoexport --host ds029142-a0.mongolab.com --port 29142 --username scraper --password scraper --db scraper --collection recipeURLs --query "{is_indexed: false}" --fields _id,url,title,ingred --out a.json
