def GetCode():
    f = open("input.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    return lines

def RunCode(code):
    accumulator = 0
    programCounter = 0
    currentInstruction = 0
    executedLines = []
    hasntRepeated = True
    while hasntRepeated:
        line = code[programCounter]
        currentInstruction = programCounter
        programCounter += 1
        info = line.split(" ")
        op = info[1][0]
        num = int(info[1][1:])
        if info[0] == "acc":
            if op == '+':
                accumulator += num
            elif op == '-':
                accumulator -= num
        if info[0] == "jmp":
            if op == '+':
                programCounter = currentInstruction + num
            elif op == '-':
                programCounter = currentInstruction - num
        executedLines.append(currentInstruction)
        print(line,"|",currentInstruction)
        if programCounter in executedLines:
            hasntRepeated = False
    print("PC:",programCounter,"; acc:",accumulator)

RunCode(GetCode())
