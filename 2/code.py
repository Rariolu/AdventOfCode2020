def GetValidPasswords():
    f = open("input.txt","r")
    lines = f.readlines()
    validPasswords = []
    for i in range(len(lines)):
        text = lines[i]
        dashIndex = text.index("-")
        colonIndex = text.index(":")
        firstSpaceIndex = text.index(" ")
        minRange = int(text[0:dashIndex])
        maxRange = int(text[(dashIndex+1):firstSpaceIndex])
        character = text[(firstSpaceIndex+1):colonIndex]
        secondSpaceIndex = text.find(" ",firstSpaceIndex+1)
        password = text[(secondSpaceIndex+1):(len(text)-1)]
        count = password.count(character)
        if count >= minRange and count <= maxRange:
            validPasswords.append(password)
            print(password)
    return validPasswords

def GetActualValidPasswords():
    f = open("input.txt","r")
    lines = f.readlines()
    validPasswords = []
    for i in range(len(lines)):
        text = lines[i]
        dashIndex = text.index("-")
        colonIndex = text.index(":")
        firstSpaceIndex = text.index(" ")
        firstCharIndex = int(text[0:dashIndex])
        secondCharIndex = int(text[(dashIndex+1):firstSpaceIndex])
        character = text[(firstSpaceIndex+1):colonIndex]
        secondSpaceIndex = text.find(" ",firstSpaceIndex+1)
        password = text[(secondSpaceIndex+1):(len(text)-1)]
        count = password.count(character)
        firstChar = password[firstCharIndex-1]
        secondChar = password[secondCharIndex-1]
        isFirstChar = firstChar == character
        isSecondChar = secondChar == character
        if isFirstChar or isSecondChar:
            if isFirstChar and isSecondChar:
                continue
            validPasswords.append(password)
            print(password)
    return validPasswords

print(len(GetActualValidPasswords()))
