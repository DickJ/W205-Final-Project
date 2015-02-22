# Files:
###extract_ingredients_allrecipes.py
extract_ingredients_allrecipes.py contains a MRJob class for processing html files from allrecipes.com and extracting their recipe ingredients. This code also eliminates stopwords from the list of potential ingredient words. These stopwords came from nltk.corpus, but are used without the library due to complications that arise when running the job on Amazon EMR. 
###generate_sh.py
Due to the limits of both the linux operating system and my ability to write MR jobs, the corpus of recipes from allrecipes.com had to be partitioned. This script partitions the recipes, generates a shell script to run MR jobs on them, and re-consolidates the recipe output after the MR is complete. This script is optimized to run on my (Rich) computer and will require modification to run elsewhere.
###get-pip.py
This file is a requirement for running on Amazon EMR and is referenced in mrjob.conf
###mrjob.conf
A config file for running on Amazon EMR
###scrape_allrecipes.py
This is the code for scraping every recipe from allrecipes.com
