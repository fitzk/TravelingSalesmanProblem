from sys import argv
import re

array_w_identifier=[]
array_wo_identifier=[]
fileName = '../no_submit/tsp_example_1.txt' #change this before submit
if len(argv) > 1:
    script, filename = argv

outFile = fileName[:-4] + '.result'
try:
    with open(fileName) as f:
        for line in f:
            array_w_identifier.append([int(s) for s in line.split() if s.isdigit()])
except IOError as e:
    print 'Error in opening file '+ fileName
    sys.exit(-1)

f2 = open(outFile,'w')

for each in array_w_identifier:
    array_wo_identifier.append(each[1:])

for each in array_wo_identifier:
    print each
for each in array_wo_identifier:
    print each

# file reads in char by char
# need to figure out best way to group numbers
# and how the algorithms should take input


f2.close()
