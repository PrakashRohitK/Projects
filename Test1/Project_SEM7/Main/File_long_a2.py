import copy
import numpy as np
import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import VarianceThreshold
from imblearn.over_sampling import SMOTE
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
#from sklearn.metrics import accuracy_score
#from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv(r"C:\Users\user\PycharmProjects\Test1\Project_SEM7\news-article-categories.csv")
k = pd.set_option('display.max_columns', None)
l = pd.set_option('display.max_rows', None)

# print(df.head())
# print(df.shape)
#print(df.info())
#print(df.isnull().sum())
#print(df["category"].value_counts())
df = df[df.category !="ARTS & CULTURE"]
df1 = df[["title", "category"]]
#print(df1)
x = np.array(df1["title"])
y = np.array(df1["category"])

#BarPLot for the Total Cat
ax=df["category"].value_counts().sort_values().plot(kind ='barh')
ax.bar_label(ax.containers[0])
plt.title("Count of Different News Articles")
#plt.show()

cv = CountVectorizer()
X = cv.fit_transform(x)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
title_tr, title_te, category_tr, category_te = train_test_split(x,y)
title_tr, title_de, category_tr, category_de = train_test_split(title_tr,category_tr)
#print("Training: ",len(title_tr))
#print("Developement: ",len(title_de),)
#print("Testing: ",len(title_te))

print("\nVectorizing data")
tokenizer = nltk.tokenize.RegexpTokenizer(r"\w+")
stop_words = nltk.corpus.stopwords.words("english")
vectorizer = CountVectorizer(tokenizer=tokenizer.tokenize, stop_words=stop_words)

vectorizer.fit(iter(title_tr))
Xtr = vectorizer.transform(iter(title_tr))
Xde = vectorizer.transform(iter(title_de))
Xte = vectorizer.transform(iter(title_te))

encoder = LabelEncoder()
encoder.fit(category_tr)
Ytr = encoder.transform(category_tr)
Yde = encoder.transform(category_de)
Yte = encoder.transform(category_te)

print("\nApplyting Feature Reduction")
print("Number of features before reduction : ", Xtr.shape[1])
selection = VarianceThreshold(threshold=0.001)
Xtr_whole = copy.deepcopy(Xtr)
Ytr_whole = copy.deepcopy(Ytr)
selection.fit(Xtr)
Xtr = selection.transform(Xtr)
Xde = selection.transform(Xde)
Xte = selection.transform(Xte)
print("Number of features after reduction : ", Xtr.shape[1])

## Sampling data
sm = SMOTE(random_state=42)
Xtr, Ytr = sm.fit_resample(Xtr, Ytr)

# # Train Models
# ### Baseline Model
# “stratified”: generates predictions by respecting the training set’s class distribution.
print("\n\nTraining baseline classifier")
dc = DummyClassifier(strategy="stratified")
dc.fit(Xtr, Ytr)
pred = dc.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

# ### Decision Tree
print("Training Decision tree")
dt = DecisionTreeClassifier()
dt.fit(Xtr, Ytr)
pred = dt.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

# ### Random Forest
print("Training Random Forest")
rf = RandomForestClassifier(n_estimators=40)
rf.fit(Xtr, Ytr)
pred = rf.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

# ### Multinomial Naive Bayesian
print("Training Multinomial Naive Bayesian")
nb = MultinomialNB()
nb.fit(Xtr, Ytr)
pred_nb = nb.predict(Xde)
print(classification_report(Yde, pred_nb, target_names=encoder.classes_))

# ### Support Vector Classification
print("Training Support Vector Classification")
from sklearn.svm import SVC
svc = SVC()
svc.fit(Xtr, Ytr)
pred = svc.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

# ### Multilayered Perceptron
print("Training Multilayered Perceptron")
mlp = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(100, 20), random_state=1, max_iter=400)
mlp.fit(Xtr, Ytr)
pred = mlp.predict(Xde)
print(classification_report(Yde, pred, target_names=encoder.classes_))

user = input("Enter a Text: ")
data = cv.transform([user]).toarray()
output = mlp.predict(data)

print(output[0])


# # Final Model: Multinomial Naive Bayesian
# **Multinomial Naive Bayesian** works the best. Lets run NB on our test data and get the confusion matrix and its heat map.
# ## Predict test data
print("\n\nPredicting test data using Multinomial Naive Bayesian")
pred_final = nb.predict(Xte)
print(classification_report(Yte, pred_final, target_names=encoder.classes_))


# get incorrectly classified data
print("\n\nIncorrectly classified")
incorrect = np.not_equal(pred_nb, Yde).nonzero()[0]
print(
    "\nTitle: ",x[incorrect[6]],
    "\nTrue Category: ",y[incorrect[6]],
    "\nPredicted Category: ", encoder.inverse_transform([pred[incorrect[6]]])[0]
)