import sys
import re
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