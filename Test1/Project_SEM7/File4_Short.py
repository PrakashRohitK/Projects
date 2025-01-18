import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('omw-1.4')
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('punkt_tab')
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import make_scorer, roc_curve, roc_auc_score
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

df = pd.read_csv(r"C:\Users\kpbrb\PycharmProjects\Test1\Project_SEM7\BBC News Train.csv")
k = pd.set_option('display.max_columns', None)
l = pd.set_option('display.max_rows', None)
# print(df.head())
# print(df.shape)
# print(df.info())

# print(df['category'].value_counts())
target_category = df['Category'].unique()
#print(target_category)
df['CategoryId'] = df['Category'].factorize()[0]
#df.head()
df1 = df[['Category', 'CategoryId']].drop_duplicates().sort_values('CategoryId')
#print(df1)
# Bar Chat
df.groupby('Category').CategoryId.value_counts().plot(kind = "bar", color = ["pink", "orange", "red", "yellow", "blue"])
plt.xlabel("Category of data")
plt.title("Visualize numbers of Category of data")
plt.show()
# Pie Chart
fig = plt.figure(figsize = (5,5))
colors = ["skyblue"]
business = df[df['CategoryId'] == 0 ]
tech = df[df['CategoryId'] == 1 ]
politics = df[df['CategoryId'] == 2]
sport = df[df['CategoryId'] == 3]
entertainment = df[df['CategoryId'] == 4]
count = [business['CategoryId'].count(), tech['CategoryId'].count(), politics['CategoryId'].count(), sport['CategoryId'].count(), entertainment['CategoryId'].count()]
pie = plt.pie(count, labels = ['business', 'tech', 'politics', 'sport', 'entertainment'],
              autopct = "%1.1f%%",
              shadow = True,
              colors = colors,
              startangle = 45,
              explode = (0.05, 0.05, 0.05, 0.05,0.05))
plt.show()
#Word Clouds
from wordcloud import WordCloud
stop = set(stopwords.words('english'))
business = df[df['CategoryId'] == 0]
business = business['Text']
tech = df[df['CategoryId'] == 1]
tech = tech['Text']
politics = df[df['CategoryId'] == 2]
politics = politics['Text']
sport = df[df['CategoryId'] == 3]
sport = sport['Text']
entertainment = df[df['CategoryId'] == 4]
entertainment = entertainment['Text']
def wordcloud_draw(df, color = 'white'):
    w=''.join(df)
    cleaned_word = ' '.join([w1 for w1 in w.split() if (w1 != 'news' and w1 != 'text')])
    wordcloud = WordCloud(stopwords = stop,background_color =color,width = 2500, height = 2500).generate(cleaned_word)
    plt.figure(1, figsize = (10,7))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

print("business related words:")
wordcloud_draw(business, 'white')
print("tech related words:")
wordcloud_draw(tech, 'white')
print("politics related words:")
wordcloud_draw(politics, 'white')
print("sport related words:")
wordcloud_draw(sport, 'white')
print("entertainment related words:")
wordcloud_draw(entertainment, 'white')
text = df["Text"]
#print(text.head(10))
category = df['Category']
#print(category.head(10))
def special_char(text):
    reviews = ''
    for x in text:
        if x.isalnum():
            reviews = reviews + x
        else:
            reviews = reviews + ' '
    return reviews


df['Text'] = df['Text'].apply(special_char)


def convert_lower(text):
    return text.lower()


df['Text'] = df['Text'].apply(convert_lower)


# print(df['body'][0])

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return [x for x in words if x not in stop_words]


df['Text'] = df['Text'].apply(remove_stopwords)


# print(df['body'][1])

def lemmatize_word(text):
    wordnet = WordNetLemmatizer()
    return " ".join([wordnet.lemmatize(word) for word in text])


df['Text'] = df['Text'].apply(lemmatize_word)
# print(df['Text'][1])
# print(df)
x = df['Text']
y = df['CategoryId']
x = np.array(df.iloc[:, 0].values)
y = np.array(df.CategoryId.values)
cv = CountVectorizer(max_features=5000)
x = cv.fit_transform(df.Text).toarray()
#print("X.shape = ", x.shape)
#print("y.shape = ", y.shape)
# Train Test and Split the df
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, shuffle=True)
# print(len(x_train))
# print(len(x_test))

perform_list = []


def run_model(model_name, est_c, est_pnlty):
    mdl = ''
    if model_name == 'Logistic Regression':
        mdl = LogisticRegression()
    elif model_name == 'Random Forest':
        mdl = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
    elif model_name == 'Multinomial Naive Bayes':
        mdl = MultinomialNB(alpha=1.0, fit_prior=True)
    elif model_name == 'Support Vector Classifer':
        mdl = SVC()
    elif model_name == 'Decision Tree Classifier':
        mdl = DecisionTreeClassifier(max_depth =3, random_state = 0)
    elif model_name == 'K Nearest Neighbour':
        mdl = KNeighborsClassifier(n_neighbors=10 , metric= 'minkowski' , p = 4)
    elif model_name == 'Gaussian Naive Bayes':
        mdl = GaussianNB()
    oneVsRest = OneVsRestClassifier(mdl)
    oneVsRest.fit(x_train, y_train)
    y_pred = oneVsRest.predict(x_test)
    # Performance metrics
    accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)
    # Get precision, recall, f1 scores
    precision, recall, f1score, support = score(y_test, y_pred, average='micro')
    print(f'Test Accuracy Score of Basic {model_name}: % {accuracy}')
    print(f'Precision : {precision}')
    print(f'Recall : {recall}')
    print(f'F1-score : {f1score}')
    # Add performance parameters to list
    perform_list.append(dict(
        [('Model', model_name), ('Test Accuracy', round(accuracy, 2)), ('Precision', round(precision, 2)),
         ('Recall', round(recall, 2)), ('F1', round(f1score, 2))]))



classifier = RandomForestClassifier(n_estimators=100 ,criterion='entropy' , random_state=0).fit(x_train, y_train)
classifier
y_pred = classifier.predict(x_test)
y_pred1 = cv.transform(['Katrina Kaif, Siddhant Chaturvedi, and Ishaan Khatter\'s latest episode of Koffee With Karan S7 is here and has taken over the internet. Pinkvilla had exclusively reported that the trio recently shot for their episode and had crazy fun. The trio is all set to star together in Phone Bhoot.  The film also stars Jackie Shroff, Sheeba Chadha, and Nidhi Bisht in supporting roles. Directed by Gurmmeet Singh, it has been written by Ravi Shankaran and Jasvinder Singh Bath and bankrolled by Ritesh Sidhwani and Farhan Akhtar’s Excel Entertainment. It is slated to release on November 4 this year.'])
yy = classifier.predict(y_pred1)
result = ""
if yy == [0]:
  result = "Business News"
elif yy == [1]:
  result = "Tech News"
elif yy == [2]:
  result = "Politics News"
elif yy == [3]:
  result = "Sports News"
elif yy == [4]:
  result = "Entertainment News"
print(result)