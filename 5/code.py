def GetSeats():
    f = open("input.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    return lines

print(GetSeats())
