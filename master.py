#!/usr/bin/env python
import worker
import worker1
import json
import  time


# The data source can be any dictionary-like object
#datasource = dict(enumerate(data))

def mapfn(k, v):
	for w in v:
		yield w, 1

def reducefn(k, vs):
	result = sum(vs)
	return result

s = worker.Server()
s.mapfn = mapfn
s.reducefn = reducefn

timeList = []

for i in range(1, 12):
	with open('d'+str(i)+'_output.json', 'r') as f:
		dataset = json.load(f)
	datasource = dataset['data']
	s.datasource = datasource
	start = time.time()
	results = s.run_server(password="scorpion11")
	end = time.time()
	timeList.append(round(end-start, 3))
	print(len(results))
	with open('MR_Output/d'+str(i)+'_ansOfMapReduce.txt', 'w') as f:
		for keys in sorted(results):
			line = keys+"\t\t\t"+str(results[keys])+"\n"
			f.write(line)
			
for i in range(1, 12):
	print("Doc:", i, timeList[i-1]) 