class Person:
    def __init__(self):
        self.affirmatives = []
    def AddYes(self, question):
        self.affirmatives.append(question)

class Group:
    def __init(self):
        self.people = []
    def AddPerson(person):
        self.people.append(person)

def GetGroups():
    f = open("input.txt","r")
    """lines = f.readlines()
    groups = []
    currentGroup = ""
    for i in range(len(lines)):
        line = lines[i]
        atEnd = i == len(lines)-1
        if len(line) > 1:
            currentGroup += line
        if line == "\n" or atEnd:
            if currentGroup[len(currentGroup)-1] == "\n":
                currentGroup = currentGroup[:-1]
            #print(currentGroup+"\nblep\n")
            groups.append(currentGroup)
            currentGroup = ""
    return groups"""
    groups = f.read().split("\n\n")
    return groups

groupAnswers = GetGroups()
for i in range(len(groupAnswers)):
    print(groupAnswers[i]+"\n")
