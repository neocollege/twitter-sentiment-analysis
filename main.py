from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100*float(part)/float(whole)

consumerKey ="gTxaJTgw8a9SIwVhOb7ZZuPic"
consumerSecret="A0ntVBJTrTneC3xZyIwIcciVBg8tQwS6BssX0NSKsEK6MTn2nB"
accessToken="3853860621-GQ3lSrCFhVDa3DPnza9HYDRTzJeplSuQ81YS3aW"
accessTokenSecret="4XsaWG4RyuGBEDNYRKtFJIL64RiMPX95PJM8hjSS5pnpN"

auth = tweepy.OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter keyword/hashtag to search about: ")
noOfSearchTerms = int(input("Enter how many search terms to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms)

positive = 0
negative =  0
neutral =  0
polarity = 0

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity ==0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

if(polarity == 0):
    print("Neutral")
elif(polarity > 0):
    print("Positive")
elif(polarity < 0):
    print("Negative")

labels = ['Positive ['+str(positive)+'%]', 'Negative ['+str(negative)+'%]', 'Neutral ['+str(neutral)+'%]']
sizes = [positive, negative, neutral]
colors = ['yellowgreen','gold','red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.title('How people are reacting on "+searchTerm+" by analyzing "+str(noOfSearchTerms)+" tweets: ')
plt.axis('equal')
plt.tight_layout()
plt.show()