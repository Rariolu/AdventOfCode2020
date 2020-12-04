def GetPassports():
    f = open("input.txt", "r")
    lines = f.readlines()
    currentPassport = ""
    passports = []
    for i in range(len(lines)):
        line = lines[i]
        atEnd = i == len(lines)-1
        if line == '\n' or atEnd:
            if atEnd:
                currentPassport += line
            else:
                currentPassport = currentPassport[:-1]
            passports.append(currentPassport)
            currentPassport = ""
        else:
            currentPassport += line
    return passports

def GetValidPassports(passports, expectedFields):
    validPassports = []
    for i in range(len(passports)):
        passport = passports[i]
        fieldsFound = 0
        missingFields = []
        for k in range(len(expectedFields)):
            field = expectedFields[k]
            if field in passport:
                fieldsFound += 1
            else:
                missingFields.append(field)
        if fieldsFound == len(expectedFields):
            validPassports.append(passport)
        else:
            print(passport,missingFields,"\n")
    return validPassports

passports = GetPassports()
validPassports = GetValidPassports(passports, ["byr","iyr","eyr","hgt","hcl","ecl","pid"])
"""for i in range(len(validPassports)):
    print(validPassports[i],"\n")"""
print(len(validPassports))
