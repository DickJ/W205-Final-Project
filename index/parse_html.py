import mrjob
from mrjob.job import MRJob
from mrjob.step import MRStep
import urllib2
import re
import nltk
from nltk.stem.porter import PorterStemmer
from httplib import BadStatusLine, IncompleteRead
import hashlib
from BeautifulSoup import BeautifulSoup
import boto
from boto.s3.key import Key

tag_list = [{'tag':'span','attr':'itemprop','attr_val':'ingredient'},
            {'tag':'span','attr':'itemprop','attr_val':'ingredients'},
            {'tag':'li','attr':'itemprop','attr_val':'ingredients'},
            {'tag':'li','attr':'id','attr_val':'liIngredient'},
            {'tag':'span','attr':'class','attr_val':'ingredient'},
            {'tag':'span','attr':'itemprop','attr_val':'ingredient'},
            {'tag':'dl','attr':'class','attr_val':'recipePartIngredient'},
            {'tag':'div','attr':'class','attr_val':'fr-ingredients'},
            {'tag':'div','attr':'class','attr_val':'inside'}]

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

ing_dic = {}
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bk = conn.get_bucket('recipes-utils')
k = Key(bk)
k.key = 'full-ingred-word-list.txt'
lines = k.get_contents_as_string()

for ing in lines.split():
    ing_dic[ing] = 1

def clean_title(title):
    title_c = title.strip().lower()
    title_c = re.sub(r'.com', '',title_c)
    return title_c

def clean_contents(texts):
    #sws = stopwords.words('english')
    words_pattern = r"[a-zA-Z][a-zA-Z]*"
    words = re.findall(words_pattern, texts)
    st = PorterStemmer()
    words = [st.stem(word) for word in words if word in ing_dic]
    return ' '.join(words)

def extract_contents(url,html):
    soup = BeautifulSoup(html)
    try:
        title = soup.html.head.title.text
    except AttributeError:
        #print "attribute error - cannot find header:{}".format(url)
        title = ''
    texts = soup_html(soup)
    if len(texts) > 0:
        return title, ' '.join(texts)
    # if raw recipes can not be found using tag list, scrape html
    else:
        # remove javascript code
        js = r"(?is)<script[^>]*>(.*?)</script>"
        br = r"<br */? *>[ \r\n]*<br */? *>"
        href = r"(?is)<a href[^>]*>(.*?)</a>"
        style = r"(?is)<style[^>]*>(.*?)</style>"
        #li = r"(?is)<li[^>]*>(.*?)</li>"
        ws = r"[\s\n\r\t]+"
        tag = r"<[^>]*?>"        
        text = re.sub(js,' ',html) # remove javascript code
        text = re.sub(href, ' ',text) # remove urls
        text = re.sub(style,' ',text) # remove style tags
        text = re.sub(br,' ',text) # remove br tags
        text = re.sub(tag,' ',text) # remove all tags
        text = re.sub(ws, ' ',text) # remove white space
        return title,text

def soup_html(soup):
    ing = []
    for tag in tag_list:
        result = soup.findAll(tag['tag'],{tag['attr']:tag['attr_val']})
        if len(result) > 0:
            for line in result:
                ing.append(line.text)
            return ing
    return ing

def extract_html(url):
    try:
        response = urllib2.urlopen(url)
    except BadStatusLine:
        return ''
    except ValueError as e:
        #print "url value error: {}".format(e)
        return ''
    except urllib2.HTTPError, e:
        #print "HTTPError: {}".format(e)
        return ''
    try:
        html = response.read()
    except IncompleteRead:
        return ''
    response.close()
    return html

class RunParseRawFile(MRJob):
    
    def configure_options(self):
        super(RunParseRawFile, self).configure_options()
        self.add_passthrough_option('--source',\
                                    help="Source location of recipe data (s3 or local)")
    #WIP                                
    #def jobconf(self):
    #    orig_jobconf = super(RunParseRawFile, self).jobconf()
    #    custom_jobconf = {'stream.num.map.output.key.fields' : 2,\
    #                      'mapred.text.key.partitioner.options':'k1,1'}
    #    return mrjob.conf.combine_dicts(orig_jobconf, custom_jobconf)
    
    #def partitioner(self):
    #    self.SORT_VALUE = True

    def mapper(self, _,line):
        url = line.strip()
        if url.startswith('http'):
        # url
            html = extract_html(url)
            if html != '':
                title, texts = extract_contents(url,html)
                title_c = clean_title(title)
                contents = clean_contents(texts)
                docid = int(hashlib.sha1(url).hexdigest(), 16) % (10 ** 8)
                doc = {'title':title_c,'contents':contents, 'url':url}
                yield docid, doc
                       
if __name__ == '__main__':
    RunParseRawFile.run()
