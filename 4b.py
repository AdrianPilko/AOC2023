import re # regex package
import sys # system package
import math   

# advent of code 2023 day 3

lines = " "
# Read command line args
runOnPc = False
if (runOnPc == True):
    if len(sys.argv)==2:
        filename = sys.argv[1]
        inputFile = open(filename, "r")
        lines = inputFile.readlines()
    else:
        print ("usage: " + sys.argv[0] + " <input filename>")
        sys.exit(1)
else:
    lines=("Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
result = 0

#process the lines

## for the second part we need to build a new list of cards based on the current lines
matchNum = 100
#index to start back from if a win happens and entries added
startFrom = 0
while matchNum !=0:
    lines = tuple(lines[i] for i in range(startFrom, len(lines)))

    # Iterate over the new tuple with the same indices as the original
    for index, line in enumerate(lines, start=startFrom):
       startFrom = 0
       print(f"Line {index}: {line}")
       linesp=line.split("|")
       #print(linesplit) # this is a list now so camt split
       fir=linesp[0]   
       sec=linesp[1]
       cardNum=fir.split(":")[0]   # might not need this
       cardNum=cardNum.split(" ")[1]
       fir=fir.split(":")[1]
       fir= [int(num) for num in fir.split() if num.isdigit()]
       print(fir)
       sec= [int(num) for num in sec.split() if num.isdigit()]
       print(sec)

       for f in fir:
          for w in sec:
            #print("w=",w, "f=",f)
            if f==w: 
               #we've won, increment a win counter
               matchNum+=1;           
       ## we've processed the line and have matchNum wins so keep a list of how many rows to replicate
       

       #now append the next matchNum lines
       print("linesBefore=",lines)
       # Get the lines to replicate (excluding the current line)
       linesToRep = lines[index+1 : index + matchNum + 1]
       # Create a new tuple by replicating the lines
       lines = lines + linesToRep
       
       if matchNum != 0: 
            startFrom = index+1
            break
       
       print("linesAfter=",lines)
       matchNum = 0       # reset matchNum

result = len(lines)
print (result)
    