# This is a sample Python script.
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sys import argv

argv
train = argv[1]

testSet = argv[2]

taggedSet = argv[4]

trainData = ''

with open(train, "r") as f:
    trainData += f.read()

#Data Cleanup, the \/ is to remove any names like McGraw\/Hill/NNP
#makes it into McGrawHill/NNP
trainData = trainData.replace('[','')
trainData = trainData.replace(']','')
trainData = trainData.replace('\/', '')
# Getting all of the words in the corpus
res = re.findall(r'\S+', trainData)


#tags = re.findall(r'/\/[\S]+/gm')

# Now I need to create a dictionary with 1 size tuples
# Make a dictionary with tags as key, and total count of tags

tagCount = {}
wordCount = {}
for j in range(len(res)):

    #Splitting word before tag, so if it was Pierre/NNP, i'd get Pierre
    word = res[j].partition("/")[0]
    # for i in range(len(res) - j + 1):
    # Generate our n-grams, this will generate n-grams up to the size of the ngram parameter
    tag = res[j].partition("/")[2]

    # Counting ngram occurence
    if word in wordCount and (word != "[") and (word != "]"):
        wordCount[word] += 1
    else:
        wordCount[word] = 1

    if tag in tagCount:
        tagCount[tag] += 1
    else:
        tagCount[tag] = 1

# Now, I need 2 tuples. ((Word),{Tag), num of times)
{}
