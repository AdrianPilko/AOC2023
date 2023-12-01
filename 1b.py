import re
import sys

# finds total of the first and last single digit in list like this
#two1nine
#eightwothree
#abcone2threexyz
#xtwone3four
#4nineeightseven2
#zoneight234
#7pqrstsixteen

def findFirstLastSpeltNumber(text, words_tuple):
    positions = []
    for word in words_tuple:
        pattern = re.escape(word)
        matches = list(re.finditer(pattern, text))
        if matches:
            positions.append((matches[0].start(), matches[-1].start() + len(word) - 1))
        else:
            positions.append((None, None))
    return positions

    
if len(sys.argv)==2:
    filename = sys.argv[1]
    inputFile = open(filename, "r")
else:
    print ("usage: " + sys.argv[0] + " <input filename>")
    sys.exit(1)

lines = inputFile.readlines()
total = 0
numbersSpelt=('one', 'two', 'three', 'four', 'five','six','seven','eight','nine')

for line in lines:
    firstDigitRE = re.search('[\d]',line)
    lastDigitRE = re.search('(\d)(?!.*\d)',line)
    speltPositions = findFirstLastSpeltNumber(line,numbersSpelt)
    numFirstRE = speltPositions[0]
    numLastRE = speltPositions[1]

    print(firstDigitRE)
    print(lastDigitRE)
    print(numFirstRE)
    print(numLastRE)
    
    # work out which one came first
    if (firstDigitRE and numFirstRE):    
        if (firstDigitRE.start() < numFirstRE.start()):
            concatd = firstDigitRE.group()
        else:
            if (numFirstRE.group() == 'one'): concatd = '1'
            if (numFirstRE.group() == 'two'): concatd = '2'
            if (numFirstRE.group() == 'three'): concatd = '3'
            if (numFirstRE.group() == 'four'):concatd = '4'
            if (numFirstRE.group() == 'five'):concatd = '5'
            if (numFirstRE.group() == 'six'): concatd = '6'
            if (numFirstRE.group() == 'seven'): concatd = '7'
            if (numFirstRE.group() == 'eight'): concatd = '8'
            if (numFirstRE.group() == 'nine'): concatd = '9'
    elif firstDigitRE:
        concatd = firstDigitRE.group()
    elif numFirstRE:
        if (numFirstRE.group() == 'one'): concatd = '1'
        if (numFirstRE.group() == 'two'): concatd = '2'
        if (numFirstRE.group() == 'three'): concatd = '3'
        if (numFirstRE.group() == 'four'):concatd = '4'
        if (numFirstRE.group() == 'five'):concatd = '5'
        if (numFirstRE.group() == 'six'): concatd = '6'
        if (numFirstRE.group() == 'seven'): concatd = '7'
        if (numFirstRE.group() == 'eight'): concatd = '8'
        if (numFirstRE.group() == 'nine'): concatd = '9'
        
    # work out which one came last
    if (lastDigitRE and numLastRE):    
        if (lastDigitRE.start() < numLastRE.start()):
            concatd = lastDigitRE.group()
        else:
            if (numLastRE.group() == 'one'): concatd = '1'
            if (numLastRE.group() == 'two'): concatd = '2'
            if (numLastRE.group() == 'three'): concatd = '3'
            if (numLastRE.group() == 'four'):concatd = '4'
            if (numLastRE.group() == 'five'):concatd = '5'
            if (numLastRE.group() == 'six'): concatd = '6'
            if (numLastRE.group() == 'seven'): concatd = '7'
            if (numLastRE.group() == 'eight'): concatd = '8'
            if (numLastRE.group() == 'nine'): concatd = '9'
    elif lastDigitRE:
        concatd = lastDigitRE.group()
    elif numLastRE:
        if (numLastRE.group() == 'one'): concatd = '1'
        if (numLastRE.group() == 'two'): concatd = '2'
        if (numLastRE.group() == 'three'): concatd = '3'
        if (numLastRE.group() == 'four'):concatd = '4'
        if (numLastRE.group() == 'five'):concatd = '5'
        if (numLastRE.group() == 'six'): concatd = '6'
        if (numLastRE.group() == 'seven'): concatd = '7'
        if (numLastRE.group() == 'eight'): concatd = '8'
        if (numLastRE.group() == 'nine'): concatd = '9'
    total = int(concatd)+total                        
print (total)
    
    
