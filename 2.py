import sys

if len(sys.argv)==2:
    filename = sys.argv[1]
    inputFile = open(filename, "r")
else:
    print ("usage: " + sys.argv[0] + " <input filename>")
    sys.exit(1)

lines = inputFile.readlines()
total=0
##input_string = "Game 54: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

# Splitting the string after ":" and stripping unnecessary spaces
for input_string in lines:
    split_after_colon = input_string.split(':')
    if len(split_after_colon) == 2:
        game_number = ''.join(filter(str.isdigit, split_after_colon[0]))  # Extracting the game number
        data = split_after_colon[1].strip()
       
        # Splitting groups by semicolon
        groups = data.split(';')
        
        result = {"game_number": game_number, "color_totals": {}}

        for group in groups:
            pairs = group.strip().split(',')
            for pair in pairs:
                split_pair = pair.strip().split()
                if len(split_pair) == 2:
                    key = int(split_pair[0])
                    color = split_pair[1]
                    if color in result["color_totals"]:
                        result["color_totals"][color] += key
                    else:
                        result["color_totals"][color] = key

        possible=1

        if result["color_totals"]["red"] < 12:
            print("game possible with red")
        else:
            print("game not possible with red")
            possible=0
            
        if result["color_totals"]["green"] < 13:
            print("game possible with green")
        else:
            possible=0
            print("game not possible with green")
            
        if result["color_totals"]["blue"] < 14:
            print("game possible with blue")
        else:
            print("game not possible with blue")
            possible=0
        print("game ", result["game_number"][0], " was possible")
        total=total+possible
print(total)


