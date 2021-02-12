from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Import functions from others files
from extract_comments_users import *

datainsta = pd.DataFrame(extract_comments_users(data))


auth = tweepy.AppAuthHandler("U1JtNPSHYJvJikl5jjQCFyBX1", "e3cUrZLWg4ZklkBChWmzG3xdxODdaYjJxDGIUgV37dHOl5pNIq")
api = tweepy.API(auth)


# Sentiment Analysis

def cleantxt(text):
    text = re.sub(r'@[A-Za-z0-9:_]+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    return text


def percentage(part, whole):
    return 100 * float(part)/float(whole)


keyword = input("Please enter keyword or hashtag to search: ")
noOfTweet = int(input("Please enter how many tweets to analyze: "))
tweets = tweepy.Cursor(api.search, q=keyword).items(noOfTweet)
tweet_list = []

for tweet in tweets:
    tweet_list.append(tweet.text)


tweet_list = pd.DataFrame(tweet_list)

# Cleaning Data
# Drop duplicates
tweet_list.drop_duplicates(inplace=True)


# Cleaning Text (RT, Punctuation etc)

# Creating new dataframe and new features and join instagram data
tw_list = pd.DataFrame(tweet_list)
tw_list = pd.concat([tw_list, datainsta.rename(columns={'0':'text'})], ignore_index=True)
tw_list["text"] = tw_list[0]


# Removing RT, Punctuation etc
tw_list["text"] = tw_list["text"].apply(cleantxt)


# Calculating Negative, Positive, Neutral and Compound values
tw_list[["polarity", "subjectivity"]] = tw_list["text"].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
tw_list.to_csv("pruebasamu.csv")

for index, row in tw_list["text"].iteritems():
    score = SentimentIntensityAnalyzer().polarity_scores(row)
    # print(score)
    neg = score["neg"]
    neu = score["neu"]
    pos = score["pos"]
    comp = score["compound"]
    if neg > pos:
        tw_list.loc[index, "sentiment"] = "negative"
    elif pos > neg:
        tw_list.loc[index, "sentiment"] = "positive"
    else:
        tw_list.loc[index, "sentiment"] = "neutral"
    tw_list.loc[index, "neg"] = neg
    tw_list.loc[index, "neu"] = neu
    tw_list.loc[index, "pos"] = pos
    tw_list.loc[index, "compound"] = comp


# Creating new data frames for all sentiments (positive, negative and neutral)
tw_list_negative = tw_list[tw_list["sentiment"] == "negative"]
tw_list_positive = tw_list[tw_list["sentiment"] == "positive"]
tw_list_neutral = tw_list[tw_list["sentiment"] == "neutral"]


def count_values_in_column(data, feature):
    total = data.loc[:, feature].value_counts(dropna=False)
    percentage = round(data.loc[:, feature].value_counts(dropna=False, normalize=True)*100, 2)
    return pd.concat([total, percentage], sort=True, axis=1, keys=["Total", "Percentage"])
    # Count_values for sentiment


wey = count_values_in_column(tw_list, "sentiment")
wey2 = pd.DataFrame(wey)
positive = wey2["Percentage"][2]
nue = wey2["Percentage"][1]
nega = wey2["Percentage"][0]

# create data for Pie Chart
pichart = count_values_in_column(tw_list,"sentiment")
names = pichart.index
size = pichart["Percentage"]


# Create a circle for the center of the plot
my_circle = plt.Circle((0,0), 0.6, color="white")
plt.pie(size, labels=names, colors=["red", "blue", "green"])
plt.title("Sentiment Analysis Result for "+keyword+"")
plt.text(-2, 0.9, ""+str(len(tw_list))+" comments analyzed", size=12, color='black')
labels = ["Negative ["+str(wey2["Percentage"][0])+"%]", "Neutral ["+str(wey2["Percentage"][1])+"%]", "Positive ["+str(wey2["Percentage"][2])+"%]"]
plt.legend(labels)
plt.show()




