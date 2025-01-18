from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import re
import pandas as pd
from termcolor import colored, cprint
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
consumerKey = "mEnc3ivDuSTMEKJ3OcGrxsG4D"
consumerSecret = "7iMKo5eNWejCE2sECbNqFGGoQGns1MltMaEsGlp74scDue663z"
accessToken = "1822776940182507520-ECttfoLiEWaAdJns6pDbb7WsgYVu69"
accessTokenSecret = "6Ur5dtRKORzrT8ZcUwudVzd9WsSxvk3eXm3zElHocJwpq"
'''
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
'''
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAN1CvQEAAAAAP2Pzx%2FYlXGsG7Z5bm6k%2B7in%2BmlU%3D9FcVi8kN5VWhyOiGGFiVUpLlV7FCRJjg9aTUnjy3r2u1s3zrSh')

def percentage(part, whole):
    return 100 * float(part)/float(whole)
keyword = input("Please enter keyword or hashtag to search:")
nooftweets =int(input("Enter Number of Tweets to analyse:"))
cprint("Analyzing the Tweets🔄...",'red', attrs=['blink'])
#tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(nooftweets)
tweets = client.search_recent_tweets(query=keyword, max_results=nooftweets)
pos = 0
neg = 0
neu = 0
polarity = 0
tweet_list = []
neu_list = []
neg_list = []
pos_list = []
for tweet in tweets:

    #print(tweet.text)
    tweet_list.append(tweet.text)
    analysis = TextBlob(tweet.text)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity
    if neg > pos:
        neg_list.append(tweet.text)
        neg += 1
    elif pos > neg:
        pos_list.append(tweet.text)
        pos += 1
    elif pos == neg:
        neu_list.append(tweet.text)
        neu += 1

tweets = [tweet for tweet in tweet_list]

# Creates a dataframe of the tweets
#print(tweets)
tweets_df = pd.DataFrame(tweets, columns = ['Tweets'])
#print(tweets_df)
for _,row in tweets_df.iterrows():
    row['Tweets'] = re.sub(r'http\S+', '', row['Tweets'])
    row['Tweets'] = re.sub(r'#\S+', '', row['Tweets'])
    row['Tweets'] = re.sub(r'@\S+', '', row['Tweets'])
    row['Tweets'] = re.sub(r'http\S+', '', row['Tweets'])
    row['Tweets'] = re.sub('\\n', '', row['Tweets'])
#print(tweets_df)
tweets_df['Polarity'] = tweets_df['Tweets'].map(lambda tweet: TextBlob(tweet).sentiment.polarity)
tweets_df['Result'] = tweets_df['Polarity'].map(lambda polarity: 'pos' if polarity > 0 else 'neg')

positive = tweets_df[tweets_df.Result == 'pos'].count()['Tweets']
negative = tweets_df[tweets_df.Result == 'neg'].count()['Tweets']
x=["Positive", "Negative"]
plt.bar(x,[positive, negative], color=["green", "red"])
y=["Positive","Negative"]
plt.legend(y)
plt.show()