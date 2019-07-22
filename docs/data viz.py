'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!'''

from wordcloud import WordCloud
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
#create a list for polarity
polarity=[]

subjectivity=[]

# Continue your program below!

for tweet in tweetData:
    tweetTB = TextBlob(tweet['text'])
    polarity.append(tweetTB.polarity)
    subjectivity.append(tweetTB.subjectivity)

# Textblob sample:



#average of polarity and subjectivity
amount1=len(polarity)
amount2=len(subjectivity)
totalpolarity=0
totalsubjectivity=0

for i in polarity:
    totalpolarity+=i
averagepolarity=totalpolarity/amount1
print(averagepolarity)



for w in subjectivity:
    totalsubjectivity+=w
averagesub=totalsubjectivity/amount2
print(averagesub)



plt.hist(polarity,3,[ -.5, 0.5,] )
plt.xlabel('Polarity')
plt.ylabel('Frequency')
plt.title('Polarity Of Tweets')
plt.grid(True)
plt.show()


allthewords=""
for x in range(70):
    allthewords +=''+ tweetData[x]['text']
print(allthewords)
tweetTB = TextBlob(allthewords)
#print(tweetTB.words)

words=tweetTB.words
filteredWords={}

listofwords= ["like", "as", "and", "about", "https"]
for word in words:
    
    if not word.isalpha():
        continue
    if len(word)<=3:
        continue
    if word in listofwords:
        continue
    filteredWords[word] = tweetTB.word_counts[word]

variable = WordCloud().generate_from_frequencies(filteredWords.items())
plt.subplot(111)
plt.imshow(variable, interpolation='bilinear')
plt.figure(1)
plt.show()











print(filteredWords)
    
