import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
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

#BarPLot for the Total Category
ax=df["category"].value_counts().sort_values().plot(kind ='barh')
ax.bar_label(ax.containers[0])
plt.title("Count of Different News Articles")
#plt.show()

cv = CountVectorizer()
X = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model =MultinomialNB()
model.fit(X_train,y_train)



user = input("Enter a Text: ")
data = cv.transform([user]).toarray()
output = model.predict(data)

print(output[0])
