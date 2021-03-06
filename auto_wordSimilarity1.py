#!/usr/bin/env python

import nltk
import itertools
import math
import networkx as nx
import matplotlib.pyplot as plt


s1 = "Businessweeks original purpose was to provide information and opinions as to what was happening in the business world  at the time"

s1_words =  nltk.word_tokenize(s1)

s2 = "Initally the magazine published sections that included topics such as marketing labour finance and management amoung others"
s2_words =  nltk.word_tokenize(s2)

s3 = "Businessweek was first published in September 1929 only weeks before the Stock Market Crash of 1929 the business world was in chaos"

s3_words =  nltk.word_tokenize(s3)

s4 = "September only weeks before Stock Crash"

s4_words =  nltk.word_tokenize(s4)

sentences = []
sentences.append(s1)
sentences.append(s2)
sentences.append(s3)
sentences.append(s4)

sen_by_word = []
sen_by_word.append(s1_words)
sen_by_word.append(s2_words)
sen_by_word.append(s3_words)
sen_by_word.append(s4_words)

total_common_words = []
weighted_sen = []
cnt = 1
cnt2 = 2
element_names = []
tot_element_names = []
#ele = []
ele2 = []
for l1, l2 in itertools.combinations(sen_by_word, 2): # two lists are chosen, l1 and l2 catches the lists
    common_words = [] 
    index1 = sen_by_word.index(l1) + 1
    index2 = sen_by_word.index(l2) + 1
    for e1, e2 in itertools.product(l1, l2): # a cartian product of all the words is produced, e1 and e2 catches the elements 
      if e1 == e2:
        common_words.append(e1) 
    total_common_words.append(common_words)
    wight = len(set(common_words)) / (math.log(len(l1),10) + math.log(len(l2),10))
    weighted_sen.append(wight)
    element_names = [] # create a new list 
    if wight != 0.0:
        element_names.append(index1)
        element_names.append(index2)       
        cnt2+=1    
    tot_element_names.append(element_names)

print weighted_sen
print ""
print ""
print tot_element_names
G = nx.Graph()


for index in range(len(sen_by_word)):
    var = "S" + str(index + 1)
    G.add_node(var)

#print G.nodes()

for index in range(len(tot_element_names)):
   #  if tot_element_names[index]:
    #   print tot_element_names[index]     
     if tot_element_names[index]:
       var = 'S' + str(tot_element_names[index][0])
       var1 = 'S' + str(tot_element_names[index][1])
       G.add_edge(var,var1)
      
print G.edges()
print G.nodes()

nx.draw_circular(G)

plt.show()

print nx.pagerank(G)


#G.add_edge(1,2)
#G.add_edge(2,3,{'weight':3.145})

