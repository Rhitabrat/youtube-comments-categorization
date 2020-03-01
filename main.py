import nltk
from nltk.tag import StanfordPOSTagger
import os

text = "please explain something...u r just reading the slides.. :("

tokens = nltk.word_tokenize(text)

# print(nltk.pos_tag(tokens))


# using stanford pos tagger
mypath = os.path.abspath(os.getcwd())
jar = mypath + '/stanford-postagger-full-2018-10-16/stanford-postagger.jar'
model = mypath + '/stanford-postagger-full-2018-10-16/models/english-left3words-distsim.tagger'

pos_tagger = StanfordPOSTagger(model, jar)

print(pos_tagger.tag(text.split()))


