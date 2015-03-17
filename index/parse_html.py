import urllib2
import lxml
import re
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import json
from httplib import BadStatusLine


def extract_html(url):
    try:
        response = urllib2.urlopen(url)
    except BadStatusLine:
        return ''
    html = response.read()
    response.close()
    return html

def extract_title(url):
    t = lxml.html.parse(url)
    return t.find(".//title").text.strip()    

def extract_contents(url,html):
    # remove javascript code
    js = r"(?is)<script[^>]*>(.*?)</script>"
    br = r"<br */? *>[ \r\n]*<br */? *>"
    href = r"(?is)<a href[^>]*>(.*?)</a>"
    style = r"(?is)<style[^>]*>(.*?)</style>"
    #li = r"(?is)<li[^>]*>(.*?)</li>"
    ws = r"[\s\n\r\t]+"
    tag = r"<[^>]*?>"
    title = extract_title(url)
    text = re.sub(js,' ',html) # remove javascript code
    text = re.sub(href, ' ',text) # remove urls
    text = re.sub(style,' ',text) # remove style tags
    text = re.sub(br,' ',text) # remove br tags
    #text = re.sub(li,' ',text) # remove li tags
    text = re.sub(tag,' ',text) # remove all tags
    text = re.sub(ws, ' ',text) # remove white space
    return (title,text)               

def clean_contents(texts):
    sws = stopwords.words('english')
    words_pattern = r"[a-zA-Z][a-zA-Z]*"
    words = re.findall(words_pattern, texts)
    st = LancasterStemmer()
    words = [st.stem(word) for word in words if not word in sws and word in ing_dic]
    return ' '.join(words)
    
def clean_title(title):
    title_c = title.lower()
    title_c = re.sub(r'.com', '',title_c)
    return title_c

ing_dic = {}
with open('full-ingred-word-list.txt') as f:
    lines = f.read()
    for ing in lines.split('\r'):
        ing_dic[ing] = 1


    
if __name__ == "__main__":
    f = open('sample_recipes.txt')
    docid = 0
    
    for line in f.readlines():
        url = line.strip()        
        path = 'data/'
        html = extract_html(url)
        if html != '':
            title, texts = extract_contents(url, html)
            title_c = clean_title(title)
            contents = clean_contents(texts)
            doc = {'doc_id':docid,'url':url,'title':title_c,'contents':contents}
            f=open('data/{}.dat'.format(docid),'w')
            f.write(json.dumps(doc))
            f.close()
            docid += 1
