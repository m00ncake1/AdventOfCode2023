# DayOne AoC Part 1 and 2
# Learnt: hey, things would be easier with RegEx!
# Unfortuantely: I am sleepy
# Experience gained: Read instructions. Do exactly what is asked. Lest you do part two during part 1,
# ... and wonder why it's not accepting your very correct solution.


names = {
    'zero': "0",
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9"
}
    
            
#word = "4threethreegctxg3dmbm1"

def solvePart1(word):
    
    container = ""
    #for key, value in names.items():
    #   word = word.replace(key, value)
    #   print(word, sep = ",")
        
    for char in word:
        if char.isdigit():
            container += char

    return int(container[0]+container[-1])

def solvePart2(word):
    container = ""
    for key, value in names.items():
       word = word.replace(key, key[0]+value+key[-1])
       #print(word)
        
    for char in word:
        if char.isdigit():
            container += char

    return int(container[0]+container[-1])


# driver code
# better put into a main function so i have done so

def main():
    total = 0
    new = 0

    with open("input1.txt") as my_file:
        lineNo = 1
        
        for line in my_file:
            
            #new = solvePart1(line)
            new = solvePart2(line)
            total += new
            
            print(lineNo, ": ",new)
            #print("new total: ", total)
            lineNo+=1
            
    print(total)

if __name__ == "main":
    main()