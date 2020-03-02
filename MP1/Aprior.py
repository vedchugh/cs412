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
unique_cats2 = []

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
    for k,v in cnt.iteritems(): #loop the words
        if v >= 771:  #loop for support 0.01
            print >>f,"%s:%s" % (v,k) # print key and values
            freq1[v]=k #write to the dict the list of Frequent-1 itemsets
    #print freq1
    f.close()
    #print bag_of_words
    for k,v in freq1.iteritems(): #loop the words
        for x,y in freq1.iteritems(): 
            if y != v:
                z =  "%s;%s" % (y,v)
                #print z
                for title in bag_of_words:
                    items = re.split(delimiters, title.strip())
                    if (v in items) and (y in items):
                        unique_cats.append(z)
    cnt2 = Counter(unique_cats)
    
    freq2 = dict()
    for k,v in cnt2.iteritems(): #loop the words
        m = sorted(re.split(delimiters, k.strip()))
        n = ';'.join([str(elem) for elem in m])
        if n not in freq2.values():
            freq2[v] = n

    freq3 = dict()
    for k,v in freq2.iteritems(): #loop the words
        for x,y in freq1.iteritems(): 
            words = re.split(delimiters, v.strip())
            if y not in words:
                z =  "%s;%s" % (v,y)
                #print z
                for title in bag_of_words:
                    items = re.split(delimiters, title.strip())
                    if (y in items):
                        if all(x in items for x in words):
                            unique_cats2.append(z)
    cnt3 = Counter(unique_cats2)
    for k,v in cnt3.iteritems(): #loop the words
        m = sorted(re.split(delimiters, k.strip()))
        n = ';'.join([str(elem) for elem in m])
        if n not in freq3.values():
            freq3[v] = n
    f=open("patterns.txt","w") #write to file
    for k,v in cnt.iteritems(): #loop the words
        if v > 771:  #loop for support 0.01
            print >>f,"%s:%s" % (v,k) # print key and values
    for k,v in freq2.iteritems(): 
        if k > 771:  #loop for support 0.01
            print >>f,"%s:%s" % (k,v) # print key and values
    for k,v in freq3.iteritems(): 
        if k > 771:  #loop for support 0.01
            print >>f,"%s:%s" % (k,v) # print key and values
    f.close()
    
    #print unique_cats2

    
 
patern()
