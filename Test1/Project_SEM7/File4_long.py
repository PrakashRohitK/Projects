import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB

#Reading DataSet
df = pd.read_csv(r"news-article-categories.csv")
k = pd.set_option('display.max_columns', None)
l = pd.set_option('display.max_rows', None)
# print(df.head())
# print(df.shape)
# print(df.info())

# print(df['category'].value_counts())
target_category = df['category'].unique()
# print(target_category)
df['categoryId'] = df['category'].factorize()[0]
# print(df.tail())
df1 = df[['category', 'categoryId']].drop_duplicates().sort_values('categoryId')
print(df1)

# Bar Chat
df.groupby('category').categoryId.value_counts().plot(kind="bar",color=["pink", "orange", "red", "yellow", "blue", "green", "grey","black", "magenta", "cyan"])
plt.xlabel("Category of data")
plt.title("Visualize numbers of Category of data")

# Pie Chart
fig = plt.figure(figsize=(5, 5))
colors = ["skyblue"]
art_and_craft = df[df['categoryId'] == 0]
business = df[df['categoryId'] == 1]
comedy = df[df['categoryId'] == 2]
crime = df[df['categoryId'] == 3]
education = df[df['categoryId'] == 4]
entertainment = df[df['categoryId'] == 5]
environment = df[df['categoryId'] == 6]
media = df[df['categoryId'] == 7]
politics = df[df['categoryId'] == 8]
religion = df[df['categoryId'] == 9]
science = df[df['categoryId'] == 10]
sports = df[df['categoryId'] == 11]
tech = df[df['categoryId'] == 12]
women = df[df['categoryId'] == 13]
count = [art_and_craft['categoryId'].count(), business['categoryId'].count(), comedy['categoryId'].count(),
         crime['categoryId'].count(),
         education['categoryId'].count(), entertainment['categoryId'].count(), environment['categoryId'].count(),
         media['categoryId'].count(),
         politics['categoryId'].count(), religion['categoryId'].count(), science['categoryId'].count(),
         sports['categoryId'].count(), tech['categoryId'].count(), women['categoryId'].count()]
z = ['art_and_craft', 'business', 'comedy', 'crime', 'education', 'entertainment', 'environment', 'media', 'politics',
     'religion', 'science', 'sports', 'tech', 'women']
plt.pie(count, labels=z,autopct="%1.1f%%",shadow=True,colors=colors,startangle=45,explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05))
# plt.show()

text = df["body"]
# print(text.head(10))
category = df['category']
# print(category.tail(10))
df['body'] = df['body'].apply(str)

#Removing Special Characters
def special_char(text):
    reviews = ''
    for x in text:
        if x.isalnum():
            reviews = reviews + x
        else:
            reviews = reviews + ' '
    return reviews
df['body'] = df['body'].apply(special_char)

#Converting to Lowercase
def convert_lower(text):
    return text.lower()
df['body'] = df['body'].apply(convert_lower)


# print(df['body'][0])

#Removing Stopwords
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return [x for x in words if x not in stop_words]
df['body'] = df['body'].apply(remove_stopwords)


# print(df['body'][1])
##Lemmatization
def lemmatize_word(text):
    wordnet = WordNetLemmatizer()
    return " ".join([wordnet.lemmatize(word) for word in text])
df['body'] = df['body'].apply(lemmatize_word)

# print(df['body'][1])
# print(df)

x = df['body']
y = df['categoryId']
x = np.array(df.iloc[:, 0].values)
y = np.array(df.categoryId.values)
cv = CountVectorizer(max_features=5000)
x = cv.fit_transform(df.body).toarray()
print("X.shape = ", x.shape)
print("y.shape = ", y.shape)
# Train Test and Split the Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, shuffle=True)
# print(len(x_train))
# print(len(x_test))

perform_list = []


def run_model(model_name, est_c, est_pnlty):
    mdl = ''
    if model_name == 'Logistic Regression':
        mdl = LogisticRegression(max_iter=10000, solver='lbfgs')
    elif model_name == 'Random Forest':
        mdl = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0)
    elif model_name == 'Multinomial Naive Bayes':
        mdl = MultinomialNB(alpha=1.0, fit_prior=True)
    elif model_name == 'Support Vector Classifer':
        mdl = SVC()
    elif model_name == 'Decision Tree Classifier':
        mdl = DecisionTreeClassifier()
    elif model_name == 'K Nearest Neighbour':
        mdl = KNeighborsClassifier(n_neighbors=10, metric='minkowski', p=4)
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


