import re
import sys

# fins total of the first and last single digit in list like this
#1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet

if len(sys.argv)==2:
    filename = sys.argv[1]
    inputFile = open(filename, "r")
else:
    print ("usage: " + sys.argv[0] + " <input filename>")
    sys.exit(1)

lines = inputFile.readlines()
total = 0

for line in lines:
    first = re.search('[\d]',line)
    last = re.search('(\d)(?!.*\d)',line)
    concatd = first.group()+last.group()
    total = int(concatd)+total                        
print (total)
    
    
