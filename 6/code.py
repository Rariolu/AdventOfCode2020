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

groupAnswers = GetGroups()
groups = ParseGroups(groupAnswers)
