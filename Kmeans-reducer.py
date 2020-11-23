#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = {}
cen = {}
#lines = open("map121.log", "r") 
# input comes from STDIN
for line in sys.stdin:
#for line in lines:
    # remove leading and trailing whitespace
    line = line.strip() 
    # parse the input we got from mapper.py
    word,cen,count = line.split('\t', 2)
    # convert count (currently a string) to int
    #print(word)
    #print(cen)
    try:
        count = int(count)
        cen = str(cen)
    except ValueError:
        continue

    try:
        if word == '0' :
            word2count[word] = word2count[word]+count
            cen0 = cen
        elif word == '1' :
            word2count[word] = word2count[word]+count
            cen1 = cen
        elif word == '2' :
            word2count[word] = word2count[word]+count
            cen2 = cen
        elif word == '3' :
            word2count[word] = word2count[word]+count
            cen3 = cen
        elif word == '4' :
            word2count[word] = word2count[word]+count
            cen4 = cen
        elif word == '5' :
            word2count[word] = word2count[word]+count
            cen5 = cen
            
        
    except:
        word2count[word] = count

 
# write the tuples to stdout
# Note: they are unsorted
#if word == '0' :
for word in word2count.keys():
    if word == '0' :
        var0 =  "%s\t%s\t%s" % (word,cen0,word2count[word])
        print(var0)
        
    elif word == '1' :
        var1 =  "%s\t%s\t%s" % (word,cen1,word2count[word])
        print(var1)

    elif word == '2' :
        var2 =  "%s\t%s\t%s" % (word,cen2,word2count[word])
        print(var2)
        
    elif word == '3' :
        var3 =  "%s\t%s\t%s" % (word,cen3,word2count[word])
        print(var3)
        
    elif word == '4' :
        var4 =  "%s\t%s\t%s" % (word,cen4,word2count[word])
        print(var4)

    elif word == '5' :
        var5 =  "%s\t%s\t%s" % (word,cen5,word2count[word])
        print(var5)
