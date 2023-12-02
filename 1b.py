import re
import sys

def firstAndLast(text):
    first_digit_spelt = None
    last_digit_spelt = None
    first_digit_num = None
    last_digit_num = None
    first_digit = -1
    last_digit = -1
    spelled_out_numbers = {
            'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
            }
    numbers = {'1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
            }


    s = text
    lastResultPos = -1
    speltResultPos = 100000
    digitResultPos = 100000
## look from start of line for first number
    #print("finding spelt nums from start")
    for numstr in spelled_out_numbers:
        resultPos = s.find(numstr)
        #print(resultPos," ",  lastResultPos, " ", numstr) 
        if resultPos >=0 and resultPos < speltResultPos:
           first_digit_spelt=int(spelled_out_numbers[numstr])
           #print("found number as word=", resultPos, " ", numstr)
           lastResultPos = resultPos
           speltResultPos = resultPos
    #print("found first digit as word=" ,first_digit_spelt, " pos=",speltResultPos) 
    #print("finding digit nums from start")
    lastResultPos = -1
    for numstr in numbers:
        resultPos = s.find(numstr)
        #print(resultPos, " ", numstr)
        if resultPos >=0 and resultPos < digitResultPos:
           first_digit_num=int(numbers[numstr])
           #print("found number as digit=", numstr," ", resultPos)
           lastResultPos = resultPos
           digitResultPos = resultPos
    #print("found first digit=" ,first_digit_num, " pos=",digitResultPos) 

    if speltResultPos < digitResultPos:
        first_digit=first_digit_spelt
    else:
        first_digit=first_digit_num

    print("FIRST_DIGIT=",first_digit)
## now look from end of line using find
    #print("finding spelt from end back")
    lastResultPos = -1
    speltResultPos = -1
    digitResultPos = -1
    for numstr in spelled_out_numbers:
        resultPos = s.find(numstr) 
        #print(resultPos," ",  lastResultPos, " ", numstr) 
        if resultPos >=0 and resultPos > speltResultPos:
           last_digit_spelt=int(spelled_out_numbers[numstr])
           #print("found number as word pos=", resultPos, " num=", numstr)
           lastResultPos = resultPos
           speltResultPos = resultPos
    #print("found last digit as word=" ,last_digit_spelt) 
    #print("finding digit nums from end")
    lastResultPos = -1
    for numstr in numbers:
        resultPos = s.find(numstr)
        #print(resultPos," ",  lastResultPos, " ", numstr) 
        if resultPos >=0 and resultPos > digitResultPos:
           last_digit_num=int(numbers[numstr])
           #print("found number as digit, pos=", resultPos, " num=", numstr)
           lastResultPos = resultPos
           digitResultPos = resultPos

    #print("found last digit=" ,last_digit_num) 
    if speltResultPos > digitResultPos:
        last_digit=last_digit_spelt
    else:
        last_digit=last_digit_num

    print("LAST_DIGIT=",last_digit)
    return first_digit, last_digit


#test
#text = "one2three4five"
#first_digit, last_digit = find_first_last_digits(text)
#print("First digit or spelled-out number:", first_digit)
#print("Last digit or spelled-out number:", last_digit)

if len(sys.argv)==2:
    filename = sys.argv[1]
    inputFile = open(filename, "r")
else:
    print ("usage: " + sys.argv[0] + " <input filename>")
    sys.exit(1)

lines = inputFile.readlines()
total = 0
for line in lines:
    print(line)
    first_digit, last_digit = firstAndLast(line)
    if ((first_digit!=None) and (last_digit!=None)):    
        total += (first_digit*10) + last_digit
        print ("added ", (first_digit*10) + last_digit)

print ("total=", total)

