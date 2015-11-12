#gives cosine similarity score for text from two HTML pages
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk import stem
import urllib2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
    
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

def get_text(url) :
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html.decode('utf-8','ignore'))
	texts = soup.findAll(text=True)
	visible_texts = filter(visible, texts)
	AllText = " ".join(visible_texts)
	return AllText

urls=["https://fedoraproject.org/wiki/Elections" ,
"https://fedoraproject.org/wiki/Env_and_Stacks"]

documents=[]
for url in urls :
	documents.append(str(get_text(url)))
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print(str(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])))

"""
words=text.split(" ")
words = [w.strip("./\()\n\t,\"\'").lower() for w in words]
filtered_words = [w for w in words if not w in ["\n"," ",""] and not w.isnumeric() ]
final_words = [w for w in filtered_words if not w in stopwords.words('english')]

stemmer=stem.PorterStemmer()
documents = [stemmer.stem(words) for words in final_words]
print(documents)

print(str(final_words))
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform()
"""

