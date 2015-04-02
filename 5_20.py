# Chapter 5
# Exercise 20
# Author Svitlana Synytsia
'''
Write code to search the Brown Corpus for particular words and phrases ac-
cording to tags, to answer the following questions:

a. Produce an alphabetically sorted list of the distinct words tagged as  MD .
'''
import nltk
from nltk.corpus import brown
tagged_w=brown.tagged_words()
sorted(set([word for word, tag in tagged_w if tag=='MD']))#���������� �� ������� ��� � ����� MD
print sorted(set([word for word, tag in tagged_w if tag=='MD']))

'''
b. Identify words that can be plural nouns or third person singular verbs (e.g.,
deals, flies).
'''
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
patterns = [           # ��������� ������� ��� ������
    (r'.*es$', 'VBZ'),                # 䳺����� 3� ����� ������
    (r'.*s$', 'NNS'),                 # �������� � ������
	]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown_sents[3])   # ���� 3� ������ ������� �����, �� ������ ���� patterns
# �� ����� � ���������� ��������, �� ����� ���������� ������� � ������ �� �������
# ����, ���� ���� � ������, �������� ������ None
print regexp_tagger.tag(brown_sents[3])

'''
c. Identify three-word prepositional phrases of the form IN + DET + NN (e.g.,
in the lab).
'''
def process(sentence):     # ������� ��� ������ ��� � ������
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):   # ����������� � ����� ���
            if (t1=='IN' and t2 == 'DT' and t3=='NN'):   # ����� ������
                print w1, w2, w3

for tagged_sent in brown.tagged_sents():
	process(tagged_sent)
print process(tagged_sent)


                
         
