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
wordTag = ()
wordTagCount = {}
tagAndPrev = {}
tagAndPrevTuple = ()
for j in range(len(res)):
    tag = res[j].partition("/")[2]
    prevTag = res[j-1].partition("/")[2]
    #had to make j>0 check bc a tag at 0 would have no previous tag
    if j > 0:
        #This will store the count of tags and previous tags
        #Stored in tuple form (expected, given) aka (current, previous)
        tagAndPrevTuple = (tag,prevTag)
        if tagAndPrevTuple in tagAndPrev:
            tagAndPrev[tagAndPrevTuple] += 1
        else:
            tagAndPrev[tagAndPrevTuple] = 1
    #Splitting word before tag, so if it was Pierre/NNP, i'd get Pierre
    word = res[j].partition("/")[0]
    # for i in range(len(res) - j + 1):
    # Generate our n-grams, this will generate n-grams up to the size of the ngram parameter

    wordTag = (word,tag)
    # Counting ngram occurence
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

    if wordTag in wordTagCount:
        wordTagCount[wordTag] += 1
    else:
        wordTagCount[wordTag] = 1

    if tag in tagCount:
        tagCount[tag] += 1
    else:
        tagCount[tag] = 1

# Now, I need 2 tuples. ((Word),{Tag), num of times)
# So at this point, I need to someonehow use chainrule and the 2 assumptions in order to calculate
# the proabbility
tagAndPrev_Matrix = {}
for tagPrev in tagAndPrev:
    tagAndPrevCount = tagAndPrev[tagPrev]
    #so if it was RRR, VBV, Prev tag would be RRR and tag would be VBV
    prev_tag, tag = tagPrev
    prob = tagAndPrevCount / tagCount[prev_tag]

    #Adding probability of a tag coming with its prior tag to a 2d matrix
    #Dictionary, with another dicionarty in it
    #if the prev tag is not in the dicionary, it will make a dicionary dictionary with
    #the tag as the key and a prev tag as the key to the matrix
    if prev_tag in tagAndPrev_Matrix:
        tagAndPrev_Matrix[prev_tag][tag] = prob
    else:
        tagAndPrev_Matrix[prev_tag] = {tag: prob}

#Now for the first pt of the equation we need to get the P(word|tag)
wordTagMatrix = {}
for wordTag in wordTagCount:
    #getting the count of the word tag
    wordAndTagCount = wordTagCount[wordTag]
    word, tag = wordTag
    prob = wordAndTagCount/tagCount[tag]

    if wordTag in wordTagMatrix:
        wordTagMatrix[word][tag] = prob
    else:
        wordTagMatrix[word] = {tag: prob}

{}