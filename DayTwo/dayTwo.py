# Imaan Saye: AoC Day Two
# Start Time: 3 Dec  22:13 
# Today I learn RegEx!
# UPDATE: Learnt RegEx succesfully! 

import re
def part1():
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

# Part Two --------------------------
# Aside: There should be a more efficient way to check the maxes
def getmax(grp):
        biggestboy = 0
        
        #x = re.findall("ai", txt)
        print(grp)
        for i in grp:
            #biggestboy = int(i) if (int(i) > biggestboy) else biggestboy
            checker = int(i)
            if checker > biggestboy:
                biggestboy = checker
        #print("max here: ",biggestboy)
        return biggestboy
        
def part2():
    green = r'(\d+(?= green))'
    red = r'(\d+(?= red))'
    blue = r'(\d+(?= blue))'

    power = 0
    
    with open("input.txt") as myfile:
        for line in myfile:
            temp= (getmax(re.findall(green, line)) * getmax(re.findall(red, line))  * getmax(re.findall(blue, line)))
            power+=temp
        #    print(temp)
    print(power)
    
def main():
    part1()
    #part2()
    
if __name__ == "main":
    main()