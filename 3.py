import re     # regex package
import sys    # system package
import math   

# advent of code 2023 day 3

result = 0

# Read command line args

if len(sys.argv)==2:
    filename = sys.argv[1]
    inputFile = open(filename, "r")
else:
    print ("usage: " + sys.argv[0] + " <input filename>")
    sys.exit(1)

def extractNumbersIndices(inString):
    currentNum ="";
    numbers = []
    indices = []
    lengths = []
    for i, char in enumerate(inString):
        if char.isdigit():
            currentNum += char
        elif currentNum:
            try:
                num = int(currentNum)
                numbers.append(num)
                indices.append(i - len(currentNum))
                lengths.append(len(currentNum))
            except ValueError:
                pass
            currentNum = ''

    # Check for the last number in case the line ends with a number
    if currentNum:
        try:
            num = int(currentNum)
            numbers.append(num)
            indices.append(len(inString) - len(currentNum))
            lengths.append(len(currentNum))
        except ValueError:
            pass
    return numbers, indices, lengths

def extractSymbolsIndices(inString):
    indices = [(index, char) for index, char in enumerate(inString) if char in "!\"#$%&'()*+,-/:;<=>?@[\\]^_`{|}~"  and char != '.']
    return indices

        
#read the lines
lines = inputFile.readlines()

# do first line (special case)
currentIndex=0
previous = None
current = lines[currentIndex]
next = lines[currentIndex+1]
maxLine= len(lines) - 1

#print("previous=", previous)
#print("current=",current)
#print("next=", next)
#print("maxLine=", maxLine)

##### assuming that every lineis same length?!!!



numbersP = []
numLensP = []
indicesP = []
symbolsP = []
numbersC = []
numLensC = []
indicesC = []
symbolsC = []
numbersN = []
numLensN = []
indicesN = []
symbolsN = []

numbersC, indicesC, numLensC = extractNumbersIndices(current)
symbolsC = extractSymbolsIndices(current)
numbersN, indicesN, numLensN = extractNumbersIndices(next)
symbolsN = extractSymbolsIndices(next)

## work out if any adjacent to each number    
indicesCLen = len(indicesC) 
symbolsCLen = len(symbolsC) 
symbolsNLen = len(symbolsN) 

print("first Lines!!!")
## for first line we only care about the current and next, there is no previous!
for n in range(0, indicesCLen, 1):           
    if (n < symbolsCLen):
        if (symbolsC[n][0] <= indicesC[n]+numLensC[n]+1) and (symbolsC[n][0] >= indicesC[n]-numLensC[n]-1):
            print ("Found part with adjacent symbol=", symbolsC[n], " ind=",indicesC[n], " num=",numbersC[n])
            result += numbersC[n]
    if (n < symbolsNLen):
        if (symbolsN[n][0] <= indicesC[n]+numLensC[n]+1) and (symbolsN[n][0] >= indicesC[n]-numLensC[n]-1):
            print ("Found part with adjacent symbol next line=", symbolsN[n], " ind=",indicesC[n], " num=",numbersC[n])
            result += numbersC[n]
            
print("numbersP:", numbersP)
print("numLensP:", numLensP)
print("indicesP:", indicesP)
print("symbolsP:", symbolsP)
print("numbersC:", numbersC)
print("numLensC:", numLensC)
print("indicesC:", indicesC)
print("symbolsC:", symbolsC)
print("numbersN:", numbersN)
print("numLensN:", numLensN)
print("indicesN:", indicesN)    
print("symbolsN:", symbolsN)

print("middle Lines!!!")

