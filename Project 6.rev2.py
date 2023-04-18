#Justin Trebour
#COP2002.0M1
#04/17/2023
#Project 6.rev2
#This program should allow for the processing of Program Codes

def main():




def rosFile():
    
    
    with open("Stu_Ros.csv") as rosterFile:
        linesFromFile = rosterFile.readlines()

    firstLineRos = linesFromFile[0]

    firstLineSplitRos = firstLineRos.split(",")

    col1 = firstLineSplitRos[5]

    progCode = []

    for line in linesFromFile:
        line = line.split(",")
        progCode.append(line[5])

    print(progCode)


def proFile():

    with open("Prog_Code.csv") as progFile:
        linesFromFileTwo = progFile.readlines()

    firstLineProg = linesFromFileTwo[0]

    firstLineSplitProg = firstLineProg.split(",")

    col2 = firstLineSplitProg[1]

    progName = []

    for line in linesFromFileTwo:
        line = line.rstrip("\n").split(",")
        progName.append(line[1])

    print(progName)




rosFile()
proFile()

if (__name__ == "__main__"):
    main()


#print(progName)



## with open("Stu_Roster.csv") as rosterFile:
##    linesFromFile = rosterFile.readlines()
##
## with open("Prog_Code.csv") as progFile:
##     linesFromFileTwo = progFile.readlines()

## firstLineRos = linesFromFile[0]

##  firstLineSplitRos = firstLineRos.split(",")

##  col1 = firstLineSplitRos[5]

##  progCode = []

##  for line in linesFromFile:
##      line = line.split(",")
##      progCode.append(line[5])


##  firstLineProg = linesFromFileTwo[0]

##  firstLineSplitProg = firstLineProg.split(",")

##  col2 = firstLineSplitProg[1]

##  progName = []

##  for line in linesFromFileTwo:
##      line = line.rstrip("\n").split(",")
##      progName.append(line[1])