"""
run_model('Logistic Regression', est_c=None, est_pnlty=None)
run_model('Random Forest', est_c=None, est_pnlty=None)
run_model('Multinomial Naive Bayes', est_c=None, est_pnlty=None)
run_model('Support Vector Classifer', est_c=None, est_pnlty=None)
run_model('Decision Tree Classifier', est_c=None, est_pnlty=None)
run_model('K Nearest Neighbour', est_c=None, est_pnlty=None)
run_model('Gaussian Naive Bayes', est_c=None, est_pnlty=None)
model_performance = pd.DataFrame(data=perform_list)
model_performance = model_performance[['Model', 'Test Accuracy', 'Precision', 'Recall', 'F1']]
print(model_performance)
"""
classify = SVC(kernel = 'linear', random_state = 100).fit(x_train, y_train)
y_pred = classify.predict(x_test)
y_pred1 = cv.transform(['George Zimmerman, the Florida man acquitted of murder in the Trayvon Martin case, is facing charges of misdemeanor stalking after he allegedlyÂ threatened and harassed a private investigator in December. A news release from the State Attorneyâ€™s Office for Seminole County, Florida,Â said Zimmerman was being investigated by the county sheriffâ€™s office over allegations that he stalked Dennis Warren late last year. Warren was hiredÂ to find people who might be interested in participating in â€œRest in Power: The Trayvon Martin Story,â€ a documentary series about the African American teenagerÂ who was fatally shot by Zimmerman, a white man acting as a neighborhood watch volunteer, in 2012.Â Â  Warren contacted Zimmerman in September and gave him information on how to contact Michael Gasparro, the seriesâ€™ executive producer. Zimmerman called Gasparro, and they talked about the documentary series, which will focus on the life and death of Martin, according to the Florida Sun-Sentinel.Â  Warren told deputies he did not hear from Zimmerman again until December, when Gasparro told him an â€œextremely agitatedâ€ Zimmerman was sending threatening messages, according to deputies who requested a warrant. In one of those texts, Zimmerman allegedly threatened that Warren would be eaten by an alligator: â€œ[The private investigator] is a [expletive] WHO BOTHERED MY UNCLE IN HIS HOME. Local OR former law officer Heâ€™s well on his way to the inside of a gator as well. 10-4?â€Â  Warren told investigators that he received 55 phone calls, 67 text messages, 36 voicemails and 27 emails from Zimmerman between Dec. 16, 2017, and Christmas Day. Some of the messages Zimmerman allegedly texted included â€œAnswer your phone (expletive)â€Â and â€œIâ€™ll see you before you realize it,â€ according to WKMG-TV in Orlando. Records show that when Warren asked Zimmerman to stop,Â he textedÂ â€œNO!â€ and then â€œPursue charges,â€Â according to Spectrum News 13 in Orlando. During this period, Zimmerman also allegedly threatened to â€œbeat Jay-Z,â€ an executive producer on the series, which is scheduled to premiere later this summer. Zimmerman told The Blast news site that â€œanyone who fucks with my parents will be fed to an alligator.â€ Records show that when Warren asked Zimmerman to stop, he textedÂ â€œNO!â€ and then â€œPursue charges,â€ according to Spectrum News 13. Zimmerman was issued a summons last week. He is scheduled to be arraigned May 30.']).toarray()
yy = classify.predict(y_pred1)
result = ""
if yy == [0]:
    result = "Art & Craft News"
elif yy == [1]:
    result = "Business News"
elif yy == [2]:
    result = "Comedy News"
elif yy == [3]:
    result = "Crime News"
elif yy == [4]:
    result = "Education News"
elif yy == [5]:
    result = "Entertainment News"
elif yy == [6]:
    result = "Environment News"
elif yy == [7]:
    result = "Media News"
elif yy == [8]:
    result = "Political News"
elif yy == [9]:
    result = "Religious News"
elif yy == [10]:
    result = "Science News"
elif yy == [11]:
    result = "Sports News"
elif yy == [12]:
    result = "Tech News"
elif yy == [13]:
    result = "Women News"

print(result)