for currentIndex in range(1, maxLine, 1):   
#if (1):
 #   currentIndex=1
    
    previous = lines[currentIndex-1]
    current = lines[currentIndex]
    next = lines[currentIndex+1]

    numbersP = numbersC
    indicesP = indicesC
    symbolsP = symbolsC
    numLensP = numLensC
    
    numbersC = numbersN
    indicesC = indicesN
    symbolsC = symbolsN
    numLensC = numLensN
    
    numbersN = []     ## clear the next before repopulating
    indicesN = []     ## clear the next before repopulating
    symbolsN = []     ## clear the next before repopulating
    numLensN = []     ## clear the next before repopulating
    numbersN, indicesN, numLensN = extractNumbersIndices(next)
    symbolsN = extractSymbolsIndices(next)

    print("numbersP:", numbersP)
    print("numLensP:", numLensP)
    print("indicesP:", indicesP)
    print("symbolsP:", symbolsP)
    print("numbersC:", numbersC)
    print("numLensC:", numLensC)
    print("indicesC:", indicesC)
    print("symbolsC:", symbolsC)
    print("numbersN:", numbersN)
    print("numLensN:", numLensN)
    print("indicesN:", indicesN)    
    print("symbolsN:", symbolsN) 
    
    ## work out if any adjacent to each number    
    indicesCLen = len(indicesC) 
    symbolsCLen = len(symbolsC) 
    symbolsPLen = len(symbolsP) 
    symbolsNLen = len(symbolsN) 
    
    print ("indicesCLen = ",indicesCLen)
    print ("symbolsCLen = ",symbolsCLen)

    
    for n in range(0, indicesCLen, 1):           
        for s in range(0,len(symbolsP),1):
             if (symbolsP[s][0] <= indicesC[n]+numLensC[n]+1) and (symbolsP[s][0] >= indicesC[n]-numLensC[n]-1):
                print ("Found part with adjacent symbol next line=", symbolsP[s], " ind=",indicesC[n], " num=",numbersC[n])
                result += numbersC[n]                   
        for s in range(0,len(symbolsC),1):
            if (symbolsC[s][0] <= indicesC[n]+numLensC[n]+1) and (symbolsC[s][0] >= indicesC[n]-numLensC[n]-1):
                print ("Found part with adjacent symbol=", symbolsC[s], " ind=",indicesC[n], " num=",numbersC[n])
                result += numbersC[n]
        for s in range(0,len(symbolsN),1):
            if (symbolsN[s][0] <= indicesC[n]+numLensC[n]+1) and (symbolsN[s][0] >= indicesC[n]-numLensC[n]-1):
                print ("Found part with adjacent symbol next line=", symbolsN[s], " ind=",indicesC[n], " num=",numbersC[n])
                result += numbersC[n]            
      

numbersP = numbersC
indicesP = indicesC
symbolsP = symbolsC
numLensP = numLensC
numbersC = numbersN
indicesC = indicesN
symbolsC = symbolsN
numLensC = numLensN      
## work out if any adjacent to each number    
indicesCLen = len(indicesC) 
symbolsCLen = len(symbolsC) 
symbolsPLen = len(symbolsP) 

print("Last Line!!!")

print("numbersP:", numbersP)
print("numLensP:", numLensP)
print("indicesP:", indicesP)
print("symbolsP:", symbolsP)
print("numbersC:", numbersC)
print("numLensC:", numLensC)
print("indicesC:", indicesC)
print("symbolsC:", symbolsC)

#deal with last line
for n in range(0, indicesCLen, 1):           
    if (n < symbolsPLen):        
         if (symbolsP[n][0] <= indicesC[n]+numLensC[n]+1) and (symbolsP[n][0] >= indicesC[n]-numLensC[n]-1):
            print ("Found part with adjacent symbol next line=", symbolsP[n], " ind=",indicesC[n], " num=",numbersC[n])
            result += numbersC[n]                   
    if (n < symbolsCLen):
        if (symbolsC[n][0] <= indicesC[n]+numLensC[n]+1) and (symbolsC[n][0] >= indicesC[n]-numLensC[n]-1):
            print ("Found part with adjacent symbol=", symbolsC[n], " ind=",indicesC[n], " num=",numbersC[n])
            result += numbersC[n]      

print (result)