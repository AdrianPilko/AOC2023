import re     # regex package
import sys    # system package
import math   

# advent of code 2023 day 3

# Read command line args
if len(sys.argv)==2:
    filename = sys.argv[1]
    inputFile = open(filename, "r")
else:
    print ("usage: " + sys.argv[0] + " <input filename>")
    sys.exit(1)

lines = inputFile.readlines()
result = 0

#process the lines
for line in lines:
                        
print (result)
    
    
