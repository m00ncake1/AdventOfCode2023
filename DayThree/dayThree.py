# Imaan Sayed's Day Three solution
# Update: Will use regex for matching indices, combined with 2D arrays :)
# Life update: I got accepted to an internship today!

import re
 
pattern =(r'\d+')


# getting the match of the string
#search_pattern = re.search(pattern)

#c get indices of match and check, if x[[y]] (i.e. whole line is x, inner is y):
# start-1,end+1: for x
# for x-1: from start-1 TO end+1
# for x+1: from start-1 TO end+1


schematic = []

with open("input.txt") as myfile:
        for line in myfile:
            schematic.append(line.strip())
            
def part1(self): 
    grid = self.schematic
    
    # get special characters: anything non-alphanumeric
    specialz = (r'[^\.\d]')
    
    partSum = 0
    maxRows = len(grid)

    for row in range(maxRows):
        
        for match in re.finditer(pattern, grid[row]):
            
            # Get surrounding block for match (number in schematic)
            start = match.start()-1
            end =match.end()+1 # because exclusive upper, +1 to auto built in +1 
            
            # Adjust block for edge cases so still within bounds
            if (start<=-1): 
                start = 0
            if (end>=len(grid[row])):
                end = len(grid[row])-1
                
            if (row == 0): # only check same row and below
                block = grid[row][start:end]+ grid[row+1][start:end]
            elif (row == (maxRows-1) ): #only check same row and above
                block = grid[row][start:end]+ grid[row-1][start:end]
            else:
                block = grid[row][start:end] + grid[row-1][start:end] + grid[row+1][start:end]
            
            #print(block)
            
            # Check if valid, i.e. if symbol in block
            if (re.search(specialz, block)):
                partSum += int(match.group()) #match.group gets exact match from match object
            
    print(partSum)
   
# Get blocks with *, check if any NUMBERS in adjacent spaces
#def part2():
     #grid = self.schematic
    
# get special characters: anything non-alphanumeric
specialz = (r'[*]')
    
partMultiply = 0
grid = schematic
maxRows = len(grid)

for row in range(maxRows): 
    for match in re.finditer(pattern, grid[row]):
        
         # Get surrounding block for match (number in schematic)
        start = match.start()-1
        end =match.end()+1 # because exclusive upper, +1 to auto built in +1    
            
        # Adjust block for edge cases so still within bounds
        if (start<=-1): 
            start = 0
        if (end>=len(grid[row])):
            end = len(grid[row])-1
                
        if (row == 0): # only check same row and below
            block = grid[row][start:end]+ grid[row+1][start:end]
        elif (row == (maxRows-1) ): #only check same row and above
            block = grid[row][start:end]+ grid[row-1][start:end]
        else:
            block = grid[row][start:end] + grid[row-1][start:end] + grid[row+1][start:end]    
            
            #print(block)
            
            # Check if valid, i.e. if symbol in block
        if (re.search((r'/d+'), block)):
            partMultiply += int(match.group()) #match.group gets exact match from match object
                   
    print(partMultiply)      