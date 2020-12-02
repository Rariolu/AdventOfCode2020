def GetValue2():
    f = open("input.txt","r")
    l = f.readlines()
    for i in range(len(l)):
        num = int(l[i])
        for j in range(i+1,len(l)):
            otherNum = int(l[j])
            if num + otherNum == 2020:
                print(str(num)+" + "+str(otherNum)+" = 2020")
                return num * otherNum
        """otherNum = 2020-num
        strOtherNum = str(otherNum)
        if strOtherNum in l:
            print("blep")"""
    return -1

def GetValue3():
    f = open("input.txt","r")
    l = f.readlines()
    length = len(l)
    for i in range(length):
        num = int(l[i])
        for j in range(i+1,length):
            num2 = int(l[j])
            for k in range(j+1, length):
                num3 = int(l[k])
                if num + num2 + num3 == 2020:
                    print(l[i]+" + "+l[j]+" + "+l[k]+" = 2020")
                    return num * num2 * num3
    return -1

print(GetValue3())
