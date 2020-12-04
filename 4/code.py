def GetPassports():
    f = open("input.txt", "r")
    lines = f.readlines()
    currentPassport = ""
    passports = []
    for i in range(len(lines)):
        line = lines[i]
        if line == '\n':
            currentPassport = currentPassport[:-1]
            passports.append(currentPassport)
            currentPassport = ""
        else:
            currentPassport += line
    return passports

