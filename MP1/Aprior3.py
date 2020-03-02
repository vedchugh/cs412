import random 
import os
import string
import sys
import re
from collections import Counter

delimiters = ";"
unique_words = []
unique_cats = []
bag_of_words = []

def patern():
    ret = []
    freq1 = dict() #define a dictionary
    file = sys.stdin # read the file
    file1 = file
    for title in file: #loop elements of the file
        bag_of_words.append(title)
        for j in re.split(delimiters, title.strip()): #loop and extract words from titles
            unique_words.append(j.strip()) #bag of words
    cnt = Counter(unique_words) # counter index the list of words
    f=open("paterns.txt","w") #write to file
    for k,v in cnt.items(): #loop the words
        if v >= 771:  #loop for support 0.01
            print("%s:%s" % (v,k), file=f) # print key and values
            freq1[v]=k #write to the dict the list of Frequent-1 itemsets
    #print freq1
    f.close()
    #print bag_of_words
    for k,v in freq1.items(): #loop the words
        for x,y in freq1.items(): 
            if y != v:
                z =  "%s;%s" % (y,v)
                #print z
                for title in bag_of_words:
                    if (v in title) and (y in title):
                        unique_cats.append(z)
    cnt2 = Counter(unique_cats)
    
    freq2 = dict()
    for k,v in cnt2.items(): #loop the words
        m = sorted(re.split(delimiters, k.strip()))
        n = ';'.join([str(elem) for elem in m])
        if n not in list(freq2.values()):
            freq2[v] = n
    f=open("patterns.txt","w") #write to file
    for k,v in freq2.items(): 
        if k >= 771:  #loop for support 0.01
            print("%s:%s" % (k,v), file=f) # print key and values
    f.close()
        #print unique_cats

    

patern()