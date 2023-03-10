# -*- coding: utf-8 -*-
"""Sentiment Analysis: Vader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sDBsVlVMWyBUz8rNT7CD7k40Hh9Ev_bu
"""

# VADER

"""### Vader (Valence Aware Dictionary and Sentiment Reasoner)

+ Is a lexicon ***(the vocabulary of a person, language, or branch of knowledge. basically a dictionary)*** and rule-based sentiment analysis tool (pre-print library) that is specifically attuned to sentiments expressed in social media
+ It is used for sentiment analysis of text which has both the polarities.
    + for example: **positive & negative**
+ Vader is used to quantify how much positive or neegative emotion the text has and also the intensity of emotion (by printing a numerical values to be interpreted)

### Advantages
+ It does not require any training data
+ It can very well understand the sentiment of a text containing:
    + emoticons
    + slangs
    + conjugations
    + capital words
    + punctuations
    + etc
+ It works excellent on social media text
"""

!pip install nltk[twitter]
# Twitter is gonna use twython library

# Download a dictionary for VADER
import nltk 
nltk.download ('vader_lexicon')

# Use package from nltk.sentiment.vader, import class SentimentIntensityAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Create object for class SentimentIntensityAnalyzer
vader = SentimentIntensityAnalyzer()

# Use the object to check whether given text is +ve or -ve

# 1. Example of +ve Review
sample = 'I really love Podd and Earth'
#vader provides you a method called vader.polarity_scores() and return a float value to determine whether it's a +ve or -ve 
vader.polarity_scores(sample)

"""### Compound Score
The compound score is the sum of +ve, -ve & neutral scores which is then normalized between:
+ -1 (most extreme negative)
+ +1 (most extreme positive)

The more compound score closer to +1, the higher the positivity of the text
"""

# 2. Example of -ve Review
sample = 'I really don\'t like pizza'
vader.polarity_scores(sample)

# 3. Example of neutral Review
sample = 'Yesterday, football match was okay'
vader.polarity_scores(sample)

"""# Use VADER on .tsv (tab separated value) dataset"""

# Import dataset
from google.colab import files
upload = files.upload ()

# Check whether the file has been uploaded or not
!ls

"""# EDA"""

# Feed the dataset to pandas
import pandas as pd
data = pd.read_csv ('amazonreviews.tsv', sep = '\t') # --> \t for tab since the file is .tsv
data

# Check how many number of records
data.shape

# Check for missing values
data.dropna(inplace = True) # remove all missing values

# Recheck the shape
data.shape
# The shape is the same, so there's no missing values

data.columns

# To check how many +ve & -ve reviews
data['label'].value_counts()

# Lambda Functions
# Also known as anonymous functions
# Benefit:
        # 1. Can take any number of arguments but can only have one expression

x = lambda x : x + 10
    # 1. First x is the name of the function
    # 2. Second x is the argument
    # 3. x + 10 is the expression or condition

print(x(5))

    # The value of 5 will be passed to the argument
    # It makes the expression of x + 10 becomes 5 + 10
    # 5 + 10 = 15

# Multiple arguments
x = lambda x,y,z : x + y + z
print (x (10,5,6))

"""#### Use lambda for sentiment analysis"""

# To compute score cards and store in the new column 'Scores''
data['scores'] = data['review'].apply (lambda review : vader.polarity_scores (review)) # use apply to invoke the lambda function

data

# Print Review and Scores columns
data[['review', 'scores']]

# Print Compound Score
data['compound'] = data['scores'].apply(lambda scores : scores['compound'])
data

data[['review', 'compound']]

data['sentiment'] = data['compound'].apply(lambda c : 'pos' if c>=0 else 'neg')

data[['review', 'sentiment']]

# Compare sentiment with label
data[['label', 'sentiment']].head(10)