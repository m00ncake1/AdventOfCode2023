# Imaan Saye: AoC Day Two
# Start Time: 3 Dec  22:13 
# Today I learn RegEx!

import re

# 12 red, 13 green, 14 blue
pattern = r'(1[3-9]|[2-9]\d+)(?= red)|(1[4-9]|[2-9]\d+)(?= green)|(1[5-9]|[2-9]\d+)(?= blue)'


game = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
total = 0
with open("input.txt") as myfile:
    for line in myfile:
        match = re.search(pattern,line)
        if not bool(match):
            #print(line)
            #print(total)
            #total += int(line[line.index(" "):line.index(":")]) #gameID at index 5
            add =re.search("(?<=Game )\d+", line).group()
            total += int(add)
        else:
            print(line)
            
            
print(total)