import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv(r"https://raw.githubusercontent.com/amankharwal/Website-data/master/bbc-news-data.csv",sep='\t')
k = pd.set_option('display.max_columns', None)
l = pd.set_option('display.max_rows', None)
# print(df.head())
# print(df.shape)
# print(df.info())
#print(df.isnull().sum())
#print(df["category"].value_counts())
df1 = df[["title", "category"]]

x = np.array(df1["title"])
y = np.array(df1["category"])

cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = MultinomialNB()
model.fit(X_train,y_train)

user = input("Enter a Text: ")
data = cv.transform([user]).toarray()
output = model.predict(data)
print(output)