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
    indices = [(index, char) for index, char in enumerate(inString) if char in "*"  and char != '.']
    return indices

totalratio = 0

def maintainGearCentreMatrix(number, posx, posy, numberAdjacentToGear)
     #   numberAdjacentToGear=[(0,0,0),
     #                         (0,0,0),
     #                         (0,0,0)]
     
     
    return numberAdjacentToGear
    
# this checks for symbols in the pre next (if args Pre and Next True, and current always
def checkSymbols(CheckPre,CheckNext, symbolsP, symbolsN, indicesC, symbolsC, numLensC, numbersC) :
    ratio = 0
    
    ## what could do is to maintain a window of 3 by 3 surrounding the *     
    numberAdjacentToGear=[(0,0,0),
                          (0,0,0),
                          (0,0,0)]
    
    
    
    print("symbolsP:", symbolsP)
    print("numbersC:", numbersC)
    print("numLensC:", numLensC)
    print("indicesC:", indicesC)
    print("symbolsC:", symbolsC)
    print("symbolsN:", symbolsN)
    
    x = 0
    y = 0
    
    ## these loops/logic finds * only
    if CheckPre==True:
        for s in range(0,len(symbolsP),1):
             for n in range(0,len(indicesC),1):             
                if  (symbolsP[s][0] <= indicesC[n]+numLensC[n]) and (symbolsP[s][0] >= indicesC[n]-1):
                    print ("previous line=", symbolsP[s], " ind=",indicesC[n], " num=",numbersC[n])
                    numberAdjacentToGear = maintainGearCentreMatrix(numbersC[n], , ,numberAdjacentToGear)
    for s in range(0,len(symbolsC),1):
        for n in range(0,len(indicesC),1):         
            if  (symbolsC[s][0] <= indicesC[n]+numLensC[n]) and (symbolsC[s][0] >= indicesC[n]-1):
                print ("current line=", symbolsC[s], " ind=",indicesC[n], " num=",numbersC[n])
    if CheckNext==True:                
        for s in range(0,len(symbolsN),1):
            for n in range(0,len(indicesC),1):
                if (symbolsN[s][0] <= indicesC[n]+numLensC[n]) and (symbolsN[s][0] >= indicesC[n]-1):
                    print ("next line=", symbolsN[s], " ind=",indicesC[n], " num=",numbersC[n])

    return ratio
        
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
totalratio+=checkSymbols(False,True, symbolsP, symbolsN, indicesC, symbolsC, numLensC, numbersC)    


for currentIndex in range(1, maxLine, 1):   
    print("middle Lines!!! ", currentIndex)   
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

    ## work out if any adjacent to each number    
    indicesPLen = len(indicesP) 
    indicesCLen = len(indicesC) 
    indicesNLen = len(indicesN) 
    symbolsCLen = len(symbolsC) 
    symbolsPLen = len(symbolsP) 
    symbolsNLen = len(symbolsN) 
    
    #print ("indicesCLen = ",indicesCLen)
    #print ("symbolsCLen = ",symbolsCLen)
    
    totalratio+=checkSymbols(True,True, symbolsP, symbolsN, indicesC, symbolsC, numLensC, numbersC)    

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

#deal with last line  
totalratio+=checkSymbols(True,False, symbolsP, symbolsN, indicesC, symbolsC, numLensC, numbersC)    
  
print (totalratio)