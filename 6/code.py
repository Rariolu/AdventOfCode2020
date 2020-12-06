class Person:
    def __init__(self):
        self.affirmatives = []
    def AddYes(self, question):
        self.affirmatives.append(question)

class Group:
    def __init__(self):
        self.people = []
    def AddPerson(self, person):
        self.people.append(person)
    def FindCommonAffirmatives(self):
        affirmatives = {}
        for i in range(len(self.people)):
            person = self.people[i]
            affs = person.affirmatives
            for j in range(len(affs)):
                if affs[j] in affirmatives:
                    affirmatives[affs[j]]+=1
                else:
                    if i == 0:
                        affirmatives[affs[j]]=1
        mutual = []
        for i in affirmatives:
            if affirmatives[i] == len(self.people):
                mutual.append(i)
        #print(mutual)
        return mutual

def GetGroups():
    f = open("input.txt","r")
    groups = f.read().split("\n\n")
    return groups

def ParseGroups(answerGroups):
    groups = []
    letters =  list(map(chr, range(97, 123)))
    totalYes = 0
    for i in range(len(answerGroups)):
        group = Group()
        lines = answerGroups[i].split("\n")
        answeredQuestions = []
        for j in range(len(lines)):
            person = Person()
            line = lines[j]
            for k in range(len(line)):
                char = line[k]
                if char in letters:
                    person.AddYes(char)
                    if char not in answeredQuestions:
                        answeredQuestions.append(char)
            group.AddPerson(person)
        groups.append(group)
        totalYes += len(answeredQuestions)
    print("Total Affirmatives:",totalYes)
    return groups

def FindTotalMutualAffirmatives(parsedGroups):
    total = 0
    for i in range(len(parsedGroups)):
        mutualAffirmatives = parsedGroups[i].FindCommonAffirmatives()
        total += len(mutualAffirmatives)
    print("Total Mutual Affirmatives:",total)
    return total

groupAnswers = GetGroups()
groups = ParseGroups(groupAnswers)
FindTotalMutualAffirmatives(groups)
