import joblib
import nltk
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import _logistic
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.linear_model import SGDRegressor 

model_SGDRegressor=SGDRegressor()

def transfer(text):
    stop_words=set(stopwords.words('english'))
    text=text.lower()
    word_tokens=word_tokenize(text)
    filtered_sentence=[w for w in word_tokens if w not in stop_words]
    
    stem_words=[]
    ps=PorterStemmer()
    for w in filtered_sentence:
        rootWord=ps.stem(w)
        stem_words.append(rootWord)

    lemma_word=[]
    wordnet_lemmatizer=WordNetLemmatizer()
    for w in stem_words:
        word1=wordnet_lemmatizer.lemmatize(w,pos="n")
        word2=wordnet_lemmatizer.lemmatize(word1,pos="v")
        word3=wordnet_lemmatizer.lemmatize(word2,pos="a")
        word4=wordnet_lemmatizer.lemmatize(word3,pos="r")
        word5=wordnet_lemmatizer.lemmatize(word4,pos="s")
        lemma_word.append(word5)
    
    result=""
    for w in lemma_word:
        result=result+w+" "
    pipe=joblib.load('model.pkl')
    res=''
    return res.join(pipe.predict([result]))
    
if __name__ == '__main__':
    ans=transfer("There are seven apples. The biggest one is the left most one.")
    print(ans)