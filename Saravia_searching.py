studentfile = open('gpa.txt', encoding = "utf8")
mydict = {}

def BuildDictionary(mydict, studentfile):
    for line in studentfile:
        wordList = line.split()
        name = wordList[0]
        GPA = wordList[1]
        mydict[name] = GPA

BuildDictionary(mydict, studentfile)
studentfile.close()

mingpa = float(input("Enter minimum GPA: "))
maxgpa = float(input("Enter maximum GPA: "))

def FindStudentsInDictionary(mydict, mingpa, maxgpa):
    inRange = 0

    for key in mydict:
        if mingpa <= float(mydict[key]) <= maxgpa:
            inRange += 1

    return inRange

FindStudentsInDictionary(mydict, mingpa, maxgpa)

mylist = []
studentfile = open('gpa.txt', encoding = "utf8")

def BuildLists(mylist, studentfile):
    for line in studentfile:
        wordList = line.split()
        mylist.append(wordList)

BuildLists(mylist, studentfile)
studentfile.close()

def SortListByName(mylist):
    nameSortList = []
    name = 0
    count = 0

    for nameList in mylist:
        nameSortList.append(nameList[0])

    while name < len(nameSortList):
        for names in range(name, len(mylist)):
            while count < ((len(nameSortList[name]) - 1) and (len(nameSortList[names]) - 1)):
                if (count + 1) == (len(nameSortList[name]) or len(nameSortList[names])):
                    break
                elif nameSortList[names][count] == nameSortList[name][count]:
                    count += 1
                else:
                    break

            if nameSortList[names][count] < nameSortList[name][count]:
                nameSortList[names], nameSortList[name] = nameSortList[name], nameSortList[names]

            count = 0
        name += 1

    return nameSortList

SortListByName(mylist)

def SortListByGPA(mylist):
    GPASortList = []
    minimumGPA =0

    for GPAList in mylist:
        GPASortList.append(GPAList[1])

    while minimumGPA < len(GPASortList):
        for GPA in range(minimumGPA, len(GPASortList)):
            if float(GPASortList[GPA]) < float(GPASortList[minimumGPA]):
                GPASortList[GPA], GPASortList[minimumGPA] = GPASortList[minimumGPA], GPASortList[GPA]
        minimumGPA += 1

    return GPASortList

SortListByGPA(mylist)

def StudentsInList_Iterative(mylist, mingpa, maxgpa):
    inRange = 0

    for GPAList in mylist:
        if mingpa <= float(GPAList[1]) <= maxgpa:
            inRange += 1

    return inRange

StudentsInList_Iterative(mylist, mingpa, maxgpa)

def StudentsInList_Recursive(mylist, mingpa, maxgpa):
    for GPAList in range(len(mylist)):
        if float(mylist[GPAList][1]) < mingpa or float(mylist[GPAList][1]) > maxgpa:
            mylist.pop(GPAList)
            return StudentsInList_Recursive(mylist, mingpa, maxgpa)

    return len(mylist)

StudentsInList_Recursive(mylist, mingpa, maxgpa)