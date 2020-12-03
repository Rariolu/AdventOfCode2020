def CreateGrid():
    f = open("input.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)-1):
        lines[i] = lines[i][:-1]
    return lines

def FindTrees(grid, xIncrease, yIncrease):
    x = 0
    trees = 0
    width = len(grid[0])
    for y in range(0, len(grid),yIncrease):
        tempX = x % width
        char = grid[y][tempX]
        tempLine = list(grid[y])
        if char == '#':
            trees+=1
            tempLine[tempX] = 'X'
        else:
            tempLine[tempX] = 'O'
        #print("".join(tempLine))
        x += xIncrease
    return trees

print(FindTrees(CreateGrid(),3,1))
