from sys import argv
import re

array=[]
fileName = '../no_submit/tsp_example_1.txt' #change this before submit
if len(argv) > 1:
    script, filename = argv

outFile = fileName[:-4] + '.result'
try:
    f = open(fileName)
    array = f.read()
except IOError as e:
    print 'Error in opening file '+ fileName
    sys.exit(-1)

f2 = open(outFile,'w')


int_array=[]
for line in array:
    if re.findall('\d+\',line)
        
for intz in int_array:
    print intz
f2.close()
