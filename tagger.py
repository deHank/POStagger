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

#Getting all of the words in the corpus
res = re.findall(r'\S+', trainData)

tags = re.findall(r'/\/[\S]+/gm')



#Tag regex: /\/[A-Z#$.,:()"']*/gm
{}