import math

def GetSeatSpecs():
    f = open("input.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)-1):
        lines[i] = lines[i][:-1]
    return lines

def ParseSeatSpecRec(spec, specIndex, minRange, maxRange):
    #print("spec:",spec,"; specIndex: ",specIndex,"; minRange:",minRange,"; maxRange :",maxRange)
    if specIndex >= len(spec):
        return (minRange,maxRange)
    diff = maxRange - minRange
    mid = minRange+(diff/2)
    specChar = spec[specIndex]
    if specChar == "F" or specChar == "L":
        if diff == 1:
            return (minRange,minRange)
        else:
            maxRange = math.floor(mid)
    elif specChar == "B" or specChar == "R":
        if diff == 1:
            return (maxRange,maxRange)
        else:
            minRange = math.ceil(mid)
    return ParseSeatSpecRec(spec,specIndex+1,minRange,maxRange)

def ParseSeatSpec(spec,minRange,maxRange):
    rng = ParseSeatSpecRec(spec,0,int(minRange),int(maxRange))
    if rng[0] != rng[1]:
        print("Range not equal, spec:",spec," min:",rng[0],"; max:",rng[1])
    return rng[0]

class Seat:
    def __init__(self, spec):
        self.specification = spec;
        rowSpec = spec[0:7]
        columnSpec = spec[7:10]
        self.row = ParseSeatSpec(rowSpec,0,127)
        self.column = ParseSeatSpec(columnSpec,0,7)
        self.seatID = (self.row * 8) + self.column


def ParseSeats(seatSpecs):
    seats = []
    #for i in range(3):
    for i in range(len(seatSpecs)):
        seats.append(Seat(seatSpecs[i]))
    return seats

def HighestSeatNumber(seats):
    highestSeatNo = -1
    for i in range(len(seats)):
        if seats[i].seatID > highestSeatNo:
            highestSeatNo = seats[i].seatID
    return highestSeatNo

seatspecs = GetSeatSpecs()
seats = ParseSeats(seatspecs)
print(HighestSeatNumber(seats))
