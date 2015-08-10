######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 4                                          #
# File:           TSP.py                                             #
# Description:    To solve travelling salesman problem using greedy  #
#                 algorithm, will not give optimal solution	         #
######################################################################

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
    return nearest_int(math.sqrt((c1[1] - c2[1])**2 + (c1[2] - c2[2])**2))

# Finds shortest tour using a greedy algorithm
def greedy_tsp(cities):
    total_distance = 0
    neighbor = list()
    tour = list()

    # Assign source city
    current_city = cities[0]
    previous_city = cities[0]
    tour.append(cities[0][0])
    
    del cities[0]

    # Find closest neighbor for each city
    while len(cities) > 0:
        min = sys.maxint
        for i in xrange(0, len(cities)):
            distance = calculate_distance(current_city, cities[i])
            if distance < min:
                neighbor = i
                min = distance

        # Update new total distance
        total_distance += min
        tour.append(cities[neighbor][0])
        current_city = cities[neighbor]
        
        del cities[neighbor]

    # Add distance between previous city to current city
    distance_between = calculate_distance(current_city, previous_city)
    total_distance = total_distance + distance_between
    
    return total_distance, tour

array_w_identifier=[]
array_wo_identifier=[]
fileName = 'tsp_example_1.txt' #default file name if no file name is given in argument
if len(sys.argv) > 1:
	fileName = sys.argv[1]

outFile = fileName + '.tour'
try:
    with open(fileName) as f:
        for line in f:
            array_w_identifier.append([int(s) for s in line.split() if s.isdigit()])
except IOError as e:
    print 'Error in opening file '+ fileName
    sys.exit(-1)

f2 = open(outFile,'w')

d, tour = greedy_tsp(array_w_identifier)
f2.write(str(d) + '\n')
for i in tour:
    f2.write(str(i) + '\n')
print d
#print tour
print len(tour)==len(set(tour)) #just to check if any city is visited twice
print len(tour)

f2.close()
