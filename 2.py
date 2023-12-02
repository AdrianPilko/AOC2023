
input_string = "game 1: 3 red, 5 blue, 7 green, 6 red, 2 green, 7 red"
total=0

# Splitting the string after ":" and stripping unnecessary spaces
split_after_colon = input_string.split(':')
if len(split_after_colon) == 2:
    game_number = split_after_colon[0].split()[-1]  # Extracting the game number
    data = split_after_colon[1].strip()

    # Splitting pairs by comma
    pairs = data.split(',')
    
    result = {"game_number": game_number, "color_totals": {}}

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
    print("game was possible")
    total=total+possible
print(total)

