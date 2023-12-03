import re     # regex package
import sys    # system package
import math   

# advent of code 2023 day 3
runOnPc  = False
lines = " "
# Read command line args
if (runOnPc == True):
    if len(sys.argv)==2:
        filename = sys.argv[1]
        inputFile = open(filename, "r")
        lines = inputFile.readlines()
    else:
        print ("usage: " + sys.argv[0] + " <input filename>")
        sys.exit(1)
else:
    lines=("467..114..",
           "...*......",
           "..35..633.",
           "......#...",
           "617*......",
           ".....+.58.",
           "..592.....",
           "......755.",
           "...$.*....",
           ".664.598..")
result = 0

#process the lines
lnc=0   #current line
lnn=1   #next
maxl=lines.len()

while lnn<maxl:
   line1=lines[lnc]
   nums= [int(s) for s in line1.split() if s.isdigit()]
 
   print(line1)
   priny(nums)     
   lnn+=1   
              
print (result)
    
    
