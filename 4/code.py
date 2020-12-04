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
        cleanPassport = passport.replace('\n',' ').replace('\t',' ')
        cleanPassport += " "
        fieldsFound = 0
        missingFields = []
        for k in range(len(expectedFields)):
            field = expectedFields[k]
            if field in passport:
                fieldIndex = cleanPassport.index(field)
                colonIndex = cleanPassport.find(":",fieldIndex)
                spaceIndex = cleanPassport.find(" ",colonIndex)
                #newLineIndex = passport.find("\n",colonIndex)
                breakIndex = spaceIndex#min(spaceIndex,newLineIndex)
                data = passport[(colonIndex+1):breakIndex]
                #print(data)
                #print("fieldIndex:",fieldIndex,"; colonIndex: ",colonIndex,"; spaceIndex: ",spaceIndex,"newLineIndex",newLineIndex,"breakIndex",breakIndex,data)
                fieldsFound += 1
            else:
                missingFields.append(field)
        if fieldsFound == len(expectedFields):
            validPassports.append(passport)
        else:
            u = 0
            #print(passport,missingFields,"\n")
    return validPassports

hexChars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
expColours = ["amb","blu","brn","gry","grn","hzl","oth"]

class PassportField:
    def __init__(self, fieldName, fieldType):
        self.fieldName = fieldName
        self.fieldType = fieldType
    def __init__(self, fieldName, fieldType, minValue, maxValue):
        self.fieldName = fieldName
        self.fieldType = fieldType
        self.minValue = minValue
        self.maxValue = maxValue
    def CheckValidity(self, data):
        typ = self.fieldType
        if typ == "4dnum":
            if len(data) != 4:
                return False
            if IntTryParse(data) == False:
                return False
            num = int(data)
            return num >= self.minValue and num <= self.maxValue
        if typ == "len":
            if "cm" not in data and "in" not in data:
                return False
            if "cm" in data:
                val = data[0:data.index("cm")]
                if IntTryParse(val) == False:
                    return False
                num = int(val)
                if num < 150 or num > 193:
                    return False
                return True
            if "in" in data:
                val = data[0:data.index("in")]
                if IntTryParse(val) == False:
                    return False
                num = int(val)
                if num < 59 or num > 76:
                    return False
                return True
        if typ == "hexcolour":
            if data[0] != '#':
                return False
            for i in range(1,len(data)):
                if data[i] not in hexChars:
                    return False
            return True
        if typ == "explicitcolour":
            if data not in expColours:
                return False
            return True
        if typ == "9dnum":
            if len(data) != 9:
                return False
            if IntTryParse(data) == False:
                return False
            return True
def IntTryParse(text):
    try:
        i = int(text)
        return True
    except:
        return False

passports = GetPassports()
validPassports = GetValidPassports(passports, ["byr","iyr","eyr","hgt","hcl","ecl","pid"])
"""for i in range(len(validPassports)):
    print(validPassports[i],"\n")"""
print(len(validPassports))
