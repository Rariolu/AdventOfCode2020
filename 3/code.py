def CreateGrid():
    f = open("input.txt", "r")
    lines = f.readlines()
    return lines

def FindTrees(grid):
    x = 3
    trees = 0
    print(len(grid))
    width = len(grid[0])
    #print(width)
    #for y in range(1, 34):
    for y in range(1,len(grid)):
        tempX = x % len(grid[y])
        if len(grid[y]) != width:
            print("width changed on "+str(y)+" to "+str(len(grid[y])))
        char = grid[y][tempX]
        tempLine = list(grid[y])
        if char == '#':
            trees+=1
            tempLine[tempX] = 'X'
        else:
            tempLine[tempX] = 'O'
        #print("".join(tempLine))
        x += 3
    return trees

print(FindTrees(CreateGrid()))
