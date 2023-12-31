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

def maintainGearCentreMatrix(number, posx, posy, numberAdjacentToGear):
     #   numberAdjacentToGear=[(0,0,0),
     #                         (0,0,0),
     #                         (0,0,0)]
     
     
    return numberAdjacentToGear
    
# this checks for symbols in the pre next (if args Pre and Next True, and current always
def checkSymbols(CheckPre,CheckNext, 
                 numbersP, numbersC, numbersN, 
                 indicesP, indicesC, indicesN, 
                 numLensP, numLensC, numLensN, 
                 symbolsC):
    ratio = 0
    
    ## what could do is to maintain a window of 3 by 3 surrounding the *     
    numberAdjacentToGear=[(0,0,0),
                          (0,0,0),
                          (0,0,0)]
    
    
    
    # print("numbersP:", numbersP)
    # print("numLensP:", numLensP)
    # print("indicesP:", indicesP)
    # print("symbolsP:", symbolsP)
    
    # print("numbersC:", numbersC)
    # print("numLensC:", numLensC)
    # print("indicesC:", indicesC)
    # print("symbolsC:", symbolsC)

    # print("numbersN:", numbersN)
    # print("numLensN:", numLensN)
    # print("indicesN:", indicesN)
    # print("symbolsN:", symbolsN)
    
    x = 0
    absDistAlongLine = 0
    
    gearNum = [0,0]
    gearPos = [0,0]
    found = 0
    
    ## these loops/logic finds * only
    
    
    maxSymCurrent = len(symbolsC)
   # maxNum = len(numbersC)
   # if (CheckPre == True) and (len(numbersP) > maxNum):  maxNum = len(numbersP)
   # if (CheckNext == True) and (len(numbersN) > maxNum):   maxNum = len(numbersN)
    
    foundNumber = 0
    gearFound = 0;
    
    for s in range(0,maxSymCurrent,1):
        #for n in range(0,maxNum,1):         
           # if s < len(symbolsC):
                if  (symbolsC[s]):
                    print ("found gear in current line=", symbolsC[s])
                    gearFound += 1 
                    ## we found a gear in current line we now need to check for numbers:
                    ## in next line adjacent to this or current or previous (controled by CheckPre and CheckNext
                    # if n+1 < len(indicesC):
                        # print("checking for numbers adjacent current line")
                        # if (indicesC[n+1] == indicesC[n]+numLensC[n]+1):
                            # ratio += numbersC[n] * numbersC[n+1]
                            # print("FOUND on current line ")
                        # else:
                            # print("No adjacent on current line")
                    # if (CheckPre == True):
                        # print("checking for numbers adjacent prev line")
                        # if n < len(indicesP):
                            # if (symbolsC[s][0] <= indicesP[n]+numLensP[n]) and (symbolsC[s][0] >= indicesP[n]-1):
                                # foundNumber = numbersP[n]
                                # print("FOUND on prev line ", indicesP[n])
                            # else:
                                # print("No adjacent on prev line ", indicesP[n])                                
                        # else:
                            # print("Not checked Pre")
                    # if (CheckNext == True):
                        # if n < len(indicesN):
                            # print("checking for numbers adjacent next line")
                            # if (symbolsC[s][0] <= indicesN[n]+numLensN[n]) and (symbolsC[s][0] >= indicesN[n]-1):
                                # ratio += numbersN[n] * foundNumber
                                # print("FOUND on next line ", indicesN[n])
                            # else:
                                # print("No adjacent on next line ", indicesN[n])                                                                
                        # else:
                            # print("Not checked Next")  
    return gearFound

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

test= False
# test ##################################
if (test == True):
    line0="467..114.."  # none only count the ones from second line if no gears on first
    line1="...*..*..."  # 467*35 +114*633 = 88507    got correct answer
    line2="..35*633.."  # 35*633 +35*43 + 43*633 = 50879 was getting 44310,  6569 too few
    line3="....*43*.."  # none                     total = 139386  (was getting 132817
    numbersP, indicesP, numLensP = extractNumbersIndices(line0)
    symbolsP = extractSymbolsIndices(line0)
    numbersC, indicesC, numLensC = extractNumbersIndices(line1)
    symbolsC = extractSymbolsIndices(line1)
    numbersN, indicesN, numLensN = extractNumbersIndices(line2)
    symbolsN = extractSymbolsIndices(line2)
    totalratio=0
    totalratio+=checkSymbols(True, True, 
                     numbersP, numbersC, numbersN, 
                     indicesP, indicesC, indicesN, 
                     numLensP, numLensC, numLensN, 
                     symbolsC)

    numbersP, indicesP, numLensP = extractNumbersIndices(line1)
    symbolsP = extractSymbolsIndices(line0)
    numbersC, indicesC, numLensC = extractNumbersIndices(line2)
    symbolsC = extractSymbolsIndices(line1)
    numbersN, indicesN, numLensN = extractNumbersIndices(line3)
    symbolsN = extractSymbolsIndices(line2)

    totalratio+=checkSymbols(True, True, 
                     numbersP, numbersC, numbersN, 
                     indicesP, indicesC, indicesN, 
                     numLensP, numLensC, numLensN, 
                     symbolsC)
    print(totalratio)
    print("DONE SIMPLE TEST EXITTING")
    sys.exit(0)
##################################
        
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
totalratio+=checkSymbols(False,True, 
                 numbersP, numbersC, numbersN, 
                 indicesP, indicesC, indicesN, 
                 numLensP, numLensC, numLensN, 
                 symbolsC)


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
    
    totalratio+=checkSymbols(True,True, 
                 numbersP, numbersC, numbersN, 
                 indicesP, indicesC, indicesN, 
                 numLensP, numLensC, numLensN, 
                 symbolsC)

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
totalratio+=checkSymbols(True,False, 
                 numbersP, numbersC, numbersN, 
                 indicesP, indicesC, indicesN, 
                 numLensP, numLensC, numLensN, 
                 symbolsC)
  
print (totalratio)
