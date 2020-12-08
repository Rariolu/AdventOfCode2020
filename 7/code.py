def GetRules():
    f = open("input.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)-1):
        lines[i] = lines[i][:-1]
    return lines

def Temp(rules,bagType):
    count = 0
    for i in range(len(rules)):
        rule = rules[i]
        if bagType in rule:
            count+=1
            print(rule)
    return count

def ElementPresent(bagDict,currentElement, element):
    if currentElement == element:
        return True
    if currentElement in bagDict:
        childBags = bagDict[currentElement]
        for i in range(len(childBags)):
            if ElementPresent(bagDict, childBags[i], element):
                return True
    return False
        

def FindBagsContaining(rules, bagType):
    containingBags = []
    bagNames = []
    bagDict = {}
    #for i in range(1):
    for i in range(len(rules)):
        rule = rules[i]
        bagsIndex = rule.index(" bags")
        bagName = rule[0:bagsIndex]
        bagNames.append(bagName)
        bagDict[bagName] = []
        containIndex = rule.index("contain")
        bagsContained = rule[containIndex+7:len(rule)]
        separateTypes = bagsContained.split("bag")
        for j in range(len(separateTypes)):
            sT = separateTypes[j]
            if " " in sT:
                spaceIndex = sT.index(" ")
                sT = sT[spaceIndex+1:]
                words = sT.split(" ")
                col = words[1] + " " + words[2]
                bagDict[bagName].append(col)
    for i in range(len(bagNames)):
        if bagNames[i] != bagType:
            if ElementPresent(bagDict,bagNames[i],"shiny gold"):
                containingBags.append(bagNames[i])
        
    print(containingBags)
            
    """for i in range(len(rules)):
        rule = rules[i]
        containIndex = rule.index("contain")
        bagsIndex = rule.index(" bags")
        bagName = rule[0:bagsIndex]
        bagsContained = rule[containIndex+7:len(rule)]
        if bagType in bagsContained:
            print(rule)
            containingBags.append(bagName)
        else:
            for i in range(len(containingBags)):
                if containingBags[i] in bagsContained:
                    print(rule)
                    containingBags.append(bagName)
                    break"""
    return containingBags

rules = GetRules()
print(len(FindBagsContaining(rules,"shiny gold bag")))
#print(Temp(rules,"shiny gold bag"))
