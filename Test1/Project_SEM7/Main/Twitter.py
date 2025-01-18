from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
from termcolor import cprint
from wordcloud import WordCloud, STOPWORDS

import re
from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
consumerKey = "3EvOEyk4WcluWq2eZiyHZyNhq"
consumerSecret = "Q3Sk9zZIIz3tvrwmyEn6rAVBjIsx2j1Ad7jryGhtdoJYMPCG7X"
accessToken = "1467127046543319040-viH7mQYzUhBDUy1HWWwTtRZRcPlqF5"
accessTokenSecret = "tcs0nR2CTmJ6PPKXW93i6wn9rqg5jOYC3Jz3pKcDhbkdE"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


def percentage(part, whole):
    return 100 * float(part)/float(whole)
keyword = input("Please enter keyword or hashtag to search:")
nooftweets =int(input("Enter Number of Tweets to analyse:"))
cprint("Analyzing the Tweets🔄...",'red', attrs=['blink'])
tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(nooftweets)
pos = 0
neg = 0
neu = 0
polarity = 0
tweet_list = []
neu_list = []
neg_list = []
pos_list = []
for tweet in tweets:

    print(tweet.text)
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


#print(pos)
#print(neg)
#print(neu)
pos = percentage(pos, nooftweets)
neg = percentage(neg, nooftweets)
neu = percentage(neu, nooftweets)
polarity = percentage(polarity, nooftweets)
pos = format(pos, '.1f')
neg = format(neg, '.1f')
neu = format(neu, '.1f')
#print(pos)
#print(neg)
#print(neu)

tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neu_list)
negative_list = pd.DataFrame(neg_list)
positive_list = pd.DataFrame(pos_list)
print("total number: ",len(tweet_list))
print("positive number: ",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))
plt.subplot(2,1,1)
labels = ['Positive ['+str(pos)+'%]' , 'Neutral ['+str(neu)+'%]','Negative ['+str(neg)+'%]']
sizes = [pos, neu, neg]
colors = ['green', 'Yellow','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90,shadow = True)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for keyword= "+keyword+"" )
plt.axis('equal')
plt.subplot(2,1,2)
l1=len(positive_list)
l2=len(negative_list)
l3=len(neutral_list)
k1=[l1,l2,l3]
k2=["POSITIVE","NEGATIVE","NEUTRAL"]
c=["Green","Red","Yellow"]
z=plt.bar(k2,k1,color =c,width = 0.4)
plt.title("Tweet Count Based on Emotion")
labels = ['😊', '😠', '😐']
for rect1, label in zip(z, labels):
    height = rect1.get_height()
    plt.annotate(label,(rect1.get_x() + rect1.get_width()/2, height+.05),ha="center",va="bottom",fontsize=30)
plt.show()

# combine all tweets into one string
all_tweets = ' '.join(tweet_list[0])

# generate word cloud
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=STOPWORDS,
                      min_font_size=10).generate(all_tweets)

# plot word cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()


# extract hashtags from tweets
hashtags = re.findall(r'\#\w+', all_tweets)

# count frequency of each hashtag
freq = Counter(hashtags)

# get top 10 hashtags
top_hashtags = freq.most_common(10)

# create bar chart
plt.barh([x[0] for x in top_hashtags], [x[1] for x in top_hashtags])
plt.title('Top Hashtags')
plt.xlabel('Frequency')
plt.show()
# create list of polarities and subjectivities
polarities = [TextBlob(tweet).sentiment.polarity for tweet in tweet_list[0]]
subjectivities = [TextBlob(tweet).sentiment.subjectivity for tweet in tweet_list[0]]

# create scatter plot
plt.scatter(polarities, subjectivities)
plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()
