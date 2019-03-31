#!/usr/bin/env python
from unionfind import *
from pprint import pprint
import operator

def setup():
    theFile = open('data.txt')
    rawData = theFile.read()
    theFile.close()
    
    #Split data string into list
    rawData = rawData.split('\n')
    rawData = filter(bool,rawData)
    
    cities = list()

    #Create and return sorted data in list
    data = list()
    for line in rawData:
        item = list()
        temp = line.split()
        item.extend([temp[0],temp[1],int(temp[2])])
        cities.extend([temp[0],temp[1]])
        data.append(item)

    return sorted(data, key=operator.itemgetter(2)),sorted(set(cities))

# Method to perform Kruskal's Algorithm    
def kruskal(data,cities):
    distance = 0
    result = list()
    cities = init(cities)
    for edge in range(len(data)):
        path = data.pop(0)
        if find(cities,path[0]) != find(cities,path[1]):
            union(cities, path[0],path[1])
	    e=path[0].rstrip()+path[1].rstrip()
            result.extend((e+str(path[2])))

            distance += path[2]
    return result,distance

data,cities = setup()
result,distance = kruskal(data,cities)
count=0
edge=''

for r in result:
 if(count<3):
  edge=edge+" "+r 
  count=count+1
 else:
  print("edge:",edge)
  edge=r
  count=1
print("edge:",edge)
print("Distance of MST: " + str(distance))
