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

        
result = 0

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


#for currentIndex in range(1, maxLine, 1):   
if (1):
    currentIndex=1
    
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
    indicesCLen = len(indicesC) - 1
    symbolsCLen = len(symbolsC) - 1
    symbolsPLen = len(symbolsP) - 1
    symbolsNLen = len(symbolsN) - 1
    
    for n in range(1, indicesCLen, 1):           
        if (n < symbolsPLen):        
             if (symbolsP[n][0] <= indicesC[n]+numLensC[n]+1) and (symbolsP[n][0] >= indicesC[n]-numLensC[n]-1):
                print ("Found part with adjacent symbol next line=", symbolsP[n], " ind=",indicesC[n], " num=",numbersC[n])
                result += numbersC[n]    
        if (n < symbolsCLen):
            if (symbolsC[n][0] <= indicesC[n]+numLensC[n]+1) and (symbolsC[n][0] >= indicesC[n]-numLensC[n]-1):
                print ("Found part with adjacent symbol=", symbolsC[n], " ind=",indicesC[n], " num=",numbersC[n])
                result += numbersC[n]
        if (n < symbolsNLen):
            if (symbolsN[n][0] <= indicesC[n]+numLensC[n]+1) and (symbolsN[n][0] >= indicesC[n]-numLensC[n]-1):
                print ("Found part with adjacent symbol next line=", symbolsN[n], " ind=",indicesC[n], " num=",numbersC[n])
                result += numbersC[n]
            
    numbersP = numbersC
    indicesP = indicesC
    numLensP = numLensC
    numbersC = numbersN
    indicesC = indicesN
    numLensC = numLensN
        
    
    #print("previous=", previous)
    #print("current=",current)
    #print("next=", next)   







              
print (result)