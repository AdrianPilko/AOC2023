import re
import sys

def firstAndLast(text):
    first_digit = None
    last_digit = None
    spelled_out_numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Extract sequences of characters using regex
    sequences = re.findall(r'\d+|[a-zA-Z]+', text)
    for sequence in sequences:
        print(sequence)
        if sequence.isdigit():
            rightmost_digit = int(str(sequence[-1]))  # Get the rightmost digit            
            print(rightmost_digit)
            if first_digit is None:
                first_digit = int(sequence)                
            #last_digit = int(sequence)
            last_digit = rightmost_digit
            
        elif sequence.lower() in spelled_out_numbers:
            digit = int(spelled_out_numbers[sequence.lower()])
            if first_digit is None:
                first_digit = digit
            last_digit = digit

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
    print(firstAndLast(line))
    first_digit, last_digit = firstAndLast(line)
    if (first_digit!=None):
        print ("first number = ", first_digit);
        total += first_digit
    if (last_digit!=None):    
        print ("last number = ", last_digit);
        total += last_digit
   
print ("total=", total)
    
