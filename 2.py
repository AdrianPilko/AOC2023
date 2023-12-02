import sys

if len(sys.argv)==2:
    filename = sys.argv[1]
    inputFile = open(filename, "r")
else:
    print ("usage: " + sys.argv[0] + " <input filename>")
    sys.exit(1)

lines = inputFile.readlines()
total=0
game_number = 0;
##input_string = "Game 54: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

# Splitting the string after ":" and stripping unnecessary spaces
for input_string in lines:
    split_after_colon = input_string.split(':')
    if len(split_after_colon) == 2:
        game_number_from_file = ''.join(filter(str.isdigit, split_after_colon[0]))  # Extracting the game number
        game_number+=1
        data = split_after_colon[1].strip()
       
        # Splitting groups by semicolon
        groups = data.split(';')
        
        result = {"game_number": game_number, "colour_totals": {}}

        for group in groups:
            pairs = group.strip().split(',')
            for pair in pairs:
                split_pair = pair.strip().split()
                if len(split_pair) == 2:
                    key = int(split_pair[0])
                    colour = split_pair[1]
                    print("colour= ", colour, "key=", key)
                    if colour in result["colour_totals"]:
                        if (key >= result["colour_totals"][colour]):
                            result["colour_totals"][colour] = key #update max
                    else:
                        result["colour_totals"][colour] = key   # set first time
                    ## if any one colour total is > the max game not possible
                    #if colour in result["colour_max"]:
                    #    if (key >= result["colour_max"][colour]):
                    #       result["colour_max"][colour] = key
                    #    else:
                    ##       result["colour_max"][colour] = 0
                           
                        
        print(result)
        possible=1

        if result["colour_totals"]["red"] <= 12:
            print("game ", game_number_from_file, " ", game_number," possible with red ", result["colour_totals"]["red"])
        else:
            print("game ", game_number_from_file, " ", game_number," not possible with red ", result["colour_totals"]["red"])
            possible=0
            
        if result["colour_totals"]["green"] <= 13:
            print("game ", game_number_from_file, " ", game_number," possible with green ", result["colour_totals"]["green"])
        else:
            possible=0
            print("game ", game_number_from_file, " ", game_number," not possible with green ", result["colour_totals"]["green"])
            
        if result["colour_totals"]["blue"] <= 14:
            print("game ", game_number_from_file, " ", game_number," possible with blue")
        else:
            print("game ", game_number_from_file, " ", game_number," not possible with blue ", result["colour_totals"]["blue"])
            possible=0
        if possible:
            print("game ", game_number_from_file, " ", game_number," was possible ", result["colour_totals"]["blue"])
            total=total+int(game_number)
        print("running total=", total)
print(total)


