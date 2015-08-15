from sys import argv
import re
import sys
import math
import time

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

    total_distance = 0
    neighbor = list()
    tour = list()
    copyCities = dict(cities)
    # Assign source city
    for k in cities:
        current_city = cities[k]
        previous_city = cities[k]
        tour.append(k)
        break

    del cities[0]

    # Find closest neighbor for each city
    while len(cities) > 0:
        min = sys.maxint
        for i in cities:
            distance = calculate_distance(current_city, cities[i])
            if distance < min:
                neighbor = i
                min = distance

        # Update new total distance
        total_distance += min
        tour.append(neighbor)
        current_city = cities[neighbor]

        del cities[neighbor]

    newPath = []
    #count = 0
    change = True
    while change:
        change = False
        #count = count + 1
        
        dist =  totalDist(tour, copyCities)
        
        for i in range(1, len(tour) - 1):
            for j in range(i + 1, len(tour)):
                newPath = newRoute(tour, i, j)

                newDist = totalDist(newPath, copyCities)
                
                if newDist < dist:
                    del tour[:]
                    tour[:] = []
                    tour = newPath
                    change = True
    
    return dist,tour

array_w_identifier=[]
array_wo_identifier=[]
fileName = 'test-input-1.txt' #change this before submit test-input-7 tsp_example_1
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

#f2 = open(outFile,'w')
start = time.clock()
d, tour = greedy_tsp(maps)
end = time.clock()
print "Execution Time: ", end-start
#f2.write(str(d) + '\n')
#for i in tour:
    #f2.write(str(i) + '\n')
print d
#print tour
print len(tour)==len(set(tour)) #just to check if any city is visited twice
print len(tour)

#f2.close()
