import pandas as pd
#import nltk as ntk
from sklearn.linear_model import LogisticRegression
#from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.externals import joblib

df=pd.read_csv("Emotion-final.csv")
Xfeatures=df['Text']
ylabels=df['Emotion']
x_train,x_test,y_train,y_test=train_test_split(Xfeatures,ylabels,test_size=0.2,random_state=42)
from sklearn.pipeline import Pipeline
pipe=Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression())])
pipe.fit(x_train,y_train)
#print(pipe.score(x_test,y_test))
joblib.dump(pipe,'pipe.pkl')