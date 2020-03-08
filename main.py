# import nltk
# from nltk.tag import StanfordPOSTagger
# import os
# import csv

# text = "please explain something...u r just reading the slides.. :("

# with open('/Scrapper/comments.csv', 'r') as file:
#     reader = csv.reader(file)
#     # for row in reader:
#     #     print(row)

# tokens = nltk.word_tokenize(text)

# # print(nltk.pos_tag(tokens))


# # using stanford pos tagger
# mypath = os.path.abspath(os.getcwd())
# jar = mypath + '/stanford-postagger-full-2018-10-16/stanford-postagger.jar'
# model = mypath + '/stanford-postagger-full-2018-10-16/models/english-left3words-distsim.tagger'

# pos_tagger = StanfordPOSTagger(model, jar)

# print(pos_tagger.tag(text.split()))



import numpy as np
import pandas as pd
from nltk import pos_tag
from nltk.tokenize import word_tokenize 

df = pd.read_csv('Scrapper/comments.csv', header=None)
df.rename(columns={0: 'comments'}, inplace=True)

# data preprocessing
print(word_tokenize(df['comments'][0]))


# tagged_df = df['comments'].str.split().map(pos_tag)

# print(tagged_df.head())

