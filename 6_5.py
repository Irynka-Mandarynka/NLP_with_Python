# Chapter 6
# Exercise 5
# Author Svitlana Synytsia
'''
Select one of the classification tasks described in this chapter, such as name
gender detection, document classification, part-of-speech tagging, or dialogue act
classification. Using the same training and test data, and the same feature extractor,
build three classifiers for the task: a decision tree, a naive Bayes classifier, and a
Maximum Entropy classifier. Compare the performance of the three classifiers on
your selected task. How do you think that your results might be different if you
used a different feature extractor?
'''
# I chose gender detection
import nltk
from nltk.corpus import names
import random
import math
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)
def gender_features(word): # function for determining gender of name
    return {'last_letter': word[-1]}
    print(gender_features('Peter-Nansy'))

    
featuresets = [(gender_features(n), g) for (n,g) in names]
size = int(len(featuresets) * 0.1)# setting a size for a testing data
train_set, test_set = featuresets[size:], featuresets[:size]

# NaiveBayesClassifier
# A NaiveBayesClassifier provides a trainable naive Bayes text classifier, with t
naiveBayesClassifier = nltk.NaiveBayesClassifier.train(train_set)
productivity=nltk.classify.accuracy(naiveBayesClassifier, test_set)
# Result from BayesClassifier
def entropy(labels):# function for determining the gender of names using entrop
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in nltk.FreqDist(labels)]
    return -sum([p * math.log(p,2) for p in probs])
productivity=entropy(['singular', 'plural', 'singular', 'plural'])
print productivity # result of productivit
## Using entropy, results getting better as we use searching tools for finding of sets of parameters that aims to increase productivity of classificators
