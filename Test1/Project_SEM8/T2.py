import nltk
import random
import tweepy
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB,MultinomialNB
import pyspark
import findspark
positive_messages = open("positive.txt","r").read()
negative_messages= open("negative.txt","r").read()
all_words=[]
documents=[]
allowed_word_types = ["J"]
for p in positive_messages.split('\n'):
    documents.append((p,"pos"))
    words=word_tokenize(p)
    pos=nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
for p in negative_messages.split("\n'"):
        documents.append((p,"neg"))
        words=word_tokenize(p)
        pos=nltk.pos_tag(words)
        for w in pos:
            if w[1][0] in allowed_word_types:
                all_words.append(w[0].lower())
                all_words=nltk. FreqDist(all_words)
                word_features=list(all_words.keys())[:5000]


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:features[w] = (w in words)
    return features
featuresets = [(find_features(rev), category) for (rev, category) in documents]
random.shuffle(featuresets)
testing_set = featuresets[10000:]
training_set = featuresets[:10000]
classifier = nltk.NaiveBayesClassifier.train(training_set)

from tweepy import Stream, OAuthHandler
import json
import classifier as s

consumerKey = "vOy5ruvn0XP5N0cCx4fOUALOM"
consumerSecret = "VjPp9XZsNGCP4o5YlXXWSkJ0fwWkXMGpK9PZTaONXEK0nOHYeB"
accessToken = "1467127046543319040-w6xFI7HtErblT4YUS8L9qvv4flwrZn"
accessTokenSecret = "UGKhvNtRYdGKlfWLuJEznjXsG8Y4TuvCU7doN8dnaLdob"
class listener(tweepy.Stream):
    def on_data(self,data):
        all_data = json.loads(data)
        tweet=all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet,sentiment_value,confidence)
        if confidence*100>=80:
            output= open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        return True
    def on_error(self, status):
        print(status)
        auth = OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["#Trump"])

findspark.init()
sc = pyspark.SparkContext(appName="myAppName").getOrCreate()
spark = pyspark.sql.SparkSession(sc)
sc. conf.getAllO
allowed_word_types = ["JJ"]
rdd_positive = sc.textFile("positive.txt")
rdd_negative = sc.textFile("negative.txt")
rdd_all_tokenized words = rdd_positive.map(lambda tweet:
                                           (nltk.pos_tag(word_tokenize(tweet)),1)).union(rdd_negative.map(lambda tweet:

(nltk.pos_tag(word_tokenize(tweet)),0)))
rdd_selected_words = rdd_all_tokenized words.map(lambda review:\
                                                 ([word[0] for word in review[0] if word[1] in allowed_word_types].review[1]))
rdd_all_words = rdd_selected_words.flatMap(lambda words:
                                           words[0]).distinct0
rdd_all_broadcast_words = sc.broadcast(rdd_all_words.collect())
rdd_featured_instances = rdd_selected_words.map(lambda instance:
                                                (find_features(instance[0]), instance[1]))
def find features (instance):
    features = []
    for word in rdd_all_broadcast_words.value:
        if word in instance:
            features.append(1)
        else:
            features.append(0)
    return features
rdd all words.coalesce(1. True).saveAsTextFile("all_words")
rdd training set rdd featured_instances.map(lambda instance:
                                            LabeledPoint(label=instance[1].features=instance[0]))
from pyspark.mllib.classification import NaïveBayes, NaiveBayes Model
from pyspark.milib.util import MLUtils
NB model NaïveBayes.train(rdd_training_set,1.0)