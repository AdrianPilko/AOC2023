import re # regex package
import sys # system package
import math   

# advent of code 2023 day 3
runOnPc = True
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
    lines=("Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
result = 0

#process the lines
#print(lines)
for line in lines:
   linesp=line.split("|")
   #print(linesplit) # this is a list now so camt split
   fir=linesp[0]
   sec=linesp[1]
   fir=fir.split(":")[1]
   fir= [int(num) for num in fir.split() if num.isdigit()]
   print(fir)
   sec= [int(num) for num in sec.split() if num.isdigit()]
   print(sec)
   win=0
   num=0
   for f in fir:
      for w in sec:
        #print("w=",w, "f=",f)
        if f==w: 
           if num==0:
              num=1
              print("found first win ", f," ", num)
           else:
               num=num*2
               print("found win ",f," ", num)
              
   print("win for row=", num)
   result+=num
              
print (result)
    