import urllib2
import lxml
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import json
from httplib import BadStatusLine
import hashlib
from BeautifulSoup import BeautifulSoup


def extract_html(url):
    try:
        response = urllib2.urlopen(url)
    except BadStatusLine:
        return ''
    html = response.read()
    response.close()
    return html

tag_list = [{'tag':'span','attr':'itemprop','attr_val':'ingredient'},
            {'tag':'span','attr':'itemprop','attr_val':'ingredients'},
            {'tag':'li','attr':'itemprop','attr_val':'ingredients'},
            {'tag':'li','attr':'id','attr_val':'liIngredient'},
            {'tag':'span','attr':'class','attr_val':'ingredient'},
            {'tag':'span','attr':'itemprop','attr_val':'ingredient'},
            {'tag':'dl','attr':'class','attr_val':'recipePartIngredient'},
            {'tag':'div','attr':'class','attr_val':'fr-ingredients'},
            {'tag':'div','attr':'class','attr_val':'inside'}]

def soup_html(soup):
    ing = []
    for tag in tag_list:
        result = soup.findAll(tag['tag'],{tag['attr']:tag['attr_val']})
        if len(result) > 0:
            for line in result:
                ing.append(line.text)
            return ing
    return ing

def extract_contents(html):
    soup = BeautifulSoup(html)
    title = soup.html.head.title.text
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

def clean_contents(texts):
    sws = stopwords.words('english')
    words_pattern = r"[a-zA-Z][a-zA-Z]*"
    words = re.findall(words_pattern, texts)
    st = PorterStemmer()
    words = [st.stem(word) for word in words if not word in sws and word in ing_dic]
    return ' '.join(words)
    
def clean_title(title):
    title_c = title.strip().lower()
    title_c = re.sub(r'.com', '',title_c)
    return title_c

ing_dic = {}
with open('full-ingred-word-list.txt') as f:
    lines = f.read()
    for ing in lines.split('\r'):
        ing_dic[ing] = 1


    
if __name__ == "__main__":
    f = open('sample_recipes.txt')
    docs = []
    for line in f.readlines():
        url = line.strip()
        print url
        path = 'data/'
        html = extract_html(url)
        if html != '':
            title, texts = extract_contents(html)
            title_c = clean_title(title)
            contents = clean_contents(texts)
            print title_c
            print contents
            docid = int(hashlib.sha1(url).hexdigest(), 16) % (10 ** 8)
            doc = {'doc_id':docid,'url':url,'title':title_c,'contents':contents}
            docs.append(doc)
            #f=open('data/{}.dat'.format(docid),'w')
            #f.write(json.dumps(doc))
            #f.close()

