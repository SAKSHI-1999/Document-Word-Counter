# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:17:17 2018

@author: Chintan Rajvir
"""

import json
import  time

timeList = []

for i in range(1, 12):
    with open('d'+str(i)+'_output.json', 'r') as f:
        dataset = json.load(f)
    data = dataset["data"]
    lines = len(data)
    wrds = []
    start = time.time()
    dct = dict()
    for j in range(lines):
        wrds += data[str(j)]
    s = set(wrds)
    for w in s:
        dct[w] = wrds.count(w)
    end = time.time()
    timeList.append(round(end-start, 3))
    print(len(dct))

for i in range(11):
    print("Doc:", i+1, "==>", timeList[i])