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

slopeGrid = CreateGrid()
r1d1 = FindTrees(slopeGrid, 1, 1)
r3d1 = FindTrees(slopeGrid, 3, 1)
r5d1 = FindTrees(slopeGrid, 5, 1)
r7d1 = FindTrees(slopeGrid, 7, 1)
r1d2 = FindTrees(slopeGrid, 1, 2)

print("R1 D1: ",r1d1)
print("R3 D1: ",r3d1)
print("R5 D1: ",r5d1)
print("R7 D1: ",r7d1)
print("R1 D2: ",r1d2)
print("Product: ",r1d1*r3d1*r5d1*r7d1*r1d2)
