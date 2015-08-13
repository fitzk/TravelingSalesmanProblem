from sys import argv
import re
import sys
import math

# Rounds number to the nearest integer
def nearest_int(num):
    if (num > 0):
        return int(num + .5)
    else:
        return int(num - .5)

# Calculates distance between city 1 and city 2
def calculate_distance(c1, c2):
    return nearest_int(math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2))

#calculate distance of a path
def totalDist(path, cities):
    finalDistance = 0
    for i in range(1,len(path)):
        finalDistance += calculate_distance(cities[path[i-1]], cities[path[i]])
    finalDistance += calculate_distance(cities[path[0]], cities[path[len(path) - 1]])
    return finalDistance

def newRoute(path, i, j):
    newRoute = []
    
    for x in range(0, i):
        newRoute.append(path[x])
    y = j
    while j > i - 1:
        newRoute.append(path[j])
        j = j - 1
    for i in range(y + 1, len(path)):
        newRoute.append(path[i])
    return newRoute

# Finds shortest tour using a greedy algorithm
def greedy_tsp(cities):

    MSTedges = list()
   
    keyy = {}
    finalPath = []
    parent = {}
    for k in cities:
        finalPath.append(k)

    newPath = []
    count = 0
    change = True
    
    while change:
        change = False
        count = count + 1
        
        dist =  totalDist(finalPath, cities)
        
        for i in range(1, len(finalPath) - 1):
            for j in range(i + 1, len(finalPath)):
                newPath = newRoute(finalPath, i, j)
                
                newDist = totalDist(newPath, cities)
                
                if newDist < dist:
                    del finalPath[:]
                    finalPath[:] = []
                    finalPath = newPath
                    change = True
    
    return dist,finalPath

array_w_identifier=[]
array_wo_identifier=[]
fileName = 'tsp_example_1.txt' #change this before submit test-input-7 tsp_example_1
if len(sys.argv) > 1:
    fileName = sys.argv[1]

outFile = fileName + '.result'
maps = {}
try:
    with open(fileName) as f:
        for line in f:
            for s in line.split(): 
                if s.isdigit():
                    array_w_identifier.append(int(s)) 
            maps[array_w_identifier[0]] = array_w_identifier[1:]
            del array_w_identifier[:]
            array_w_identifier[:] = []
except IOError as e:
    print 'Error in opening file '+ fileName
    sys.exit(-1)

f2 = open(outFile,'w')

#print array_w_identifier
d, tour = greedy_tsp(maps)
print d
print tour
print len(tour)==len(set(tour)) #just to check if we visited any city twice
print len(tour)
f2.close()
