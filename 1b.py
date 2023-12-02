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

number_value = None
last_value = None


def last_occurrence_pattern(pattern):
    return r'(?s)(?=.*' + pattern + ')(?!.*' + pattern + '.*)'

def create_last_occurrence_spelled_out_pattern(spelled_out_numbers):
    pattern_parts = [last_occurrence_pattern(re.escape(word)) for word in spelled_out_numbers.keys()]
    spelled_out_pattern_last = "|".join(pattern_parts)
    return spelled_out_pattern_last




def firstAndLast(text):    
    global last_value
    global number_value  
    
    # Define regex pattern for spelled-out numbers and digits
    spelled_out_numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Create a regex pattern to match spelled-out numbers or digits separately
    spelled_out_pattern_first = "|".join(r'{}'.format(re.escape(word)) for word in spelled_out_numbers.keys())
    digit_pattern_first = r'\d+'
    # Combine patterns for both spelled-out numbers and digits
    combined_pattern_first = "|".join([spelled_out_pattern_first, digit_pattern_first])
    # Find all matches in the text
    match_first = re.search(combined_pattern_first, text)

    # Create a regex pattern to match spelled-out numbers or digits separately
    spelled_out_pattern_last = create_last_occurrence_spelled_out_pattern(spelled_out_numbers)
    digit_pattern_last = '(\d)(?!.*\d)'
    # Combine patterns for both spelled-out numbers and digits
    combined_pattern_last = "|".join([spelled_out_pattern_last, digit_pattern_last])
    # Find all matches in the text
    match_last = re.search(combined_pattern_last, text)

    print(match_first)
    if match_first:
        matched_text = match_first.group()
        
        if matched_text.isdigit():
            number_value = int(matched_text)
        else:
            for word, digit in spelled_out_numbers.items():
                if matched_text == word:
                    number_value = int(digit)

    print(match_last)
    if match_last:
        matched_text = match_last.group()
        
        if matched_text.isdigit():
            last_value = int(matched_text)
        else:
            for word, digit in spelled_out_numbers.items():
                if matched_text == word:
                    last_value = int(digit)


#if len(sys.argv)==2:
#    filename = sys.argv[1]
#    inputFile = open(filename, "r")
#else:
 #   print ("usage: " + sys.argv[0] + " <input filename>")
#    sys.exit(1)

#lines = inputFile.readlines()
total = 0

#for line in lines:
line = "one2three4five"
print(line)
print(firstAndLast(line))
print ("first number = ", number_value);
print ("last number = ", last_value);
total += number_value
   
print ("total=", total)
    
    
