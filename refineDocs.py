# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:42:07 2018

@author: Chintan Rajvir
"""

import re
from nltk.corpus import stopwords
import json

stopWords = set(stopwords.words('english'))
specialChar = "~`!@#$%^&*()_+={}[]|\\:;\'\"<>?/.,"

urlRE = re.compile("http")
    
fileName = "Datasets/d"
for i in range(1, 12):
    dct = dict()
    c = 0
    with open(fileName+str(i)+".txt", errors="ignore") as f:
        for lines in f:
            lines = lines.strip().split('|')
            lines = lines[2].split()
            wrds = []
            for phrase in lines:
                phrase = phrase.lower()
                phrase = phrase.rstrip("'s")
                chars = list(phrase)
                phrase = ""
                for ch in chars:
                    if ch not in specialChar:
                        phrase+=ch
                if urlRE.match(phrase) == None and phrase!="-" and phrase not in stopWords and phrase not in specialChar:
                    try:
                        phrase.encode('ascii')
                        if phrase!="":
                            wrds.append(phrase)
                    except:
                        continue
            if wrds!=[]:
                dct.update({c: wrds})
                c+=1
    data = {"data": dct} 
    with open("d"+str(i)+"_output.json", 'w') as outfile:
        json.dump(data, outfile)