### THIS SCRIPT IS USED TO TRAIN THE ML MODEL AND SAVE IT ###
#### SCRIPT TO CREATE A MODEL FOR DETERMINING MODE OF CONTACT ###
import json as j
import pandas as pd
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
import pickle
import os
# from . import views
import json
json_file_path = "upi_no_upi_otp.json"
with open(os.path.abspath(json_file_path), 'r') as j:
     contents = json.loads(j.read())


data = pd.DataFrame(contents)

    # stemmer = SnowballStemmer('english')
    # words = stopwords.words("english")

X_train, X_test, y_train, y_test = train_test_split(data['post'], data.intent, test_size=0.2)

pipeline = Pipeline([('vect', TfidfVectorizer(ngram_range=(1, 2), stop_words="english", sublinear_tf=True)),
                     ('chi',  SelectKBest(chi2, k='all')),
                     ('clf', LinearSVC(C=1.0, penalty='l1', max_iter=3000, dual=False))])

model = pipeline.fit(X_train, y_train)
vectorizer = model.named_steps['vect']
chi = model.named_steps['chi']
clf = model.named_steps['clf']

feature_names = vectorizer.get_feature_names()
feature_names = [feature_names[i] for i in chi.get_support(indices=True)]
feature_names = np.asarray(feature_names)

# save the model to disk
filename = 'upi_no_upi_otp.sav'
pickle.dump(model, open(filename, 'wb'))





# views.index_page(request)
